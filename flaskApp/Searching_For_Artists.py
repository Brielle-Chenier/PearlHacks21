import csv
from spotipy_app import add_songs_to_playlist

def search(country):
    with open('.\\artists.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        local_artists = []

        for row in csv_reader:
            if country in str(row [0]):
                new_row = str(row[0]).split(',')
                local_artists.append(str(new_row[1]))

        for artist in local_artists:
            print (artist)
        if (len(local_artists)==0):
            local_artists = [country]
    link = add_songs_to_playlist(country, local_artists)
    return link

