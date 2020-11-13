import discogs_key as dk
import requests
import json
import time

DDR_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json'
BRD_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json'

paths = [DDR_PATH, BRD_PATH]


def get_meta(jahr, titel, artist):
    key = dk.consumer_key
    secret = dk.consumer_secret
    song = titel + ' ' + artist
    r = requests.get(f'https://api.discogs.com/database/search?q={song}&key={key}&secret={secret}')
    # print(r.json())
    page = r.json()
    # print(page['results'])
    if 'results' in page:
        results = page['results']
        for re in results[:]:
            if 'year' not in re.keys():
                results.remove(re)
        results_sorted = sorted(results, key=lambda k: k['year'])
        for re in results_sorted:
            #print(re, "\n\n\n")
            if int(re['year']) <= 1990:
                #print(re, "\n")
                genre = re['genre']
                style = re['style']
                label = re['label']
                country = re['country']
                return (genre, style, label, country)

for p in paths:
    with open(p) as file:
        hit_json = json.load(file)
        nicht_gefunden = []

        for jahr in hit_json:
            for song in hit_json[jahr]:
                titel = song['titel']
                artist = song['interpret']
                data = get_meta(jahr, titel, artist)
                time.sleep(2)
                if data == None:
                    print(f'[ERROR]     Keine Metadaten zu {titel} von {artist} gefunden')
                    nicht_gefunden.append(titel)
                else:
                    genre, style, label, country = data[0], data[1], data[2], data[3]
                    song['label'] = label
                    song['genre'] = genre
                    song['style'] = style
                    song['land'] = country
                    print(f'[SUCCESS]   Metadaten zu {titel} von {artist} gefunden')

    with open(p, 'w') as up_file:
        json.dump(hit_json, up_file, indent=4, ensure_ascii=False)
    
    print(nicht_gefunden)
    print(len(nicht_gefunden))

