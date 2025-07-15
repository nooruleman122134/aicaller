import sys
import os

# Add the parent directory of 'api' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from api.firebase.firebase_utils import get_realtime_status
import threading

def speak(message):
    print(f"🎤 Speaking: {message}")

def play_ride_voice():
    data = get_realtime_status(1)
    status = data.get("status")
    issue = data.get("issue")

    message = "Welcome to WeRide."

    if status == "arrived":
        message = "Your driver has arrived. Please confirm the vehicle before boarding."
    elif status == "cancelled":
        message = "Your ride has been cancelled. Please book again."
    elif status == "completed":
        message = "Thank you for riding with WeRide. We hope you had a smooth trip."
    elif issue == "suspicious_noise":
        message = "We have detected a possible issue. Press 1 if you're safe, or 2 if you need help."

    t = threading.Thread(target=speak, args=(message,))
    t.start()
