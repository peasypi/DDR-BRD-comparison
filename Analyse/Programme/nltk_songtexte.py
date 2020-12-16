import preprocessing as prep
import frequenzlisten as freq
import visualisierung as vis
import os


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
        words = prep.get_words(ddr_hits)
        lemmalist = prep.get_lemmalist(words, year)
        lem_wostopwords = prep.delete_stopwords(lemmalist)
        words_wostopwords = prep.delete_stopwords(words)
        mfw = freq.count_mfw(lem_wostopwords)
        #create_wordcloud(mfw,'brd')
        vis.create_barplot(mfw,'brd',year)
        mfb = freq.get_bigrams(words_wostopwords)
        #create_wordcloud(mfb,'brd')
        vis.create_barplot(mfb,'brd',year)

#main_nltk()
