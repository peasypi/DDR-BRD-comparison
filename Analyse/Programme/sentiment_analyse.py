from textblob_de import TextBlobDE as TextBlob
from spacy_sentiws import spaCySentiWS
import spacy

nlp = spacy.load('de')
sentiws = spaCySentiWS(sentiws_path='/Users/pia/Desktop/Uni/SoSe2019/Drama Mining und Film Analyse/Projekt/figurennetzwerk/Senti Net 1.0/SentiWS_v2.0')
nlp.add_pipe(sentiws)

wort = "Traum"

a_list = ["perfekt", "toll", "Traum", "alt", "schön", "super", "schlimm", "schrecklich", "Ekel", "Traum", "Trauer", "Gesundheit", "albern"]


indices = []

for i in range(len(a_list)):

   if a_list[i] == wort:
      indices.append(i)

print(indices)

# get range from aspect
for i in indices:
    print(i)
    beginn = i-3 
    if beginn < 0:
        beginn = 0
    end = i + 4
    
    aspect = " ".join(a_list[beginn:end])
    sentiment = 0
    counter = 0
    doc = nlp(aspect)
    for token in doc:
        if token._.sentiws is not None:
            counter += 1
            sentiment += token._.sentiws
    
    sentiment = sentiment/counter

    blob3 = TextBlob(aspect)

    print("TextBlob: ", blob3.sentiment)
    print("spaCy_SentiWS: ", sentiment)