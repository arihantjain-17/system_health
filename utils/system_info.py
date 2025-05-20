import platform
import uuid

def get_machine_info():
    return {
        "machine_id": str(uuid.getnode()),
        "os": platform.system(),
        "hostname": platform.node()
    }
