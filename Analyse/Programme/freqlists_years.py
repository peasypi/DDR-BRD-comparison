import preprocessing as prep
import frequenzlisten as freq
import visualisierung as vis
import os
import json

DDR_DIR = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/txt_years/DDR"
BRD_DIR = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/txt_years/BRD"

#Bei which 'nouns' angeben, falls nur nach most frequent nouns gesucht wird, ansonsten 'all'
def analyze_years(path, land, which):
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
        print(dict(mfw))
        #vis.create_wordcloud(mfw,land)
        #vis.create_barplot(mfw,land,year)
        #mfb = freq.get_bigrams(words_wostopwords)
        #vis.create_wordcloud(mfb,'brd')
        #vis.create_barplot(mfb,'brd',year)
        mfw_dict[year] = dict(mfw)
    return mfw_dict

dirs = {DDR_DIR, BRD_DIR}
for d in dirs:
    if "/BRD" in d:
        mfw_dict = analyze_years(d, 'brd', 'nouns')
        with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/years/BRD/brd_mfn.json", "w") as js:
            json.dump(mfw_dict, js, indent=4, ensure_ascii=False)
    else:
        mfw_dict = analyze_years(d, 'ddr', 'nouns')
        with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/years/DDR/ddr_mfn.json", "w") as js:
            json.dump(mfw_dict, js, indent=4, ensure_ascii=False)


