from flask import Flask
from flask_cors import CORS
from config import config
from app.database import init_db

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    CORS(app, origins=app.config.get('CORS_ORIGINS', '*'))

    init_db(app)

    from app.routes import api_bp, pages_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(pages_bp)

    @app.route('/health')
    def health():
        return {'durum': 'aktif'}

    return app    