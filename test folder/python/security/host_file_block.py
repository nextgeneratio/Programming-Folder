import psutil
import os
import time

def is_editor_opening_hosts():
    hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    blocked_editors = ["notepad.exe", "notepad++.exe"]
    
    for process in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            if process.info['name'].lower() in blocked_editors:
                if process.info['open_files']:
                    for file in process.info['open_files']:
                        if file.path.lower() == hosts_path.lower():
                            print(f"Blocking {process.info['name']} from editing hosts file.")
                            os.system(f"taskkill /F /PID {process.info['pid']}")
                            return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

if __name__ == "__main__":
    while True:
        is_editor_opening_hosts()
        time.sleep(1)  # Check every second
