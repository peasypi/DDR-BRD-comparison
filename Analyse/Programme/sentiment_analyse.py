from textblob_de import TextBlobDE as TextBlob
from spacy_sentiws import spaCySentiWS
import spacy
import re
import nltk
from HanTa import HanoverTagger as ht
import hilfsprogramme.preprocessing as prep
nlp = spacy.load('de')
sentiws = spaCySentiWS(sentiws_path='/Users/pia/Desktop/Uni/SoSe2019/Drama Mining und Film Analyse/Projekt/figurennetzwerk/Senti Net 1.0/SentiWS_v2.0')
nlp.add_pipe(sentiws)

gleichhäufige_worte = ["Nacht", "Haus", "Auge", "Jahr", "Hand", "Mädchen"]

#a_list = ["perfekt", "toll", "Traum", "alt", "schön", "super", "schlimm", "schrecklich", "Ekel", "Traum", "Trauer", "Gesundheit", "albern"]

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt') as file:
        ddr_hits = file.read()

words = prep.get_words(ddr_hits)
lemmalist = prep.get_lemmalist(words)

wort = "Liebe"

indices = []

for i in range(len(lemmalist)):

   if lemmalist[i] == wort:
      indices.append(i)

print(indices)

# get range from aspect
for i in indices:
    print(i)
    beginn = i-3 
    if beginn < 0:
        beginn = 0
    end = i + 4
    
    aspect = " ".join(lemmalist[beginn:end])
    sentiment = 0
    counter = 0
    doc = nlp(aspect)
    for token in doc:
        if token._.sentiws is not None:
            print(token, token._.sentiws)
            counter += 1
            sentiment += token._.sentiws
    
    sentiment = sentiment/counter

    blob3 = TextBlob(aspect)

    print("TextBlob: ", blob3.sentiment)
    print("spaCy_SentiWS: ", sentiment)