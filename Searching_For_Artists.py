import csv

def search(country):
    with open('C:\\Users\\kayla\\Desktop\\Visual Studios Code\\Pearl Hacks\\artists.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        local_artists = [country]

        for row in csv_reader:
            if row [0] == country:
                #print (row[1])
                local_artists.append(row[1])
        
        #print (local_artists)
        add_songs_to_playlist(local_artists)

