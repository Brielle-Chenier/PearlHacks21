import csv
from spotipy_app import add_songs_to_playlist

def search(country):
    with open('C:\\Users\\brie\\OneDrive\\Documents\\GitHub\\Hackathons\\PearlHacks21\\artists.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        local_artists = []

        for row in csv_reader:
            if row [0] == country:
                print (row[1])
                local_artists.append(row[1])

        print (local_artists)
        #add_songs_to_playlist(local_artists)


search("United Kingdom")