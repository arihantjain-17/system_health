import platform
import subprocess
import wmi  # Only used for Windows

def check_os_update():
    system = platform.system()

    try:
        if system == "Windows":
            w = wmi.WMI()
            updates = w.Win32_QuickFixEngineering()
            if updates:
                latest = max(update.InstalledOn for update in updates if update.InstalledOn)
                return {"up_to_date": True, "last_installed": latest}
            return {"up_to_date": False, "last_installed": None}

        elif system == "Linux":
            result = subprocess.check_output("apt list --upgradable 2>/dev/null", shell=True, text=True)
            return {"up_to_date": len(result.strip().splitlines()) <= 1, "details": result.strip()}

        elif system == "Darwin":
            result = subprocess.check_output("softwareupdate -l", shell=True, text=True)
            return {"up_to_date": "No new software available" in result, "details": result.strip()}

    except Exception:
        return {"up_to_date": False, "details": "Error"}
