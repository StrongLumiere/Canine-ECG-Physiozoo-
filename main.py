import os
import numpy as np
from src.path_setting import path_setting
from src.ecg_read import ecg_read
from src.ecg_peak_read import ecg_peak_read
from src.ecg_windowing import ecg_window
from src.Pan_tompkins import Pan_tompkins
from src.ecg_stft import ecg_stft
from src.polar_transform import spectrogram_polar_transform
from src.plot_ecg import plot_ecg, plot_ecgseg
from src.plot_spectrogram import plot_spectrogram
from src.plot_polar_ecg import plot_polar_ecg
from src.save_img import save

#=========================
# TASK HANDLE FUNCTIOS
#=========================

def run_ecg_plot(base_dir, list_dogs: list, PT):
    """Option 1: 특정 개체의 ECG 신호 Plot"""
    print("#############[What Number do you plot?]############") 
    n=int(input(">>>[1~17]") )  
    id = list_dogs[n - 1]

    id_path = base_dir + f"\\{id}\\{id}"    
    id_path= base_dir +f"\\{id}\\{id}"

    if PT: 
        ecg_signal, fs=ecg_read(id_path)
        ecg_signal=Pan_tompkins(ecg_signal, fs).fit()
    else:
       ecg_signal, fs=ecg_read(id_path)     
    plot_ecg(id=id, ecg_signal= ecg_signal, fs= fs)

def run_stft_plot(base_dir, list_dogs: list, PT):
    """Option 2: 전체 개체 STFT Spectrogram Plot"""
    for id in list_dogs:
        id_path= base_dir +f"\\{id}\\{id}"
        if PT: 
            ecg_signal, fs=ecg_read(id_path)
            ecg_signal=Pan_tompkins(ecg_signal, fs).fit()
        else:
            ecg_signal, fs=ecg_read(id_path)   

        frequencies, times, stft = ecg_stft(ecg_signal=ecg_signal, fs=fs)
        plot_spectrogram(id=id, stft=stft, times=times, frequencies=frequencies)

def run_polar_plot(base_dir, list_dogs: list, PT):
    """Option 3: 전체 개체 Polar Spectrogram Plot"""
    # loop for each id's
    for id in list_dogs:
                print(f'[{id}]')
                id_path= base_dir +f"\\{id}\\{id}" 
                if PT: 
                    ecg_signal, fs=ecg_read(id_path)
                    ecg_signal=Pan_tompkins(ecg_signal, fs).fit()
                else:
                    ecg_signal, fs=ecg_read(id_path)   
    
                # ecg stft
                _, _, stft=ecg_stft(ecg_signal=ecg_signal,fs=fs)
    
                print('...stft done')
    
                # kspace- reversed
                raw_k, x1, y1=spectrogram_polar_transform(stft, grid_resolution = 512, flipped_up = True, method = 'linear')
                plot_polar_ecg(id=id, k=raw_k,x=x1,y=y1, reversed= True)
                print('...polar done')

def run_save_images(base_dir, list_dogs: list, PT):
    """Option 4: Windowing 및 Polar ECG 이미지 일괄 저장"""
    # save path setting
    save_path= "C:\\Users\\user\\Desktop\\new_ecg_project\\img"
    os.makedirs(save_path, exist_ok=True)

    for id in list_dogs:
        print(f'[{id}]')
        id_path= base_dir +f"\\{id}\\{id}" 

        if PT: 
                    ecg_signal, fs=ecg_read(id_path)
                    ecg_signal=Pan_tompkins(ecg_signal, fs).fit()
        else:
            ecg_signal, fs=ecg_read(id_path)

        # windowing
        df_ecg_segments=ecg_window(id, ecg_signal=ecg_signal, fs=fs)
        
        #segments for 1 ecg 
        for i, (_, row) in enumerate(df_ecg_segments.iterrows(), start=1):
            segment = np.load(row["file"])
            print(f"...{id}segment[{i}]")
            # plot_ecgseg(id,segment,fs,i)

            # ecg stft
            _, _, stft=ecg_stft(ecg_signal=segment, fs=fs)
            print('...stft done')

            # kspace- reversed
            raw_k, x1, y1=spectrogram_polar_transform(
                stft, 
                grid_resolution = 512, 
                flipped_up = True, 
                method = 'linear')

            save(grid_d=raw_k, 
                grid_x=x1, 
                grid_y=y1, 
                save_path=save_path, 
                id=id,
                seg_num= i, 
                image_size=(224,224))
                # image_size=(96,96))  
            print(f'...save{id}-segment{i} complete') 

def run_segment_plot(base_dir, list_dogs: list, PT):
    """Option 5: 첫 번째 개체의 ECG Segment Plot"""
    print("#############[What Number do you plot?]############") 
    n=int(input(">>>[1~17]") )  
    id = list_dogs[n - 1]

    id = list_dogs[n - 1]
    
    id_path = base_dir + f"\\{id}\\{id}"    
    id_path= base_dir +f"\\{id}\\{id}"

    if PT: 
        ecg_signal, fs=ecg_read(id_path)
        ecg_signal=Pan_tompkins(ecg_signal, fs).fit()
    else:
        ecg_signal, fs=ecg_read(id_path) 

        ecg_segments=ecg_window(id, ecg_signal=ecg_signal, fs=fs)

    # segments for 1 ecg 
    for i, segment in enumerate(ecg_segments, start=1):

        plot_ecgseg(
            id=id,
            ecg_segment=segment,
            fs=fs,
            num_seg = i
        )    

def main():

    print("#############[What to do?]############")
    print("1. ECG plot\n"
          "2. STFT plot\n"
          "3. Polar plot\n"
          "4. Save Image\n"
          "5. Segments for 1 ECG"
          )
    
        
    print("#####################################")
    i=input(">>>")

    # path setting, set your directory path which your physiozoo data directories are saved.
    base_dir, list_dogs=path_setting()

    # Pan&Tompkins preprocessing
    print("#############[Do use PT?]############")
    PT=bool(input(">>>[y:1/n:0]"))

    # make ecg plot image
    if int(i)==1:
        run_ecg_plot(base_dir=base_dir, list_dogs=list_dogs, PT=PT)
    # make ecg spectrogram image
    elif int(i)==2:
        run_stft_plot(base_dir=base_dir, list_dogs=list_dogs, PT=PT)
    # make polar spectrogram image
    elif int(i)==3:
        run_polar_plot(base_dir=base_dir, list_dogs=list_dogs, PT=PT)
         
    # save all polar ecg image
    elif int(i)==4:
        run_polar_plot(base_dir=base_dir, list_dogs=list_dogs, PT=PT)
    # make ecg segments plot for 1 id
    if int(i)==5:
        run_segment_plot(base_dir=base_dir, list_dogs=list_dogs, PT=PT)
            
    else:
        print(-1)    


    return 


if __name__ == "__main__":
    main()