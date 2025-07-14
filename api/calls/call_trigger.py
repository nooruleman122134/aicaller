from twilio_utils import make_call

# 🔄 Verified number & correct ngrok voice route
recipient_number = "+923295029168"
ngrok_voice_url = "https://9caf129ac3a8.ngrok-free.app/voice"  # ← include /voice

# ✅ Trigger the call
make_call(recipient_number, ngrok_voice_url)
