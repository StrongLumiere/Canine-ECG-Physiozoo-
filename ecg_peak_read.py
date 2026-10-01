import wfdb

def ecg_peak_read(patient_id):
    annotation = wfdb.rdann(patient_id, 'qrs')
    qrs_peaks = annotation.sample

    return qrs_peaks