from flask import Flask, redirect, url_for, render_template
import csv
from spotipy_app import add_songs_to_playlist
import spotipy
from Searching_For_Artists import search

app = Flask (__name__)

@app.route("/<country>")
def home(country):
    link = search(country)
    return render_template("index.html", link = link)

@app.route("/")
def home1():
    return render_template("index.html", link = "")


if __name__ == "__main__":
    app.run(debug = True)