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
import os

#with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/ddr_try_string.txt') as file:
#    ddr_hits = file.read()

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

#Stopworte entfernen und neue Liste erstellen
def delete_stopwords(wortliste):
    stopset = stopwords.words('german')
    tokens_without_sw = [w for w in wortliste if not w.lower() in stopset]
    return tokens_without_sw

#Counter zählt die most frequent words in der Liste ohne Stopwörter
def count_mfw(tokenliste):        
    Zaehler = Counter(tokenliste)
    most_occur = Zaehler.most_common(20)
    print(most_occur)
    return most_occur

#Most frequent Bigramme
def get_bigrams(worte):
    liste = list(nltk.bigrams(worte))
    bigrms = []
    for i in liste:
        bigrms.append(' '.join(i).lower())
    counts = Counter(bigrms)
    most_bigrams = counts.most_common(20)
    for b in most_bigrams[:]:
        if b[0] == '-- --':
            most_bigrams.remove(b)
    return most_bigrams

#Liste wieder zu String -- damit Wordcloud erstellen
def create_wordcloud(mostfrequent,land):
    wordcloud = WordCloud(max_words=20, background_color="white", colormap='Set2').generate_from_frequencies(dict(mostfrequent))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    if len(mostfrequent[0][0].split(' ')) == 1:
        plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{}_pics/wordcloud_{}.png'.format(land.upper(),land))
    else:
        plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{}_pics/wordcloud_bigrams_{}.png'.format(land.upper(),land))
    plt.show()

#Balkendiagramm erstellen 
def create_barplot(mostfrequent,land,year):
    mostfrequent.reverse()
    worte = ()
    counts = []
    for tup in mostfrequent:
        worte = worte + (tup[0],)
        counts.append(tup[1])
    y_pos = np.arange(len(worte))
    if len(mostfrequent[0][0].split(' ')) == 1:
        locator = matplotlib.ticker.MultipleLocator(50)
        plt.gca().xaxis.set_major_locator(locator)
        plt.figure(figsize=(18, 12), dpi=400)
        #Titel für Komplett
        #plt.title('{}: most frequent words'.format(land.upper()))
        #Titel für Jahre
        plt.title('{}: {}: most frequent words'.format(land.upper(),year))
        plt.ylabel('Worte')
        plt.xlabel("Häufigkeit")
        plt.barh(y_pos, counts, color='#81bbee')
        plt.yticks(y_pos, worte)
        #Save All
        plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{}_pics/barplot_mfw_{}.png'.format(land.upper(),land))
        #Save year by year
        plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{}_pics/years/mfn/mfw_{}_{}.png'.format(land.upper(),land,year))
        #plt.show()
    else:
        locator = matplotlib.ticker.MultipleLocator(20)
        plt.gca().xaxis.set_major_locator(locator)
        plt.figure(figsize=(18, 12), dpi=400)
        #Titel für Komplett
        #plt.title('{}: most frequent bigrams'.format(land.upper()))
        #Titel für Jahre
        plt.title('{}: {}: most frequent bigrams'.format(land.upper(), year))        
        plt.ylabel('Bi-Gramme')
        plt.xlabel("Häufigkeit")
        plt.barh(y_pos, counts, color='#81bbee')
        plt.yticks(y_pos, worte)
        #Save All
        plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{}_pics/barplot_mfb_{}.png'.format(land.upper(),land))
        #Save year by year
        plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{}_pics/years/mfb/mfb_{}_{}.png'.format(land.upper(),land,year))
        #plt.show()


def main_nltk():
    #All-Lyrics-Analyse
    '''with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_string.txt') as file:
        ddr_hits = file.read()
    words = get_words(ddr_hits)
    lemmalist = get_lemmalist(words)
    lem_wostopwords = delete_stopwords(lemmalist)
    words_wostopwords = delete_stopwords(words)
    mfw = count_mfw(lem_wostopwords)
    #create_wordcloud(mfw,'brd')
    create_barplot(mfw,'brd')
    mfb = get_bigrams(words_wostopwords)
    #create_wordcloud(mfb,'brd')
    create_barplot(mfb,'brd')'''

    #Jahr-für-Jahr-Analyse
    PATH ="/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/txt_years/BRD"
    txt_year_list = os.listdir(PATH)
    for txt in txt_year_list:
        with open(PATH + "/" + txt) as file:
            ddr_hits = file.read()
        year = txt[4:-4]
        words = get_words(ddr_hits)
        lemmalist = get_lemmalist(words)
        lem_wostopwords = delete_stopwords(lemmalist)
        words_wostopwords = delete_stopwords(words)
        mfw = count_mfw(lem_wostopwords)
        #create_wordcloud(mfw,'brd')
        create_barplot(mfw,'brd',year)
        mfb = get_bigrams(words_wostopwords)
        #create_wordcloud(mfb,'brd')
        create_barplot(mfb,'brd',year)

main_nltk()
