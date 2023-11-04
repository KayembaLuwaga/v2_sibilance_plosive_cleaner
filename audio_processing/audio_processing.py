# audio_processing/audio_processing.py
from pydub import AudioSegment
from audio_processing.sibilance_removal import remove_sibilance
from audio_processing.plosive_removal import remove_plosive

def process_audio(audio_file, remove_sibilance_flag, remove_plosive_flag, cutoff_frequency, silence_thresh):
    audio = AudioSegment.from_file(audio_file)

    if remove_sibilance_flag:
        audio = remove_sibilance(audio_file, silence_thresh)

    if remove_plosive_flag:
        audio = remove_plosive(audio_file, cutoff_frequency)

    return audio
