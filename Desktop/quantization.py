### import packages
import numpy as np
import pydub
import wave
import matplotlib.pyplot as plt
from pydub import AudioSegment
import os
import json

### write down your code here



wave_file = wave.open(r'C:\Users\idea\hw01-cheng-jingwen\wav\original\Close_back_rounded_vowel.wav', 'r')
f = wave_file
samplewidth = f.getsampwidth()
framerate = f.getframerate()
numframes = f.getnframes()
Wav_Data = wave_file.readframes(numframes)
Wav_Data = np.fromstring(Wav_Data, dtype=np.int16)
Wav_Data = Wav_Data * 1.0 / (max(abs(Wav_Data)))

### Sorry,  I really don't know how to quantise the sound 