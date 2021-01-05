import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib.ticker
import os

#Liste wieder zu String -- damit Wordcloud erstellen
def create_wordcloud(mostfrequent,land):
    wordcloud = WordCloud(max_words=20, background_color="white", colormap='Set2').generate_from_frequencies(dict(mostfrequent))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    #Falls es einzelne Worte sind
    if len(mostfrequent[0][0].split(' ')) == 1:
        plt.savefig(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{land.upper()}_pics/wordcloud_{land}.png')
    #Falls es Bi-Gramme sind
    else:
        plt.savefig(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{land.upper()}_pics/wordcloud_bigrams_{land}.png')
    #plt.show()


#Balkendiagramm erstellen 
def create_barplot(mostfrequent, land, year):
    mostfrequent.reverse()
    worte = ()
    counts = []
    for tup in mostfrequent:
        worte = worte + (tup[0],)
        counts.append(tup[1])
    y_pos = np.arange(len(worte))
    #Falls es nur einzelne Worte sind
    if len(mostfrequent[0][0].split(' ')) == 1:
        locator = matplotlib.ticker.MultipleLocator(50)
        plt.gca().xaxis.set_major_locator(locator)
        plt.figure(figsize=(18, 12), dpi=400)
        if year == "all":
            #Titel für Komplett
            plt.title('{}: most frequent words'.format(land.upper()))        
            plt.ylabel('Worte')
            plt.xlabel("Häufigkeit")
            plt.barh(y_pos, counts, color='#81bbee')
            plt.yticks(y_pos, worte)
            #Save All
            plt.savefig(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{land.upper()}_pics/barplot_mfw_{land}.png')
        else:
            #Titel für Jahre
            plt.title('{}: {}: most frequent words'.format(land.upper(),year))
            plt.ylabel('Worte')
            plt.xlabel("Häufigkeit")
            plt.barh(y_pos, counts, color='#81bbee')
            plt.yticks(y_pos, worte)
            #Save year by year
            plt.savefig(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{land.upper()}_pics/years/mfn/mfw_{land}_{year}.png')
            #plt.show()
    #Falls es Bigramme sind
    else:
        locator = matplotlib.ticker.MultipleLocator(20)
        plt.gca().xaxis.set_major_locator(locator)
        plt.figure(figsize=(18, 12), dpi=400)
        if year == "all":
            #Titel für Komplett
            plt.title('{}: most frequent bigrams'.format(land.upper()))
            plt.ylabel('Bi-Gramme')
            plt.xlabel("Häufigkeit")
            plt.barh(y_pos, counts, color='#81bbee')
            plt.yticks(y_pos, worte)
            #Save All
            plt.savefig(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{land.upper()}_pics/barplot_mfb_{land}.png')
        else:
            #Titel für Jahre
            plt.title(f'{land.upper()}: {year}: most frequent bigrams')        
            plt.ylabel('Bi-Gramme')
            plt.xlabel("Häufigkeit")
            plt.barh(y_pos, counts, color='#81bbee')
            plt.yticks(y_pos, worte)
            #Save year by year
            plt.savefig(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{land.upper()}_pics/years/mfb/mfb_{land}_{year}.png')
        #plt.show()
    

def create_metadata_piechart(land, kategorie, meta_dict):
    anzahl = []
    label = []
    #analyze_cat = {}
    sonst = 0
    durchschnitt = int(sum(meta_dict[kategorie].values())/len(meta_dict[kategorie]))
    for key in meta_dict[kategorie]:
        if meta_dict[kategorie][key] <= durchschnitt:
            sonst = sonst + meta_dict[kategorie][key]
        else:
            anzahl.append(meta_dict[kategorie][key])
            label.append(key)
    
    anzahl.append(sonst)
    label.append("Sonstige")
    
    x = np.array(anzahl)
    
    plt.figure(figsize=(15, 12), dpi=400)
    plt.title(f'{land.upper()}: {kategorie.capitalize()}')
    plt.pie(x, labels=label)
    #plt.show()
    plt.savefig(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/meta_data//{land.upper()}/pie_{kategorie}_{land}.png')
