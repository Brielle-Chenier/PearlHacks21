from flask import Flask, redirect, url_for, render_template
import csv
from spotipy_app import add_songs_to_playlist
import spotipy
from Searching_For_Artists import search

app = Flask (__name__)
country_list = ['Canada', 'Romania', 'Australia','South Korea','Brazil', 'New Zealand', 'Finland', 'Turkey', 'India', 'Germany']
country_list2 = ['Indonesia','Costa Rica', 'Panama','Ecuador', 'Norway','France','Japan','Croatia','Switzerland','Columbia']
country_list3 = ['Dominican Republic', 'Mexico','Italy','Latvia','United Kingdom','Iceland','Honduras','El Salvador','Chile']
country_list4 = ['Nicaragua', 'Argentina','Ecuador','Bolivia','Uruaguay','Andorra','Guatemala','Austria','Jordan','Belgium']
@app.route("/<country>")
def home(country):
    link = search(country)
    return redirect(link)

@app.route("/")
def home1():
    return render_template("index.html", base_url = "http://127.0.0.1:5000/", list1 = country_list, list2 = country_list2, list3 = country_list3, list4 = country_list4)


if __name__ == "__main__":
    app.run(debug = True)