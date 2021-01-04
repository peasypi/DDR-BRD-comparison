import nltk
import json
import re
from HanTa import HanoverTagger as ht
from nltk.corpus import stopwords

# Erstellt Wort-Liste
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

#Erstellt Liste mit lemmatisierten Worten
#which gibt an ob alle Worte untersucht werden sollen oder nur die Nomen ('nouns')
def get_lemmalist(worte, which):
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
        if which == "all":
            lemma_list.append(tup[0])
        elif which == "nouns":
            #Alternativ: Hinzufügen der lemmatisierten Nomen zur lemma_list
            if tup[1] == 'NN':
                lemma_list.append(tup[0])
    
    for w in lemma_list[:]:
        #Herauslöschen aller Worte, die nur aus einem Buchstaben bestehen
        if len(w) == 1:
            lemma_list.remove(w)
        #Herauslöschen aller "Worte", die nicht aus Buchstaben bestehen (Sonderzeichen)
        else:
            match = re.search(r'\w+', w)
            if match:
                pass
            else:
                lemma_list.remove(w)
    return lemma_list

#Stopworte entfernen und neue Liste erstellen
def delete_stopwords(wortliste):
    #Lädt Stopwortliste von NLTK ein
    stopset = stopwords.words('german')
    tokens_without_sw = [w for w in wortliste if not w.lower() in stopset]
    return tokens_without_sw


