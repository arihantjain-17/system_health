import platform
import subprocess

def check_sleep_timeout():
    system = platform.system()

    try:
        if system == "Windows":
            result = subprocess.check_output("powercfg /query SCHEME_CURRENT SUB_SLEEP STANDBYIDLE", shell=True, text=True)
            for line in result.splitlines():
                if "Power Setting Index" in line:
                    value = int(line.strip().split()[-1], 16)
                    return value <= 600

        elif system == "Linux":
            result = subprocess.getoutput("gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout")
            timeout = int(result.strip())
            return timeout <= 600

        elif system == "Darwin":
            result = subprocess.check_output("pmset -g | grep sleep", shell=True, text=True)
            for line in result.splitlines():
                if "sleep" in line:
                    timeout = int(line.split()[-1])
                    return timeout <= 10

    except:
        return False
