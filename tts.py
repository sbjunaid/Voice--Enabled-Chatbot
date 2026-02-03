import sounddevice as sd
from transformers import pipeline

# Load Hindi TTS pipeline (offline after first download)
tts = pipeline(
    task="text-to-speech",
    model="facebook/mms-tts-hin"
)

def speak(text):
    speech = tts(text)
    audio = speech["audio"]
    sampling_rate = speech["sampling_rate"]

    sd.play(audio, samplerate=sampling_rate)
    sd.wait()
