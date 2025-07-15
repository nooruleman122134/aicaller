import threading
from api.firebase.firebase_utils import get_realtime_status

def speak(message):
    print(f"🔊 Speaking: {message}")  # Replace with pyttsx3 if needed

def play_ride_voice():
    data = get_realtime_status(1)
    status = data.get("status")
    issue = data.get("issue")

    message = "Welcome to WeRide."

    if status == "arrived":
        message = "Your driver has arrived."
    elif status == "cancelled":
        message = "Your ride has been cancelled."
    elif status == "completed":
        message = "Thank you for riding with WeRide."
    elif issue == "suspicious_noise":
        message = "Possible issue detected. Press 1 if safe."

    t = threading.Thread(target=speak, args=(message,))
    t.start()
