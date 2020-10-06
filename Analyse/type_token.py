import nltk
import spacy
import re
import json

DDR_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json'
BRD_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json'
paths = [DDR_PATH, BRD_PATH]

def get_type_token(hit_json):
    for jahr in hit_json:
        for k in hit_json[jahr]:
    #Tokenisieren der Lyrics mit spacy
            if "lyrics" in k:
                songtext = k["lyrics"]
                nlp = spacy.load('de')
                spacy_doc = nlp(songtext)

                token = [tok.text.lower() for tok in spacy_doc]
    # Löschen der new lines
                for t in token[:]:
                    if re.match(r'(\n)+\s*', t):
                        token.remove(t)
    # Löschen der Sonderzeichen
                for t in token[:]:
                    if re.match(r'\'|\.\.\.|\.|´|!|\?|,|:|-|;', t):
                        token.remove(t)

                types = set(token) 
                ratio = len(types)/len(token)*100

                k["tokenanzahl"] = len(token)
                k["typeanzahl"] = len(types)
                k["type/token"] = round(ratio, 2)

    return hit_json

def average_ttr(hit_json):
    ttr = 0
    anzahl_songs = 0

    for jahr in hit_json:
        for l in hit_json[jahr]:
            if "type/token" in l:
                ttr += l["type/token"]
                anzahl_songs += 1

    average_ratio = ttr/anzahl_songs

    return average_ratio    

for p in paths:
    with open(p) as file:
        hit_json = json.load(file)
    updated_json = get_type_token(hit_json)
    with open(p, 'w') as file:
        json.dump(updated_json, file, indent=4, ensure_ascii=False)
    with open(p) as j:
        hit_json = json.load(j)
    average_ratio = average_ttr(hit_json)
    print(p + "\nDurchschnittliche Type-Token-Ratio: ", average_ratio)
    




