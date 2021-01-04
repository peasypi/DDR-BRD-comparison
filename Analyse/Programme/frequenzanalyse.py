import hilfsprogramme.preprocessing as prep
import hilfsprogramme.frequenzlisten as freq
import hilfsprogramme.visualisierung as vis
import os
import json

DDR_STRING = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt"
BRD_STRING = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_string.txt"
DDR_DIR = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/txt_years/DDR"
BRD_DIR = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/txt_years/BRD"

strings = {DDR_STRING, BRD_STRING}
dirs = {DDR_DIR, BRD_DIR}

#Bei which 'nouns' angeben, falls nur nach most frequent nouns gesucht wird, ansonsten 'all'
def get_freqlists_years(path, which):
    #Jahr-für-Jahr-Analyse
    txt_year_list = os.listdir(path)
    mfw_dict = {}
    for txt in txt_year_list:
        print(txt)
        with open(path + "/" + txt) as file:
            hit_string = file.read()
        year = txt[4:-4]
        words = prep.get_words(hit_string)
        lemmalist = prep.get_lemmalist(words, which)
        lem_wostopwords = prep.delete_stopwords(lemmalist)
        #words_wostopwords = prep.delete_stopwords(words)
        mfw = freq.count_mfw(lem_wostopwords)
        #print(dict(mfw))
        #vis.create_wordcloud(mfw,land)
        #vis.create_barplot(mfw,land,year)
        #mfb = freq.get_bigrams(words_wostopwords)
        #vis.create_wordcloud(mfb,'brd')
        #vis.create_barplot(mfb,'brd',year)
        mfw_dict[year] = dict(mfw)
    return mfw_dict


def get_freqlists(string):
    freqdict = {} 
    words = prep.get_words(string)
    lemmalist = prep.get_lemmalist(words, 'all')
    lem_wostopwords = prep.delete_stopwords(lemmalist)
    #words_wostopwords = delete_stopwords(words)
    mfw = freq.count_mfw(lem_wostopwords)
    freqdict['all'] = dict(mfw)
    lemmalist = prep.get_lemmalist(words, 'nouns')
    lem_wostopwords = prep.delete_stopwords(lemmalist)
    #words_wostopwords = delete_stopwords(words)
    mfw = freq.count_mfw(lem_wostopwords)
    freqdict['nouns'] = dict(mfw)
    return freqdict


for s in strings:
    with open(s, 'r') as file:
        hit_string = file.read()
        if 'ddr_string' in s:
            freqdict = get_freqlists(hit_string)
            with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/DDR/ddr_mfw.json", "w") as js:
                    json.dump(freqdict, js, indent=4, ensure_ascii=False)
        else:
            freqdict = get_freqlists(hit_string)
            with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/BRD/brd_mfw.json", "w") as js:
                    json.dump(freqdict, js, indent=4, ensure_ascii=False)

for d in dirs:
    if "/BRD" in d:
        mfw_dict = get_freqlists_years(d, 'nouns')
        with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/years/BRD/brd_year_mfn.json", "w") as js:
            json.dump(mfw_dict, js, indent=4, ensure_ascii=False)
    else:
        mfw_dict = get_freqlists_years(d, 'nouns')
        with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/years/DDR/ddr_year_mfn.json", "w") as js:
            json.dump(mfw_dict, js, indent=4, ensure_ascii=False)
