import nltk
import spacy
import re
import json

DDR_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json'
BRD_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json'
with open(BRD_PATH) as file:
    ddr_hits = json.load(file)

for jahr in ddr_hits:
    for k in ddr_hits[jahr]:
        if "lyrics" in k:
            songtext = k["lyrics"]
            nlp = spacy.load('de')
            spacy_doc = nlp(songtext)

            token = [tok.text.lower() for tok in spacy_doc]

            #print(token)
            #print(len(token))
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

            #print(k)

with open(BRD_PATH, 'w') as file:
    json.dump(ddr_hits, file, indent=4, ensure_ascii=False)


#print(re.match(r'(\\n)+\s*|\W', token[126]))
# print(len([tok.text for tok in spacy_doc]))
