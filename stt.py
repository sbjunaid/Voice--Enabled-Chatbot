from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio 

#load, save and manipulate audio files with support for formats like WAV, MP3, FLAC, and Sphere.

processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")

def transcribe(audio_path):
    speech, sr = torchaudio.load(audio_path)
    inputs = processor(speech.squeeze(), sampling_rate=sr, return_tensors="pt").input_features
    predicted_ids = model.generate(inputs)
    text = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    return text[0]
