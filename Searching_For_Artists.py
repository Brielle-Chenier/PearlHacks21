import csv
from spotipy_app import add_songs_to_playlist

def search(country):
    with open('C:\\Users\\briel\\OneDrive\\Documents\\GitHub\\Hackathons\\PearlHacks21\\artists.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        local_artists = []

        for row in csv_reader:
            if country in str(row [0]):
                new_row = str(row[0]).split(',')
                local_artists.append(str(new_row[1]))

        for artist in local_artists:
            print (artist)
        #add_songs_to_playlist(local_artists)


search("United Kingdom")