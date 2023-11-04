# audio_processing/plosive_removal.py
from pydub import AudioSegment
from scipy import signal  # Import the signal module from scipy
import numpy as np

def remove_plosive(audio_file, cutoff_frequency):
    audio = AudioSegment.from_file(audio_file)

    # Convert the audio to a NumPy array for manipulation
    audio_array = np.array(audio.get_array_of_samples())

    # Implement plosive removal logic here with the user-specified cutoff frequency
    nyquist = 0.5 * audio.frame_rate
    normal_cutoff = cutoff_frequency / nyquist
    b, a = signal.butter(4, normal_cutoff, btype='low', analog=False)
    filtered_audio = signal.lfilter(b, a, audio_array).astype(np.int16)

    # Create a new AudioSegment from the filtered NumPy array
    filtered_audio_segment = AudioSegment(filtered_audio.tobytes(), frame_rate=audio.frame_rate,
                                          sample_width=filtered_audio.dtype.itemsize, channels=1)

    return filtered_audio_segment
