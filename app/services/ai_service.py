import requests
from flask import current_app
class AIServiceError(Exception):
    pass

class AIService:
    def __init__(self):
        self.api_key = current_app.config.get('GROQ_API_KEY', '')
        self.business_context = current_app.config.get('BUSINESS_CONTEXT', '')
        self.api_url = "https://api.groq.com/openai/v1/chat/completions" 

    def yanit_uret(self, mesaj, gecmis=None):
        if not self.api_key:
            return "Demo modundayiz: Groq API anahtari tanimli degil."
        messages = [{"role": "system", "content": self.business_context}]

        if gecmis:
            messages.extend(gecmis)

        messages.append({"role": "user", "content": mesaj})
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 500
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=15)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except requests.RequestException as e:
            raise AIServiceError(f"AI servisi hatasi: {e}")      