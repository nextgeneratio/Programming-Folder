import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


# Set the parameters for recording
duration = 5  # seconds
fs = 44100  # Sample rate
