# audio_processing/sibilance_removal.py
import librosa
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def remove_sibilance(audio, silence_thresh):
    # Convert AudioSegment to NumPy array
    audio_array = np.array(audio.get_array_of_samples())
    
    # Apply spectral analysis using Librosa
    stft = librosa.stft(audio_array.astype(float))
    
    # Find sibilant frequency components based on threshold
    sibilance_mask = np.abs(stft) > silence_thresh
    
    # Remove sibilant components
    stft_clean = stft * ~sibilance_mask
    
    # Inverse transform to obtain clean audio
    audio_clean = librosa.istft(stft_clean)
    
    # Convert back to AudioSegment
    audio_clean = AudioSegment.from_array(audio_clean.astype(np.int16), frame_rate=audio.frame_rate, sample_width=2, channels=1)
    
    return audio_clean
