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

### Encryption Process:
1. The script scans the current directory for files to encrypt.
2. It generates a symmetric encryption key using the `Fernet` encryption algorithm from the `cryptography` library.
3. The encryption key is stored in the `ransom.txt` file.
4. All files except the script files (`ransomware.py`, `Decrypt.py`, and `ransom.txt`) are encrypted.
5. The contents of the selected files are replaced with their encrypted versions.
6. A message is printed to the console, and a GUI notification warns the user that their files have been encrypted.

### Decryption Process:
1. The `Decrypt.py` script prompts the user to input a secret phrase.
2. The phrase is hashed using `SHA-256` and compared to a predefined secret hash.
3. If the phrase is correct, the script retrieves the encryption key from the `ransom.txt` file.
4. The encrypted files are decrypted and restored to their original state.
5. A success message is printed, and the user is notified via a GUI popup.
6. If the secret phrase is incorrect, the decryption fails, and a warning message is displayed.

## Code Example

## Requirements

To run this project, you need the following:

- Python 3.x
- `cryptography` library (install via pip):
  ```bash
  pip install cryptography
  ```
