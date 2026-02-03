from audio_utils import record_audio
from stt import transcribe
from tts import speak
import scipy.io.wavfile as wav
from translate import to_hindi



if __name__ == "__main__":
    record_audio()
    text = transcribe("input.wav")
    print("Transcribed:", text)

    hindi_text = to_hindi(text)
    response = f"आपने कहा: {hindi_text}"
    speak(response)

    
