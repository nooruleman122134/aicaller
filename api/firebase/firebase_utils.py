import os
import firebase_admin
from firebase_admin import credentials, db

def init_firebase():
    cred_path = os.getenv("FIREBASE_CRED_PATH")
    db_url = os.getenv("FIREBASE_DB")

    if not cred_path:
        raise Exception("FIREBASE_CRED_PATH is not set.")
    if not db_url:
        raise Exception("FIREBASE_DB is missing.")

    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': db_url
    })

def get_realtime_status(ride_id):
    ref = db.reference(f"/rides/{ride_id}")
    return ref.get() or {}
