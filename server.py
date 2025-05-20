
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb+srv://arihantjaindec2003:shbUnyLn9OEfVP7U@cluster0.d1lfxiz.mongodb.net/ddd"
mongo = PyMongo(app)

@app.route("/")
def dashboard():
    # Fetch latest record
    data = mongo.db.reports.find_one(sort=[("timestamp", -1)])
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
