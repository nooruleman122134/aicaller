import os
import sys
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from twilio.twiml.voice_response import VoiceResponse

# Load .env variables
load_dotenv()

# Fix import paths
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Internal imports
from firebase.firebase_utils import init_firebase, get_realtime_status
from db import init_db
from db.db_utils import get_ride_status
from voice.dynamic_voice_play import play_ride_voice
from knowledge_base import get_voice_message

# Initialize Firebase
init_firebase()

# Flask app
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))

# Configure DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
init_db(app)

# Whitelisted Emails
ALLOWED_EMAILS = ['noor@example.com', 'boss@weride.com']

# Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        if email in ALLOWED_EMAILS:
            return redirect(url_for('dashboard'))
        error = "You are not authorized."
    return render_template('index.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/play-voice', methods=['POST'])
def play_voice():
    play_ride_voice()
    return redirect(url_for('dashboard'))

@app.route('/voice', methods=['GET', 'POST'])
def voice():
    ride_id = request.args.get('id', 1)
    data = get_realtime_status(ride_id)
    status = data.get("status")
    message = get_voice_message(status) if status else "WeRide status unknown."
    
    response = VoiceResponse()
    response.say(message, voice='alice', language='en-US')
    return str(response)

# Vercel deployment handler
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

# ✅ Local run
if __name__ == "__main__":
    app.run(debug=True)
