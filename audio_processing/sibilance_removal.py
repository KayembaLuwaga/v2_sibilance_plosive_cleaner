# audio_processing/sibilance_removal.py
import librosa
import numpy as np
from pydub import AudioSegment

def remove_sibilance(audio, silence_thresh, audio_length):
    # Convert AudioSegment to NumPy array
    audio_array = np.array(audio.get_array_of_samples())

    # Apply spectral analysis using Librosa
    stft = librosa.stft(audio_array.astype(float))

    # Find sibilant frequency components based on the threshold
    sibilance_mask = np.abs(stft) > silence_thresh

    # Remove sibilant components
    stft_clean = stft * ~sibilance_mask

    # Inverse transform to obtain clean audio
    audio_clean = librosa.istft(stft_clean)

    # Ensure processed audio matches the original audio length
    processed_audio = AudioSegment(
        audio_clean.tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=audio.sample_width,
        channels=audio.channels,
    )[:audio_length]

    return processed_audio
