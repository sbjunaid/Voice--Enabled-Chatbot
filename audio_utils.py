import sounddevice as sd
import scipy.io.wavfile as wav

def record_audio(filename="input.wav", duration=5, fs=16000, device=2):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, device=2)
    sd.wait()
    wav.write(filename, fs, audio)
    print("Recording saved")

