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

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt') as file:
    ddr_hits = file.read()

def get_words(txtfile):
    #Löschen der Sonderzeichen
    txtfile = re.sub(r'\'|\.\.\.|\.|´|!|\?|,|:|–|;|`|\"|\\', "", txtfile)
    #Tokenisieren des großen Strings
    words = nltk.tokenize.word_tokenize(txtfile,language='german')
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
def create_wordcloud(mfw,land):
    wordcloud = WordCloud(max_words=20, background_color="white", colormap='GnBu').generate_from_frequencies(dict(mfw))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    plt.savefig('wordcloud_{}.png'.format(land))

def create_barplot(mfw,land):
    mfw.reverse()
    worte = ()
    counts = []
    for tup in mfw:
        worte = worte + (tup[0],)
        counts.append(tup[1])
    y_pos = np.arange(len(worte))
    plt.title('most frequent words')
    plt.ylabel('Worte')
    plt.xlabel("Häufigkeit")
    plt.barh(y_pos, counts, color='#81bbee')
    plt.yticks(y_pos, worte)
    plt.show()
    plt.savefig('barplot_mfw_{}.png'.format(land))


words = get_words(ddr_hits)
lemmalist = get_lemmalist(words)
lem_wostopwords = delete_stopwords(lemmalist)
mfw = count_mfw(lem_wostopwords)
print(mfw)
create_wordcloud(mfw,'ddr')
create_barplot(mfw,'ddr')

