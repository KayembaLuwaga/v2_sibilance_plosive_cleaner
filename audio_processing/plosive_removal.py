# audio_processing/plosive_removal.py
from pydub import AudioSegment
import numpy as np
from scipy.signal import butter, lfilter

def remove_plosive(audio, cutoff_frequency):
    # Convert AudioSegment to NumPy array
    audio_array = np.array(audio.get_array_of_samples())
    
    # Apply a low-pass filter to remove plosives
    nyquist = 0.5 * audio.frame_rate
    normal_cutoff = cutoff_frequency / nyquist
    b, a = butter(4, normal_cutoff, btype='low', analog=False)
    filtered_audio = lfilter(b, a, audio_array).astype(np.int16)
    
    # Convert back to AudioSegment
    filtered_audio_segment = AudioSegment.from_array(filtered_audio, frame_rate=audio.frame_rate, sample_width=2, channels=1)
    
    return filtered_audio_segment
