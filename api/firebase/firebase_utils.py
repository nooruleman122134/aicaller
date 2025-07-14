import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load credentials & initialize Firebase
cred_path = os.getenv("FIREBASE_CRED_PATH")
db_url = os.getenv("FIREBASE_DB")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': db_url
})

# Function to get ride status
def get_realtime_status(ride_id):
    ref = db.reference(f"rides/{ride_id}")
    return ref.get() or {}
