import subprocess
import platform

def check_disk_encryption():
    system = platform.system()

    try:
        if system == "Windows":
            result = subprocess.check_output("manage-bde -status C:", shell=True, text=True)
            return "Percentage Encrypted: 100%" in result
        
        elif system == "Linux":
            result = subprocess.check_output("lsblk -o NAME,TYPE,MOUNTPOINT", shell=True, text=True)
            return "/dev/mapper" in result or "crypt" in result.lower()

        elif system == "Darwin":  # macOS
            result = subprocess.check_output("fdesetup status", shell=True, text=True)
            return "FileVault is On" in result

    except Exception:
        return False
