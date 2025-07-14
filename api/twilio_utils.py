from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def make_call(to_number, twiml_url):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    client = Client(account_sid, auth_token)

    try:
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url=twiml_url
        )
        print(f"📞 Call initiated! SID: {call.sid}")
        return call.sid
    except Exception as e:
        print(f"❌ Call failed: {e}")
        return None
