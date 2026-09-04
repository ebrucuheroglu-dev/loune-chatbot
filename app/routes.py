from flask import Blueprint, request, jsonify, render_template
from app.database import lead_ekle, tum_leadler
from app.services.ai_service import AIService, AIServiceError

api_bp = Blueprint('api', __name__)
pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def index():
    return render_template('index.html')

@pages_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@api_bp.route('/sohbet', methods=['POST'])
def sohbet():
    data = request.get_json()
    mesaj = data.get('mesaj')
    gecmis = data.get('gecmis', [])

    if not mesaj:
        return jsonify({'basari': False, 'hata': 'Mesaj bos olamaz.'}), 400

    try:
        ai_service = AIService()
        cevap = ai_service.yanit_uret(mesaj, gecmis)
        return jsonify({'basari': True, 'cevap': cevap}), 200
    except AIServiceError as e:
        return jsonify({'basari': False, 'hata': str(e)}), 503

@api_bp.route('/leads', methods=['POST'])
def leads_ekle():
    data = request.get_json()
    isim = data.get('isim')
    telefon = data.get('telefon')
    mesaj = data.get('mesaj')
    etkinlik = data.get('etkinlik')

    if not isim or not telefon:
        return jsonify({'basari': False, 'hata': 'Isim ve telefon zorunlu.'}), 400

    lead_ekle(isim, telefon, mesaj, etkinlik)
    return jsonify({'basari': True, 'mesaj': 'Kayit alindi.'}), 201

@api_bp.route('/leads', methods=['GET'])
def leads_listele():
    leads = tum_leadler()
    sonuc = [dict(lead) for lead in leads]
    return jsonify({'basari': True, 'leads': sonuc}), 200

                        