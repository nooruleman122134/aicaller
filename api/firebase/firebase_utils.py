import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

load_dotenv()

# Point directly to the correct path
cred_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'weride-adminsdk.json')
db_url = os.getenv("FIREBASE_DB")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': db_url
})

def get_realtime_status(ride_id):
    ref = db.reference(f"rides/{ride_id}")
    return ref.get() or {}
