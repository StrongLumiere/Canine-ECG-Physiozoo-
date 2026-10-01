import os
import wfdb

def ecg_read(patient_id):
    # 'data' 디렉토리와 patient_id를 연결하여 상대 경로 생성
    file_path = os.path.join("data", patient_id)
    
    # 수정된 경로를 사용하여 레코드 읽기
    record = wfdb.rdrecord(file_path) 
    ecg_signal = record.p_signal[:,0]  
    fs = record.fs
    
    return ecg_signal, fs

