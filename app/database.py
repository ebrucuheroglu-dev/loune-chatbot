import sqlite3
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE_URL'])
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db(app):
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                etkinlik TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()   

def lead_ekle(isim, telefon, mesaj=None, etkinlik=None):
    db = get_db()
    db.execute(
        'INSERT INTO leads (isim, telefon, mesaj, etkinlik) VALUES (?, ?, ?, ?)',
        (isim, telefon, mesaj, etkinlik)
    )
    db.commit()

def tum_leadler():
    db = get_db()
    leads = db.execute('SELECT * FROM leads ORDER BY tarih DESC').fetchall()
    return leads             