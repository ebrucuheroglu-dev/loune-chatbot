# Loune - Elbise Kiralama Chatbot

Loune, özel günler (davet, mezuniyet, düğün gibi) için elbise kiralama
hizmeti sunan bir platformun yapay zeka destekli sohbet asistanıdır.

## Özellikler
- Müşterilerle sohbet ederek elbise, kombin ve kiralama tercihlerini öğrenir
- Müşteri iletişim bilgilerini (lead) veritabanına kaydeder
- Yönetim paneli üzerinden kayıtları listeler

## Teknolojiler
- Python, Flask
- SQLite
- Groq API (yapay zeka, model: openai/gpt-oss-20b)
- Wix Velo (frontend)

## Canlı Bağlantılar
- **Backend (API):** https://loune-chatbot.onrender.com
- **Wix Sitesi:** https://ebrucuheroglu.wixstudio.com/my-site-2

## Kurulum (Yerel Geliştirme)
1. Sanal ortam oluşturun: `python -m venv venv`
2. Sanal ortamı aktive edin
3. Bağımlılıkları kurun: `pip install -r requirements.txt`
4. `.env` dosyasına Groq API anahtarınızı ekleyin
5. Sunucuyu başlatın: `python run.py`
6. Tarayıcıda `http://localhost:5000` adresini açın

## API Uç Noktaları
- `GET /health` - Sunucu durumu
- `POST /api/sohbet` - Chatbot ile konuşma
- `POST /api/leads` - Yeni müşteri kaydı
- `GET /api/leads` - Tüm kayıtları listele