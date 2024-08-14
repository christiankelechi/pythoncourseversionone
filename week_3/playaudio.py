from pydub import AudioSegment
from pydub.playback import play

# Load your .wav file
audio = AudioSegment.from_wav("week_3/alarmwave.wav")

# Play the .wav file
play(audio)
