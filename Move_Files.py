import os
import shutil

source_dir = "E:/Document_Files"
destination_dir = "E:/Python/PRO102"

list_of_files = os.listdir(source_dir)
extension_list = []

for files in list_of_files:
    name, extension = os.path.splitext(files)

    if(extension == ''):
        continue
    if extension in ['.pdf']:
        path1 = source_dir + '/' + files
        path2 = destination_dir + '/' + "Move_Files"
        path3 = destination_dir + '/' + "Move_Files" + '/' + files
        
        if os.path.exists(path2):
          print("Moving " + files + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + files + ".....")
          shutil.move(path1, path3)

# Project 102
