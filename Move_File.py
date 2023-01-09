import os
import shutil
from_dir = 'C:/Users/ASUS/Downloads'
to_dir = 'C:/Users/ASUS/Desktop/Document_Files'
list_of_files = os.listdir(from_dir)
for file in list_of_files:
    root, ext = os.path.splitext(file)
    if ext in ['.exe','.pdf','.zip']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + 'exe_files'
        path3 = to_dir + '/' + 'exe_files' + '/' + file
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)