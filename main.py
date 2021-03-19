from werkzeug.security import generate_password_hash, check_password_hash
from flask.helpers import send_from_directory
from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth
import os

app = Flask(__name__, template_folder=".")
auth = HTTPBasicAuth()

DIRECTORIES = [
    "movies",
    "torrents"
]

USERS = {
    "username": generate_password_hash("password"),
}

CONTENT_PATH = "content"

HOST = "127.0.0.1"

PORT = 5000

@auth.verify_password
def verify_password(username, password):
    if username in USERS and check_password_hash(USERS.get(username), password):
        return username

@app.route("/")
@auth.login_required
def root():
    return render_template("index.html", folders=os.listdir(CONTENT_PATH))

@app.route("/<directory>/")
@auth.login_required
def get_directory(directory):
    try:
        return render_template("index.html", folders=os.listdir(f"{CONTENT_PATH}/{directory}"))
    except NotADirectoryError:
        return send_from_directory(directory=CONTENT_PATH, filename=directory, as_attachment=True)

@app.route("/<directory>/<file>")
@auth.login_required
def get_directory_file(directory, file):
    return send_from_directory(directory=os.path.join(CONTENT_PATH, directory), filename=file, as_attachment=True)

app.run(HOST, PORT)