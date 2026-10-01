import matplotlib.pyplot as plt

def plot_spectrogram(id, stft, times, frequencies) :

    plt.figure(figsize=(12, 3))
    plt.imshow(stft, aspect='auto', cmap='jet', origin='lower', extent=[times.min(), times.max(), frequencies.min(), frequencies.max()])
    plt.title(f'STFT of original ECG [{id}]')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar(label='db')
    plt.tight_layout()
    plt.show()

    return
