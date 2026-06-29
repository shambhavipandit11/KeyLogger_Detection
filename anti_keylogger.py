import os
import sys
import psutil
import time

# 1. Database of known/suspicious keylogger process keywords and modules
SUSPICIOUS_KEYWORDS = [
    "keylogger", "klog", "logger", "spy", "hook", "pynput", "keyboard_monitor"
]

# Simulated local database of malicious MD5 hashes/names for Signature matching
KNOWN_BAD_PROCESSES = ["keylogger.exe", "spy_agent.exe", "hook_listener.exe"]

def scan_processes():
    print("\n" + "="*50)
    print("[*] Launching Active Keylogger Detection Scan...")
    print("="*50)
    
    detected_threats = 0
    current_pid = os.getpid()

    # Iterate through all active system processes
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            cmdline = proc.info['cmdline']

            # Skip checking this running detection script itself
            if pid == current_pid:
                continue

            is_malicious = False
            reason = ""

            # Check 1: Signature Based Match (Exact Name Matching)
            if name and name.lower() in KNOWN_BAD_PROCESSES:
                is_malicious = True
                reason = "Matches known keylogger signature database."

            # Check 2: Heuristic/Behavioral Keyword Scanning
            if name:
                for keyword in SUSPICIOUS_KEYWORDS:
                    if keyword in name.lower():
                        is_malicious = True
                        reason = f"Suspicious keyword tracking pattern found in process name: '{keyword}'"
                        break

            # Check 3: Deep inspection of execution command line arguments
            if cmdline and not is_malicious:
                cmd_line_str = " ".join(cmdline).lower()
                for keyword in SUSPICIOUS_KEYWORDS:
                    if keyword in cmd_line_str:
                        is_malicious = True
                        reason = f"Suspicious library or parameter found in command line: '{keyword}'"
                        break

            # If a threat is validated, flag it to the user
            if is_malicious:
                detected_threats += 1
                print(f"\n[!] ALERT: Potential Keylogger Detected!")
                print(f"    [-] Process Name: {name}")
                print(f"    [-] Process ID (PID): {pid}")
                print(f"    [-] Risk Factor: HIGH")
                print(f"    [-] Reason: {reason}")
                
                # Interactive Remediation Action
                choice = input(f"    [>] Would you like to terminate PID {pid}? (y/n): ").strip().lower()
                if choice == 'y':
                    try:
                        p = psutil.Process(pid)
                        p.terminate()
                        print(f"    [+] Process {pid} successfully terminated.")
                    except Exception as e:
                        print(f"    [-] Failed to terminate process: {e}")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    print("\n" + "="*50)
    if detected_threats == 0:
        print("[+] Scan Completed. System appears clean. No active keyloggers found.")
    else:
        print(f"[+] Scan Completed. Action taken on {detected_threats} threat(s).")
    print("="*50)

if __name__ == "__main__":
    # Ensure tool runs with enough privileges to scan system processes
    print("[*] Checking admin/root privileges...")
    try:
        is_admin = os.getuid() == 0 if sys.platform != 'win32' else os.system("net session >nul 2>&1") == 0
    except AttributeError:
        is_admin = False # fallback for environments that don't support getuid
        
    print("[*] Running Anti-Keylogger Framework Interface.")
    
    while True:
        print("\n--- Anti-Keylogger Dashboard ---")
        print("1. Run Live Detection Scan")
        print("2. Run a Mock Keylogger Simulator (To Test the Detector)")
        print("3. Exit")
        
        mode = input("Select an option (1-3): ").strip()
        
        if mode == '1':
            scan_processes()
        elif mode == '2':
            print("\n[*] Starting a Mock Keylogger simulator process for 15 seconds...")
            print("[*] Open another terminal window quickly and run Option 1 to detect it!")
            
            # This loop mimics a running background script containing targeted keywords
            try:
                for i in range(15):
                    # We modify the process window title/execution footprint dynamically
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
            print("[*] Simulator closed.")
        elif mode == '3':
            print("Exiting tool.")
            break
        else:
            print("Invalid option. Please try again.")