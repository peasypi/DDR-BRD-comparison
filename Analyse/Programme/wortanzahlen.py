import nltk_songtexte as nl

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_string.txt') as f:
    brd_string = f.read()

brd_liste = nl.get_words(brd_string)
#ddr_liste = nl.delete_stopwords(ddr_liste)

len_worte = 0
for w in brd_liste[:]:
    if len(w) == 1:
        brd_liste.remove(w)
    else:
        len_worte += len(w)

av_wordlength = len_worte/len(brd_liste)
print("Total words der BRD-Songs: " + str(len(brd_liste)))
print("Average word length der BRD-Songs ist: "+ str(av_wordlength))