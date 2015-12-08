# -*- coding: cp1253 -*-
import os

def rename_files():

    #(1) get filenames from a folder
    file_list  = os.listdir(r"C:\Users\ΓΙΩΡΓΟΣ\Desktop\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current path is " + saved_path)
    os.chdir("C:\Users\ΓΙΩΡΓΟΣ\Desktop\prank")
    new_path = os.getcwd()
    print("Current path is " + new_path)
    #(2) for each file,rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
