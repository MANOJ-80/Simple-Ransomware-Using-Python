# Simple Ransomware in Python

## What is Ransomware?

Ransomware is a type of malicious software (malware) that encrypts a user's files or locks them out of their system, rendering the data inaccessible until a ransom is paid. It typically spreads through phishing emails, malicious links, or software vulnerabilities. Once activated, ransomware will encrypt files and demand payment, often in cryptocurrency, to provide the decryption key.

## Purpose of This Project

This project, **Simple Ransomware in Python**, is designed for educational purposes only. It demonstrates how ransomware attacks function and the mechanisms behind file encryption and decryption. Understanding these concepts is crucial for cybersecurity awareness and defense strategies.

### Warning: 
**DO NOT use these scripts on any real or sensitive data.** This code is for educational purposes only and should only be run in a controlled environment, such as a virtual machine or a sandbox, where it cannot cause harm. Misuse of this code could result in data loss or legal consequences.

## Features

- **File Encryption**: Encrypts all files in the directory (except specified scripts) using symmetric encryption (Fernet).
- **Decryption**: Allows the user to decrypt files if the correct secret key is provided.
- **GUI Notifications**: Uses `tkinter` to display messages during encryption and decryption processes.

## Files Included

- `ransomware.py`: The main script that encrypts files.
- `Decrypt.py`: The script that decrypts the encrypted files.
- `ransom.txt`: A text file containing the encryption key.
  
## How It Works

1. **Encryption**:
   - The script scans the current directory for files to encrypt.
   - It generates a symmetric encryption key and saves it in `ransom.txt`.
   - Each file's contents are encrypted using the Fernet symmetric encryption algorithm.

2. **Decryption**:
   - The decryption script prompts the user for a secret key.
   - If the provided key matches the expected hash, it decrypts the files using the saved encryption key.

## Requirements

To run this project, you need the following:

- Python 3.x
- `cryptography` library (install via pip):
  ```bash
  pip install cryptography
