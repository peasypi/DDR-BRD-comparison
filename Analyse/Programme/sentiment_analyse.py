from textblob_de import TextBlobDE as TextBlob
from spacy_sentiws import spaCySentiWS
import spacy
import re
import nltk
import csv
from HanTa import HanoverTagger as ht
import hilfsprogramme.preprocessing as prep

nlp = spacy.load('de')
sentiws = spaCySentiWS(sentiws_path='/Users/pia/Desktop/Uni/SoSe2019/Drama Mining und Film Analyse/Projekt/figurennetzwerk/Senti Net 1.0/SentiWS_v2.0')
nlp.add_pipe(sentiws)


DDR_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt'
BRD_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_string.txt'
paths = [DDR_PATH, BRD_PATH]    

def sentiment_analyse(hits):
    words = prep.get_words(hits)
    lemmalist = prep.get_lemmalist(words, "all")

    #wort = "Nacht"

    senti_dict = {}

    for wort in gleichhäufige_worte:
        indices = []
        """for i in range(len(lemmalist)):

        if lemmalist[i] == wort:
            indices.append(i)

        #print(indices)"""
        indices = [i for i, x in enumerate(lemmalist) if x == wort]
        senti_list = []

        # get range from aspect
        for i in indices:
            #print(i)
            beginn = i-5 
            if beginn < 0:
                beginn = 0
            end = i + 6

            aspect = " ".join(lemmalist[beginn:end]).lower()
            #print(aspect)
            sentiment = 0
            counter = 0
            doc = nlp(aspect)
            for token in doc:
                if token._.sentiws is not None:
                    #print(token, token._.sentiws)
                    counter += 1
                    sentiment += token._.sentiws

            if counter != 0:
                sentiment = sentiment/counter

            senti_list.append(sentiment)

            blob3 = TextBlob(aspect)

            #print("TextBlob: ", blob3.sentiment)
            #print("spaCy_SentiWS: ", sentiment)
        print(f"Durchschnittlicher Sentimentwert von {wort} ist: {sum(senti_list)/len(senti_list)}")
        senti_dict[wort] = sum(senti_list)/len(senti_list)

    return senti_dict

gleichhäufige_worte = ["Nacht", "Haus", "Auge", "Jahr", "Hand", "Mädchen"]

for p in paths:
    with open(p, 'r') as file:
            hits = file.read()
    if "ddr_string" in p:
        ddr_senti_dict = sentiment_analyse(hits)
    else:
        brd_senti_dict = sentiment_analyse(hits)


with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/sentiments.csv', mode='w') as csv_file:
    fieldnames = ['Wort', 'DDR', 'BRD']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for wort in gleichhäufige_worte:
        row = {'Wort': wort, 'DDR': round(ddr_senti_dict[wort],5), 'BRD': round(brd_senti_dict[wort],5)}
        writer.writerow(row)


"""
BRD:
Durchschnittlicher Sentimentwert von Nacht ist: -0.014133472222222242
Durchschnittlicher Sentimentwert von Haus ist: -0.0042341085271317865
Durchschnittlicher Sentimentwert von Auge ist: 0.008602252252252245
Durchschnittlicher Sentimentwert von Jahr ist: 0.006361587301587304
Durchschnittlicher Sentimentwert von Hand ist: -0.014208101851851847
Durchschnittlicher Sentimentwert von Mädchen ist: -0.018249275362318847
{'Nacht': -0.014133472222222242, 'Haus': -0.0042341085271317865, 'Auge': 0.008602252252252245, 'Jahr': 0.006361587301587304, 'Hand': -0.014208101851851847, 'Mädchen': -0.018249275362318847}

DDR:
Durchschnittlicher Sentimentwert von Nacht ist: 0.006143906250000002
Durchschnittlicher Sentimentwert von Haus ist: -0.018427688172043013
Durchschnittlicher Sentimentwert von Auge ist: -0.003410344827586203
Durchschnittlicher Sentimentwert von Jahr ist: 0.037930709876543206
Durchschnittlicher Sentimentwert von Hand ist: 0.0030696825396825385
Durchschnittlicher Sentimentwert von Mädchen ist: 0.0022840136054421744
{'Nacht': 0.006143906250000002, 'Haus': -0.018427688172043013, 'Auge': -0.003410344827586203, 'Jahr': 0.037930709876543206, 'Hand': 0.0030696825396825385, 'Mädchen': 0.0022840136054421744}
"""