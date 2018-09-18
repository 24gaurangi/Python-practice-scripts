"""
Script to create folder in specified location and copy default files into it
If folder exists, create the default files
"""

import os, sys
import shutil

dest_folder_location=r"D:\Applications\Open"
default_file1="Gaurangi_Wanjari_Resume.docx"

folder_names_tobe_created=['Test_Folder']

for i in folder_names_tobe_created:
    new_folder=os.path.join(dest_folder_location,i)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    try:
        shutil.copyfile(os.path.join(dest_folder_location,default_file1),os.path.join(new_folder,"Test_File_1.docx"))
    except:
        e=sys.exc_info()[1]
        print("Error: ",e)


