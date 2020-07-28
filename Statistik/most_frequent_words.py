from collections import Counter 
from spacy.lang.de.stop_words import STOP_WORDS
import spacy
import re
import json
from nltk.corpus import stopwords

stopset = stopwords.words('german')

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json') as file:
    ddr_hits = json.load(file)

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json') as file:
    brd_hits = json.load(file)


nlp = spacy.load('de')

for jahr in ddr_hits:
    mfw_ddr = []
    all_lyrics_ddr = ""
    for i in ddr_hits[jahr]:
        all_lyrics_ddr = all_lyrics_ddr + "\n\n" + i["lyrics"]

    #Löschen der Sonderzeichen
    all_lyrics_ddr = re.sub(r'\'|\.\.\.|\.|´|!|\?|,|:|\–|;|`|\"|\\', "", all_lyrics_ddr)

    spacy_doc = nlp(all_lyrics_ddr)

    token = [tok.lemma_.lower() for tok in spacy_doc]
    # Löschen der new lines
    for t in token:
        if re.match(r'(\n)+\s*', t):
            token.remove(t)
        
    token = [tok for tok in token if tok not in stopset]

    Counterv = Counter(token)
    most_occur = Counterv.most_common(4) 

    print(jahr + " waren die most frequent words:")
    print(most_occur)
    print("\n")