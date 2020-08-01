### import packages

### write down your code here

import numpy as np
import pydub
import wave
import matplotlib .pyplot as plt
from pydub import AudioSegment
import os
import json


def Resample(input_signal,src_f,tar_fs):
    dtype = input_signal.dtype
    audio_len = len(input_signal)
    audio_time_max = 1.0*(audio_len-1) / src_fs
    src_time = 1.0 * np.linspace(0,audio_len,audio_len) / src_fs
    tar_time = 1.0 * np.linspace(0,np.int(audio_time_max*tar_fs),np.int(audio_time_max*tar_fs)) / tar_fs
    output_signal = np.interp(tar_time,src_time,input_signal).astype(dtype)

    return output_signal

if __name__ == '__main__':

    wave_file = r'C:\Users\idea\hw01-cheng-jingwen\wav\original\Close_back_rounded_vowel.wav'
    audio_file = wave.open(wave_file, 'rb')
    audio_data = audio_file.readframes(audio_file.getnframes())
    audio_data_short = np.fromstring(audio_data, np.short)
    src_fs = audio_file.getframerate()
    src_chanels = audio_file.getnchannels()
    str_data = audio_file.readframes(src_fs)
    wave_data = np.fromstring(str_data, dtype=np.int16)

    if src_chanels > 1:
        audio_data_short = audio_data_short[::src_chanels]

    tar_fs = np.int(src_fs * 0.5)
audio_data_short0=Resample(audio_data_short,src_fs,tar_fs)
def DrawSpectrum(wwav_data,framerate):

    plt.figure(figsize=(4,3))
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()
wave_data=audio_data_short0
framerate=tar_fs
DrawSpectrum(wave_data,framerate)




