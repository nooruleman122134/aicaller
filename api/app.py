import os
import sys
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from twilio.twiml.voice_response import VoiceResponse

# 📂 Load environment variables
load_dotenv()

# 🔧 Fix import paths for internal modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 🧠 Internal imports
from voice.dynamic_voice_play import play_ride_voice
from firebase.firebase_utils import get_realtime_status
from db import init_db
from db.db_utils import get_ride_status
from knowledge_base import get_voice_message

# 🚀 Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

# 🗄️ Link SQLAlchemy
init_db(app)

# 🔐 Email Auth
ALLOWED_EMAILS = ['noor@example.com', 'boss@weride.com']

# 🌐 Home/Login Page
@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        if email in ALLOWED_EMAILS:
            return redirect(url_for('dashboard'))
        else:
            error = "⛔ You are not authorized to log in."
    return render_template('index.html', error=error)

# ✅ Dashboard Route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# ▶️ Play Local Voice (Button)
@app.route('/play-voice', methods=['POST'])
def play_voice():
    play_ride_voice()
    return redirect(url_for('dashboard'))

# 📞 Twilio Webhook
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    ride_id = request.args.get('id', 1)
    status, issue = get_ride_status(ride_id)

    message = get_voice_message(status)
    resp = VoiceResponse()
    resp.say(message, voice='alice', language='ur-PK')
    return str(resp)

# ⚠️ Vercel requires this WSGI handler
def handler(environ, start_response):
    return app(environ, start_response)
handler = app