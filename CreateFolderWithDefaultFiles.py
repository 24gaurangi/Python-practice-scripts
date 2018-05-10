"""
Script to create folder in specified location and copy default files into it
If folder exists, create the default files

"""

import os
import shutil

folder_location=r"D:\Applications\Open"
default_file1=r"D:\Applications\default_file1.docx"
default_file2=r"D:\Applications\default_file2.docx"
folder_names=['Test_Folder_1','Test_folder_3']

for i in folder_names:
    new_folder=os.path.join(folder_location,i)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    try:
        shutil.copyfile(default_file1,os.path.join(new_folder,"Test_File_1.txt"))
        shutil.copyfile(default_file2,os.path.join(new_folder,"Test_File_2.docx"))

    except:
        print(err)

