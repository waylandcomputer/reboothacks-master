from flask import Flask, render_template, send_from_directory
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def newpage():
    return render_template("test.html")
