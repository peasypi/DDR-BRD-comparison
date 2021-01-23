import hilfsprogramme.preprocessing as prep


DDR_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt"
BRD_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_string.txt"

paths = [DDR_PATH, BRD_PATH]

def count_Fliegen(hit_string):
    #Preprocessing
    worte = prep.get_words(hit_string)
    lemmalist = prep.get_lemmalist(worte, "all")
    worte_wo_stopwords = prep.delete_stopwords(lemmalist)

    #zu überprüfende Worte
    fliegen_liste = ["Vogel", "fliegen", "Flug"]

    #Zähler für die Worte 
    counter = 0
    for wort in fliegen_liste:
        for w in worte_wo_stopwords:
            if wort == w:
                counter += 1

    return counter

def chi_squared(ddr_freq, brd_freq):
    total_words = 187776
    total_ddr = 84485
    total_brd = 103291
    obs_x_ddr = ddr_freq
    obs_x_brd = brd_freq
    #Beobachtete Häufigkeit des Wortes X in beiden Korpora
    total_x = obs_x_ddr + obs_x_brd 
    #Beobachtete Anzahl aller Wörter außer X in DDR-Korpus
    other_words_ddr = total_ddr - obs_x_ddr
    #Beobachtete Anzahl aller Wörter außer X in BRD-Korpus
    other_words_brd = total_brd - obs_x_brd
    #Anzahl aller Wörter außer X in beiden Korpora
    total_others = other_words_brd + other_words_ddr

    #Erwartete Häufigkeit des Wortes X in DDR-Korpus
    exp_x_ddr = (total_ddr * total_x)/total_words
    #Erwartete Häufigkeit des Wortes X in BRD-Korpus
    exp_x_brd = (total_brd * total_x)/total_words

    #Erwartete Anzahl aller Wörter außer X in DDR-Korpus
    exp_others_ddr = (total_ddr * total_others)/total_words
    #Erwartete Anzahl aller Wörter außer X in BRD-Korpus
    exp_others_brd = (total_brd * total_others)/total_words

    #Chi-Quadratwert des Wortes X
    chi_squared = round((((obs_x_ddr - exp_x_ddr)**2)/exp_x_ddr) + (((obs_x_brd - exp_x_brd)**2)/exp_x_brd) + (((other_words_ddr - exp_others_ddr)**2)/exp_others_ddr) + (((other_words_brd - exp_others_brd)**2)/exp_others_brd), 3)

    return chi_squared


for p in paths:
    with open(p, 'r') as f:
        hit_string = f.read()
    if "ddr_string" in p:
        ddr_freq = count_Fliegen(hit_string)
        print(f'Das Motiv Fliegen kommt im DDR-Korpus {ddr_freq}-Mal vor.')
    else:
        brd_freq = count_Fliegen(hit_string)
        print(f'Das Motiv Fliegen kommt im BRD-Korpus {brd_freq}-Mal vor.')
    chi = chi_squared(ddr_freq, brd_freq)
    if chi > 3.84:
        sig = "signifikant"
    else:
        sig = "nicht signifikant"
    print(f'Der Chi-Quadrat-Wert ist {chi}. Die Frequenzunterschiede des Motives Fliegen sind damit {sig}.')

