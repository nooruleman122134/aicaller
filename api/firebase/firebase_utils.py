# File: api/firebase/firebase_utils.py

import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

def init_firebase():
    if not firebase_admin._apps:  # Prevent multiple initializations
        cred_path = os.getenv("FIREBASE_CRED_PATH")
        db_url = os.getenv("FIREBASE_DB")

        if not cred_path or not db_url:
            raise ValueError("⚠️ Firebase environment variables are missing.")

        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': db_url
        })

def get_realtime_status(ride_id):
    ref = db.reference(f"/rides/{ride_id}")
    return ref.get() or {}
