import nltk_songtexte as nl

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt') as f:
    ddr_string = f.read()

ddr_liste = nl.get_words(ddr_string)
#ddr_liste = nl.delete_stopwords(ddr_liste)

len_worte = 0
for w in ddr_liste[:]:
    if len(w) == 1:
        ddr_liste.remove(w)
    else:
        len_worte += len(w)

av_wordlength = len_worte/len(ddr_liste)
print("Total words der DDR-Songs: " + str(len(ddr_liste)))
print("Average word length der DDR-Songs ist: "+ str(av_wordlength))