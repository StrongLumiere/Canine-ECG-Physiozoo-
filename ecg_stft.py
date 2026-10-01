from scipy import signal
import numpy as np

"""
window length = 0.1 * fs = 50 -> So we do 64 for window by han window
nperseg(window) = 64
noverlap = 32 (50%)
"""
def ecg_stft(ecg_signal, fs):
    frequencies, times, stft = signal.stft(ecg_signal, fs, nperseg=64, noverlap=32)

    # log scale (by db) ,1e-10 for not to be divided by 0
    stft = 10 * np.log10(abs(stft+ 1e-10))

    return  frequencies, times, stft




