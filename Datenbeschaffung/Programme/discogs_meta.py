import discogs_key as dk
import requests
import json

DDR_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json'
BRD_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json'

paths = [DDR_PATH, BRD_PATH]

def get_meta(jahr, titel, artist):
    key = dk.consumer_key
    secret = dk.consumer_secret
    r = requests.get(f'https://api.discogs.com/database/search?release_title={titel}&artist={artist}&year={jahr}&key={key}&secret={secret}')
    #print(r.json())
    page = r.json()
    #print(page['results'])
    results = page['results']
    if not results:
        return 'Nothing'
    else:
        genre = results[0]['genre']
        style = results[0]['style']
        label = results[0]['label']
        country = results[0]['country']
        return (genre, style, label, country)

for p in paths:
    with open(p) as file:
        hit_json = json.load(file)

        for jahr in hit_json:
            for song in hit_json[jahr]:
                titel = song['titel']
                artist = song['interpret']
                data = get_meta(jahr, titel, artist)
                if data == "Nothing":
                    pass
                else:
                    genre, style, label, country = data[0], data[1], data[2], data[3]
                    song['label'] = label
                    song['genre'] = genre
                    song['style'] = style
                    song['land'] = country
    
    with open(p, 'w') as up_file:
        json.dump(hit_json, up_file, indent=4, ensure_ascii=False)

#/database/search?q={query}&{?type,title,release_title,credit,artist,anv,label,genre,style,country,year,format,catno,barcode,track,submitter,contributor}
