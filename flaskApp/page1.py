from flask import Flask, redirect, url_for, render_template
import csv
from spotipy_app import add_songs_to_playlist
import spotipy
from Searching_For_Artists import search

app = Flask (__name__)
country_list = ['Canada', 'Romania', 'Australia','South Korea','Brazil', 'New Zealand', 'Finland', 'Turkey', 'India', 'Germany']
country_list2 = ['Indonesia','Costa Rica', 'Panama','Ecuador', 'Chile','France','Japan','Croatia','Switzerland','Columbia']
country_list3 = ['Dominican Republic', 'Mexico','Italy','Latvia','United Kingdom','Iceland','Honduras','El Salvador','Belgium']
country_list4 = ['Nicaragua', 'Argentina','Norway','Bolivia','Uruaguay','Andorra','Guatemala','Austria','Jordan','Paraguay']
country_list5 = ['Uzbekistan', 'Bulgaria', 'Estonia', 'Hungary', 'Ireland', 'Cyprus', 'Taiwan', 'Morocco', 'Israel', 'Sweden']
country_list6 = ['Slovakia', 'Peru', 'Netherlands', 'Poland','Czech Republic','Greece','Tunisia', 'Portugal', 'South Africa']
country_list7 = ['Russia', 'Philippines','Vietnam', 'Egypt','Thailand', 'United States']
@app.route("/<country>")
def home(country):
    link = search(country)
    return redirect(link)

@app.route("/")
def home1():
    return render_template("index.html", base_url = "http://127.0.0.1:5000/", list1 = country_list, list2 = country_list2, list3 = country_list3, list4 = country_list4, list5 = country_list5, list6 = country_list6, list7= country_list7)


if __name__ == "__main__":
    app.run(debug = True)