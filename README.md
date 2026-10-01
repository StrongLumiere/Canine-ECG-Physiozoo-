# In a nuts shell on Canine-ECG-Physiozoo- Projects
An end-to-end Python framework for ECG signal processing and feature extraction. Converts raw cardiac signals into time-frequency STFT spectrograms and transforms them into 2D polar coordinate images. Includes Pan-Tompkins R-peak detection, sliding window segmentation, and automated dataset generation tailored for CNN-based deep learning workflows.

<img width="2207" height="1037" alt="image" src="https://github.com/user-attachments/assets/5d6d1e4f-3648-4c45-9404-f5034700fc30" />



## 🫀 ECG Signal Processing & Polar Spectrogram Pipeline

A comprehensive Python pipeline designed for preprocessing Electrocardiography (ECG) signals, performing Short-Time Fourier Transform (STFT), and transforming spectrograms into 2D polar coordinate representations. 
This repository provides an end-to-end workflow for analyzing ECG waveforms and generating image-based feature representations suitable for deep learning models (e.g., CNNs).

---

## 📌 Key Features

- **ECG Signal Processing**: Load and visualize raw multi-channel/single-channel ECG data.
- **R-Peak Detection**: Signal cleaning and feature enhancement via the Pan-Tompkins algorithm.
- **Windowing & Segmentation**: Slice continuous long-term ECG recordings into uniform segments.
- **Time-Frequency Analysis**: Generate high-resolution time-frequency spectrograms using STFT.
- **Polar Coordinate Transformation**: Convert Cartesian spectrograms into polar representation for spatial feature map generation.
- **Dataset Generation**: Automated pipeline to export $224 \times 224$ images tailored for model training.

---

## 📁 Project Structure

```text
├── src/
│   ├── path_setting.py           # Subject/Dog ID mapping and dataset directory setup
│   ├── ecg_read.py               # Raw ECG file reader
│   ├── Pan_tompkins.py           # Pan-Tompkins algorithm for QRS detection
│   ├── ecg_windowing.py          # Sliding window segmentation logic
│   ├── ecg_stft.py               # Short-Time Fourier Transform execution
│   ├── polar_transform.py        # Cartesian to polar coordinate transformation
│   ├── plot_*.py                 # Visualization modules (ECG, STFT, Polar plots)
│   └── save_img.py               # Polar image formatting and saving
└── main.py                       # CLI execution entry point
