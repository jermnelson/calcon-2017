__author__ = "Jeremy Nelson"

from flask import render_template, request
from app import app, pages

@app.route("/about")
def about():
    return render_template("calcon-2017/about.html",
        pages=pages)

@app.route("/join")
def join():
    return render_template("calcon-2017/join.html")

@app.route("/")
def home():
    return render_template("calcon-2017/index.html")


