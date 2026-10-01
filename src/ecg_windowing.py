import numpy as np
import pandas as pd
import os

def ecg_window(id, ecg_signal, fs, window_sec=30, overlap=0.5):
    
    # window와 stride 계산
    window_samples = int(window_sec * fs)
    stride_samples = int(window_samples * (1 - overlap))
    
    segments = []

    for start in range(0, len(ecg_signal) - window_samples + 1, stride_samples):

        save_path = "C:\\Users\\user\\Desktop\\new_ecg_project\\data\\seg" 
        os.makedirs(save_path, exist_ok=True)
        save_seg_path = save_path + f"\\ecg_seg"
        os.makedirs(save_seg_path, exist_ok=True)

        end = start + window_samples


        # ECG 30초 segment
        segment = ecg_signal[start:end]

        # # ECG signal 저장
        file_name = f"{id}_segment_{len(segments) + 1}.npy"
        file_path = os.path.join(save_seg_path, file_name)
        np.save(file_path, segment)

        # metadata만 저장
        segments.append({
            "patient_id": id,
            "segment": len(segments) + 1,
            "start_sec": start / fs,
            "end_sec": end / fs,
            "fs": fs,
            "n_samples": len(segment),
            "file": file_path
        })
        
        df=pd.DataFrame(segments)
        # print(df)
        df.to_csv(save_path + f"\\ecg_segments{id}.csv", index=False)

    return df
