import discogs_key as dk
import requests
import json

DDR_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json'
BRD_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json'

paths = [DDR_PATH, BRD_PATH]


def get_meta(jahr, titel, artist):
    key = dk.consumer_key
    secret = dk.consumer_secret
    r = requests.get(f'https://api.discogs.com/database/search?track={titel}&artist={artist}&key={key}&secret={secret}')
    # print(r.json())
    page = r.json()
    # print(page['results'])
    results = page['results']
    if not results:
        return 'Nothing'
    else:
        for re in results:
            if int(re['year']) <= 1990:
                #print(re, "\n")
                genre = re['genre']
                style = re['style']
                label = re['label']
                country = re['country']
                break
            else:
                return 'Nothing'
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
                    print(f'[ERROR]     Keine Metadaten zu {titel} von {artist} gefunden')
                else:
                    genre, style, label, country = data[0], data[1], data[2], data[3]
                    song['label'] = label
                    song['genre'] = genre
                    song['style'] = style
                    song['land'] = country
                    print(f'[SUCCESS]   Metadaten zu {titel} von {artist} gefunden')

    with open(p, 'w') as up_file:
        json.dump(hit_json, up_file, indent=4, ensure_ascii=False)

# /database/search?q={query}&{?type,title,release_title,credit,artist,anv,label,genre,style,country,year,format,catno,barcode,track,submitter,contributor}
