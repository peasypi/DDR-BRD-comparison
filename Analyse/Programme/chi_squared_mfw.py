import csv

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/chi_squared_neu.csv', mode='w') as csv_file:
    fieldnames = ['Wort', 'DDR', 'BRD', 'chi squared', 'Frequenzunterschiede mit 95%', 'Frequenzunterschiede mit 99.9%']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    #Daten
    mfw_ddr = {'Nacht': 320, 'Leben': 313, 'Tag': 276, 'Traum': 264, 'Liebe': 256, 'Zeit': 237, 'Welt': 212, 'Mann': 139, 'Lied': 127, 'Erde': 126, 'Haus': 124, 'Auge': 116, 'Wind': 115, 'Mensch': 112, 'Haut': 111, 'Jahr': 108, 'Hand': 105, 'Herz': 103, 'Wort': 98, 'Mädchen': 98}
    mfw_brd = {'Liebe': 369, 'Nacht': 362, 'Traum': 248, 'Mann': 242, 'Leben': 230, 'Tag': 210, 'Welt': 209, 'Zeit': 203, 'Herz': 188, 'Hand': 143, 'Frau': 135, 'Haus': 129, 'Mädchen': 115, 'Kind': 114, 'Auge': 113, 'Lied': 111, 'Freund': 109, 'Sonne': 108, 'Jahr': 105, 'Wein': 105, 'Mensch': 92, 'Wort': 90, 'Wind': 84, 'Erde': 63, 'Haut': 40}

    #Anzahl aller Worte beider Korpora
    total_words = 187770
    #Anzahl aller Worte in einzelnen Korpora
    total_ddr = 84485
    total_brd = 103285

    other_words_brd = 0
    other_words_ddr = 0

    #Für jedes Wort in mfw-Liste
    for w in mfw_ddr:
        #Beobachtete Häufigkeit des Wortes X in DDR-Korpus
        obs_x_ddr = mfw_ddr[w]
        if w in mfw_brd:
            #Beobachtete Häufigkeit des Wortes X in BRD-Korpus
            obs_x_brd = mfw_brd[w]
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

            #kritischer Wert für 95%ige Sicherheit der Frequenzunterschiede
            p = 3.84
            #kritischer Wert für 99.999% Sicherheit der Frequenzunterschiede
            q = 10.83
            #Wenn X^2 größer als p, dann
            if chi_squared > p:
                #ist 
                sig = "signifikant"
            else:
                sig = "nicht signifikant"

            if chi_squared > q:
                freq = "signifikant"
            else:
                freq = "nicht signifikant"

            row = {'Wort': w, 'DDR': obs_x_ddr, 'BRD': obs_x_brd, 'chi squared': chi_squared, 'Frequenzunterschiede mit 95%': sig, "Frequenzunterschiede mit 99.9%": freq }
            writer.writerow(row)

            '''print("[SUCCESS]    Der chi-Quadrat-Wert von " + w + " ist:",chi_squared)
            if chi_squared > p:
                print("                 -> Die Frequenzunterschiede sind mit 95-prozentiger Sicherheit signifikant (also nicht zufällig).")
            else:
                print("                 -> Die Frequenzunterschiede sind mit 95-prozentiger Sicherheit NICHT signifikant.")
        else:
            print("[ERROR]      " + w + " kommt nicht in der Most-Frequent-Noun-Liste der BRD vor!")'''


