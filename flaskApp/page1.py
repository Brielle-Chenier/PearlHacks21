from flask import Flask, redirect, url_for, render_template

app = Flask (__name__)

@app.route("/<country>")
def home(country):
    return render_template("index.html", link = country)

@app.route("/")
def home1():
    return render_template("index.html", link = "")


if __name__ == "__main__":
    app.run(debug = True)