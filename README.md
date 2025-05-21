
Here is demo video of overall functionality <br>
https://drive.google.com/file/d/1rrKtqXzGGlRc7VnmTsKzoqx0oBff3UCu/view?usp=sharing

# 🧠 System Health Dashboard

A Python-based background system health monitoring tool that periodically collects system configuration and health data (like disk encryption status, OS updates, antivirus, and sleep settings) and uploads it to a MongoDB Atlas database. Ideal for auditing and centralized system monitoring.

## 📦 Features

- ✅ Disk encryption check
- 🛡️ Antivirus status check
- 🕒 OS update status
- 💤 Sleep timeout settings
- 🧠 Collects device hardware info
- ☁️ Pushes data to MongoDB Atlas only when changes are detected
- 🔁 Runs every 30 minutes as a background daemon
- 📄 Saves state locally in `state.json` to detect config changes

---

## ⚙️ Project Structure
```
system_health/
├── checks/
│ ├── antivirus.py
│ ├── disk_encryption.py
│ ├── os_update.py
│ └── sleep_settings.py
├── utils/
│ └── system_info.py
├── daemon/
│ └── watcher.py
├── main.py
├── requirements.txt
└── README.md
```

> ✅ When compiled, `state.json` is automatically created in the same directory as the `watcher.exe`.

---

## ⚙️ Prerequisites

- Python 3.8+
- pip
- MongoDB Atlas URI or local MongoDB server

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/arihantjain-17/system_health.git
cd system_health
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
pip install pymongo schedule
```
### 3.Configure MongoDB
Open daemon/watcher.py and update this line with your MongoDB connection string:
```
MONGO_URI = "your_mongodb_uri"
```

▶️ Run the Program
```
python main.py
```
This will:
 - Run initial health checks
- Insert data to MongoDB if new or changed
- Store local state in state.json
- Schedule next run in 30 minutes

###🛠️ Build Executable (.exe) for windows

1. Install PyInstaller
```bash
pip install pyinstaller
```
2 Create the Executable
```bash
pyinstaller --onefile main.py --name watcher
```
3.  Navigate to the dist/ folder and run the executable
```bash
./watcher.exe
```
###🐞 Common Issue
###If you see this error:
```
TypeError: Object of type ObjectId is not JSON serializable
```
###✅ Fix: After inserting the document into MongoDB, remove _id before saving to state.json:
```
current.pop("_id", None)
```
👤 Author
Arihant Jain
GitHub: @arihantjain2003
