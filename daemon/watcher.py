

import json
import os
import schedule
import time
import signal
import sys
import copy
from datetime import datetime
from pymongo import MongoClient

from checks.disk_encryption import check_disk_encryption
from checks.os_update import check_os_update
from checks.antivirus import check_antivirus_status
from checks.sleep_settings import check_sleep_timeout
from utils.system_info import get_machine_info

# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://arihantjaindec2003:shbUnyLn9OEfVP7U@cluster0.d1lfxiz.mongodb.net/ddd"
client = MongoClient(MONGO_URI)
db = client.ddd  # Database
collection = db.system_health_reports  # Collection

# Path to store state.json where .exe is run from
BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
STATE_FILE = os.path.join(BASE_DIR, "state.json")

# Global flag for daemon control
running = True

def load_state():
    if not os.path.exists(STATE_FILE) or os.stat(STATE_FILE).st_size == 0:
        return {}
    with open(STATE_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_state(data):
    def default_serializer(obj):
        return str(obj)  # fallback for ObjectId or datetime, etc.

    with open(STATE_FILE, "w") as f:
        json.dump(data, f, default=default_serializer)

def collect_data():
    data = get_machine_info()
    data.update({
        "disk_encryption": check_disk_encryption(),
        "os_update": check_os_update(),
        "antivirus": check_antivirus_status(),
        "sleep_ok": check_sleep_timeout(),
        "timestamp": datetime.utcnow().isoformat()
    })
    return data

def has_changed(current, previous):
    return json.dumps(current, sort_keys=True) != json.dumps(previous, sort_keys=True)



def run_check():
    print("Running system checks...")
    previous = load_state()
    current = collect_data()

    if has_changed(current, previous):
        print("Changes detected. Inserting into MongoDB...")
        try:
            mongo_data = copy.deepcopy(current)  # Avoid in-place mutation by MongoDB
            collection.insert_one(mongo_data)
            print("Data inserted successfully.")
        except Exception as e:
            print(f"MongoDB insert failed: {e}")
        
        save_state(current)  # current has no _id
    else:
        print("No changes detected.")

def signal_handler(sig, frame):
    global running
    print("\nReceived stop signal. Shutting down gracefully...")
    running = False

def start_daemon():
    global running

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    schedule.every(30).minutes.do(run_check)
    run_check()  # Run once immediately

    while running:
        schedule.run_pending()
        time.sleep(1)

    print("Daemon stopped.")

if __name__ == "__main__":
    start_daemon()
