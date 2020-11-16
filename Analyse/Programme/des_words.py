import json
import csv
import nltk
import re
#import nltk_songtexte as nl

#DDR_JSON = ""
#BRD_JSON = ""
DDR_STRING = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt"
BRD_STRING = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_string.txt"

#jsons = [DDR_JSON, BRD_JSON]
strings = [DDR_STRING, BRD_STRING]

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

def get_total_words(wort_liste):

    total_words = len(wort_liste)

    return total_words

def get_av_wordlength(wort_liste, total_words):
    
    word_length = 0
    for w in wort_liste:
        word_length += len(w)
    
    av_wordlength = word_length/total_words

    return av_wordlength

def get_type_token(string):
    
    token = nltk.tokenize.word_tokenize(string,language='german')
    for t in token[:]:
        if re.match(r'(\n)+\s*', t):
            token.remove(t)
        elif re.match(r'\'|\.\.\.|\.|´|!|\?|,|:|-|;', t):
            token.remove(t)
    
    tokenanzahl = len(token)
    typeanzahl = len(set(token))
    ratio = (typeanzahl/tokenanzahl)*100

    return tokenanzahl, typeanzahl, ratio


with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/deskriptive.csv', mode='w') as csv_file:
    fieldnames = ['Land', 'Total Words', 'Average Word Length', 'Token', 'Types', 'TTR']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    l = 0
    for s in strings:
        with open(s) as file:
            text = file.read()

        wort_liste = get_words(text)
        total_words = get_total_words(wort_liste)
        av_wordlength = get_av_wordlength(wort_liste, total_words)
        token, types, ratio = get_type_token(text)

        if "ddr_string" in s:
            land = "DDR"
        else:
            land = "BRD"

        row = {'Land': land, 'Total Words': total_words, 'Average Word Length': round(av_wordlength, 3), 'Token': token, 'Types': types, 'TTR': round(ratio, 3)}
        writer.writerow(row)