# KeyLogger Detection System

A lightweight, fully functional cybersecurity utility designed to detect and counter unauthorized keystroke logging activities on Windows operating systems. This project employs a dual-layer approach combining signature matching and heuristic behavioral process monitoring to identify potential threats and provide real-time incident remediation.

## 🚀 Features

* **Real-time Process Auditing:** Enumerates and monitors active system tasks utilizing kernel-level mapping definitions.
* **Signature-Based Inspection:** Cross-references active application states against a known definitions dictionary of malicious processes.
* **Heuristic Analysis:** Intercepts command-line execution parameters to flag suspicious low-level hook inputs (e.g., `pynput`, `keyboard`).
* **Active Threat Remediation:** Provides an automated control interface allowing administrators to forcefully terminate a verified threat dynamically.
* **Built-in Threat Simulator:** Includes a secure environment tool to safely test the active detection parameters without exposing the host to actual malware.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **Core Libraries:** `psutil`, `os`, `sys`, `time`
* **Compilation Environment:** PyInstaller (for cross-platform standalone executable production)

---

## 💻 How to Run & Test

### Option 1: Running the Source Code (.py)

1. Clone or download this repository.
2. Install the necessary system auditing extension:
   ```bash
   pip install psutil
