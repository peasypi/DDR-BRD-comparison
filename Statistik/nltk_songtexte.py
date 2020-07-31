import nltk
import json
import re
from HanTa import HanoverTagger as ht
from collections import Counter 
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json') as file:
    ddr_hits = json.load(file)

def get_words(jsonfile):
    all_lyrics = ""
    #großen String mit allen Liedtexten der DDR erstellen
    for jahr in jsonfile:
        for i in jsonfile[jahr]:
            all_lyrics = all_lyrics + "\n\n" + i["lyrics"]
    #Löschen der Sonderzeichen
    all_lyrics = re.sub(r'\'|\.\.\.|\.|´|!|\?|,|:|–|;|`|\"|\\', "", all_lyrics)
    #Tokenisieren des großen Strings
    words = nltk.tokenize.word_tokenize(all_lyrics,language='german')
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
    word_list = []
    for tup in tags:
        word_list.append(tup[0])
    for w in word_list[:]:
        if len(w) == 1:
            word_list.remove(w)
        else:
            match = re.search('\W+', w)
            if match:
                word_list.remove(w)
    return word_list

#Stopworte entfernen und neue Liste erstellen
def delete_stopwords(wortliste):
    stopset = stopwords.words('german')
    tokens_without_sw = [w for w in wortliste if not w.lower() in stopset]
    return tokens_without_sw


#Counter zählt die most frequent words in der Liste ohne Stopwörter
def count_mfw(tokenliste):        
    Zaehler = Counter(tokenliste)
    most_occur = Zaehler.most_common(20)
    return most_occur

#Liste wieder zu String -- damit Wordcloud erstellen
def create_wordcloud(tokenliste):
    text = " ".join(tokenliste)
    wordcloud = WordCloud(max_words=20, background_color="white", colormap='gnuplot2').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

words = get_words(ddr_hits)
lemmalist = get_lemmalist(words)
lem_wostopwords = delete_stopwords(lemmalist)
print(lem_wostopwords)
mfw = count_mfw(lem_wostopwords)
print(mfw)
create_wordcloud(lem_wostopwords)


