import os
import matplotlib.pyplot as plt
import numpy as np

def plot_ecg(id, ecg_signal, fs):

    total_samples = len(ecg_signal)
    time = np.arange(total_samples) / fs

    plt.figure(figsize=(12, 4))
    plt.plot(time, ecg_signal, '#10a37f')
    plt.title(f'ECG Signal for Patient ID: {id}')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()
    return


def plot_ecgseg(id, ecg_segment, fs, num_seg):
    total_samples = len(ecg_segment)
    time = np.arange(total_samples) / fs

    plt.figure(figsize=(12, 4))
    plt.plot(time, ecg_segment, '#10a37f')
    plt.title(f'ECG Signal for {id} segment_{num_seg}"')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()
    return
