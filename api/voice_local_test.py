from gtts import gTTS
import os

# Urdu message
message = "السلام علیکم! آپ کی رائڈ آ چکی ہے۔ شکریہ WeRide استعمال کرنے کا۔"

# Generate TTS
tts = gTTS(text=message, lang='ur')
tts.save("ride_voice.mp3")

# Play the audio file (Windows)
os.system("start ride_voice.mp3")
