mfw_ddr = {'Nacht': 320, 'Leben': 313, 'Tag': 276, 'Traum': 264, 'Liebe': 256, 'Zeit': 237, 'Welt': 212, 'Mann': 139, 'Lied': 127, 'Erde': 126, 'Haus': 124, 'Auge': 116, 'Wind': 115, 'Mensch': 112, 'Haut': 111, 'Jahr': 108, 'Hand': 105, 'Herz': 103, 'Wort': 98, 'Mädchen': 98}
mfw_brd = {'Liebe': 369, 'Nacht': 362, 'Traum': 248, 'Mann': 242, 'Leben': 230, 'Tag': 210, 'Welt': 209, 'Zeit': 203, 'Herz': 188, 'Hand': 143, 'Frau': 135, 'Haus': 129, 'Mädchen': 115, 'Kind': 114, 'Auge': 113, 'Lied': 111, 'Freund': 109, 'Sonne': 108, 'Jahr': 105, 'Wein': 105}

total_words = 189016
total_ddr = 85078
total_brd = 103938

other_words_brd = 0
other_words_ddr = 0

for w in mfw_ddr:
    obs_x_ddr = mfw_ddr[w]
    if w in mfw_brd:
        obs_x_brd = mfw_brd[w]
        total_x = obs_x_ddr + obs_x_brd 
        other_words_ddr = total_ddr - obs_x_ddr
        other_words_brd = total_brd - obs_x_brd
        total_others = other_words_brd + other_words_ddr

        exp_x_ddr = (total_ddr * total_x)/total_words
        exp_x_brd = (total_brd * total_x)/total_words

        exp_others_ddr = (total_ddr * total_others)/total_words
        exp_others_brd = (total_brd * total_others)/total_words

        chi_squared = (((obs_x_ddr - exp_x_ddr)**2)/exp_x_ddr) + (((obs_x_brd - exp_x_brd)**2)/exp_x_brd) + (((other_words_ddr - exp_others_ddr)**2)/exp_others_ddr) + (((other_words_brd - exp_others_brd)**2)/exp_others_brd)
        print("[SUCCESS]    Der chi-Quadrat-Wert von " + w + " ist:",chi_squared)
        p = 3.84
        if chi_squared > p:
            print("                 -> Die Frequenzunterschiede sind mit 95-prozentiger Sicherheit signifikant (also nicht zufällig).")
        else:
            print("                 -> Die Frequenzunterschiede sind mit 95-prozentiger Sicherheit NICHT signifikant.")
    else:
        print("[ERROR]      " + w + " kommt nicht in der Most-Frequent-Noun-Liste der BRD vor!")
