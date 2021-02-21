import csv
from spotipy_app import add_songs_to_playlist

def search(country):
    with open('C:\\Users\\briel\\OneDrive\\Documents\\GitHub\\Hackathons\\PearlHacks21\\artists.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        local_artists = [country]

        for row in csv_reader:
            if row [0] == country:
                #print (row[1])
                local_artists.append(row[1])
    for artist in local_artists:
        print (artist)
    link = add_songs_to_playlist(country, local_artists)
    return link

