# audio_processing/sibilance_removal.py
from pydub import AudioSegment
from pydub.silence import split_on_silence

def remove_sibilance(audio_file, silence_thresh):
    audio = AudioSegment.from_file(audio_file)

    # Split audio on silence with the user-specified threshold
    audio_segments = split_on_silence(audio, silence_thresh=silence_thresh)  # Use the provided silence threshold

    # Remove silent segments (assumed to be sibilance)
    non_silent_audio = AudioSegment.empty()
    for segment in audio_segments:
        if segment.duration_seconds > 0.5:  # Adjust the duration threshold as needed
            non_silent_audio += segment

    return non_silent_audio
