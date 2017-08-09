__author__ = "Jeremy Nelson"

from flask import render_template, request
from app import app

@app.route("/background")
def background():
    return render_template("calcon-2017/content.html",
        title="Background on Project")
        

@app.route("/")
def home():
    return render_template("calcon-2017/index.html")


