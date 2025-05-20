import platform
import subprocess
import wmi

def check_antivirus_status():
    system = platform.system()

    try:
        if system == "Windows":
            c = wmi.WMI(namespace="root\\SecurityCenter2")
            products = c.AntiVirusProduct()
            active = any(p.productState in [397568, 266240] for p in products)
            return {"present": bool(products), "active": active}

        elif system == "Linux":
            result = subprocess.run("pgrep -f clamd", shell=True, capture_output=True)
            return {"present": result.returncode == 0, "active": result.returncode == 0}

        elif system == "Darwin":
            result = subprocess.run("pgrep -f antivirus", shell=True, capture_output=True)
            return {"present": result.returncode == 0, "active": result.returncode == 0}

    except:
        return {"present": False, "active": False}
