from textblob_de import TextBlobDE as TextBlob
from spacy_sentiws import spaCySentiWS
import spacy
import re
import nltk
from HanTa import HanoverTagger as ht

nlp = spacy.load('de')
sentiws = spaCySentiWS(sentiws_path='/Users/pia/Desktop/Uni/SoSe2019/Drama Mining und Film Analyse/Projekt/figurennetzwerk/Senti Net 1.0/SentiWS_v2.0')
nlp.add_pipe(sentiws)

gleichhäufige_worte = ["Nacht", "Haus", "Auge", "Jahr", "Hand", "Mädchen"]

#a_list = ["perfekt", "toll", "Traum", "alt", "schön", "super", "schlimm", "schrecklich", "Ekel", "Traum", "Trauer", "Gesundheit", "albern"]
def get_words(txtfile):
    #Löschen der Sonderzeichen
    txtfile = re.sub(r'\'|\.\.\.|\.|´|\!|\?|,|:|–|;|`|\"|\\|\)|\(|_', "", txtfile)
    #Tokenisieren des großen Strings
    words = nltk.tokenize.word_tokenize(txtfile,language='german')
    for w in words[:]:
        if len(w) == 1:
            words.remove(w)
        else:
            match = re.search(r'\w+', w)
            if match:
                pass
            else:
                words.remove(w)
    return words

def get_lemmalist(worte):
    #Laden des HanoverTaggers
    tagger = ht.HanoverTagger('morphmodel_ger.pgz')
    #Worte in words lemmatisieren und taggen
    tags = []
    for wort in worte:
        tag = tagger.analyze(wort,taglevel=1)
        tags.append(tag)
    #Aus den tag-Tupeln nur Worte in eine Liste speichern
    lemma_list = []
    for tup in tags:
        #Hinzufügen der lemmatisierten Worte zur lemma_list
        #lemma_list.append(tup[0])
        #Alternativ: Hinzufügen der lemmatisierten Nomen zur lemma_list
        if tup[1] == 'NN':
            lemma_list.append(tup[0])

    for w in lemma_list[:]:
        if len(w) == 1:
            lemma_list.remove(w)
        else:
            match = re.search(r'\w+', w)
            if match:
                pass
            else:
                lemma_list.remove(w)
    return lemma_list

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt') as file:
        ddr_hits = file.read()

words = get_words(ddr_hits)
lemmalist = get_lemmalist(words)

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