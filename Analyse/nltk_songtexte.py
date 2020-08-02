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
import matplotlib.ticker

#with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt') as file:
#    ddr_hits = file.read()

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/ddr_try_string.txt') as file:
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
def create_wordcloud(mostfrequent,land):
    wordcloud = WordCloud(max_words=20, background_color="white", colormap='Set2').generate_from_frequencies(dict(mostfrequent))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    #plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/{}_pics/wordcloud_{}.png'.format(land.upper(),land))    
    plt.show()

def create_barplot(mostfrequent,land):
    mostfrequent.reverse()
    worte = ()
    counts = []
    for tup in mostfrequent:
        worte = worte + (tup[0],)
        counts.append(tup[1])
    y_pos = np.arange(len(worte), dtype=int)
    locator = matplotlib.ticker.MultipleLocator(2)
    plt.gca().xaxis.set_major_locator(locator)
    if len(mostfrequent[0][0].split(' ')) == 1:
        plt.title('most frequent words')
        plt.ylabel('Worte')
        plt.xlabel("Häufigkeit")
        plt.barh(y_pos, counts, color='#81bbee')
        plt.yticks(y_pos, worte)
        #plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/{}_pics/barplot_mfw_{}.png'.format(land.upper(),land))
        plt.show()
    else:
        plt.title('most frequent bigrams')
        plt.ylabel('Bi-Gramme')
        plt.xlabel("Häufigkeit")
        plt.barh(y_pos, counts, color='#81bbee')
        plt.yticks(y_pos, worte)
        #plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/{}_pics/barplot_mfb_{}.png'.format(land.upper(),land))
        plt.show()

def get_bigrams(worte):
    liste = list(nltk.bigrams(words))
    bigrms = []
    for i in liste:
        bigrms.append(' '.join(i).lower())
    counts = Counter(bigrms)
    most_bigrams = counts.most_common(20)
    return most_bigrams



words = get_words(ddr_hits)
print(words)
lemmalist = get_lemmalist(words)
print(lemmalist)
lem_wostopwords = delete_stopwords(lemmalist)
print(lem_wostopwords)
mfw = count_mfw(lem_wostopwords)
print(mfw)
create_wordcloud(mfw,'ddr')
create_barplot(mfw,'ddr')
mfb = get_bigrams(lem_wostopwords)
print(mfb)
create_wordcloud(mfb,'ddr')
create_barplot(mfb,'ddr')

