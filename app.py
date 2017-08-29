__author__ = "Jeremy Nelson"

from flask import Flask
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config["FLATPAGES_EXTENSION"] = ".md"
pages = FlatPages(app)
