
Here is demo video of overall functionality <br>
https://drive.google.com/file/d/1rrKtqXzGGlRc7VnmTsKzoqx0oBff3UCu/view?usp=sharing

# 🧠 System Health Dashboard

A simple, modern Flask-based web application that collects and displays system health reports in real-time using MongoDB for data storage and Tailwind CSS for a sleek frontend.

---

## 🚀 Features

- 📦 POST endpoint to receive system health reports
- 🧾 View latest report data on a web dashboard
- 🎨 Beautiful Tailwind CSS frontend
- 📅 Automatically stores timestamp for each report
- ☁️ Cloud MongoDB (MongoDB Atlas) integration

---


---

## 🛠 Technologies Used

- **Python 3**
- **Flask**
- **MongoDB Atlas**
- **Flask-PyMongo**
- **Tailwind CSS**

---

## 📡 API Endpoints

### `POST /api/report`

Saves system health data to the MongoDB database.

#### 🔸 Request JSON Example:
```json
{
  "machine_id": "ABC123",
  "os": "Windows 11",
  "hostname": "user-PC",
  "disk_encryption": "Enabled",
  "os_update": "Up to date",
  "antivirus": "Active",
  "sleep_ok": "Yes"
}

