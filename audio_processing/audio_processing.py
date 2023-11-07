from pydub import AudioSegment
from audio_processing.sibilance_removal import remove_sibilance
from audio_processing.plosive_removal import remove_plosive

def process_audio(input_path, output_path, remove_sibilance_flag, remove_plosive_flag, cutoff_frequency, silence_thresh):
    audio = AudioSegment.from_file(input_path)
    audio_length = len(audio)  # Get the length of the original audio

    if remove_sibilance_flag:
        audio = remove_sibilance(audio, silence_thresh, audio_length)

    if remove_plosive_flag:
        audio = remove_plosive(audio, cutoff_frequency, audio_length)

    audio.export(output_path, format='wav')
