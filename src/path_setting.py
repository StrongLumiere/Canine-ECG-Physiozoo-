import os
from pathlib import Path

def path_setting(): 

   # PATH Setting
    path = os.getcwd()
    os.chdir(path+ "\\data\\Dog")
    base_dir= os.getcwd()
    print("### Setting Complete ###")
    print(base_dir)

    if os.path.exists(base_dir):
        # os.listdir로 전체 항목을 불러온 뒤, os.path.isdir로 폴더인지 검사
        subfolders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
        print("하위 폴더 목록:", subfolders)

    else:
        print(f"{base_dir} 경로를 찾을 수 없습니다.")

    return base_dir, subfolders # list of whole dogs

