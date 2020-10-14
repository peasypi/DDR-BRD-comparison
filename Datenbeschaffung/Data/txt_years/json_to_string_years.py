import json

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json') as file:
    ddr_hits = json.load(file)

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json') as file:
    brd_hits = json.load(file)


#großen String mit allen Liedtexten der DDR erstellen
for jahr in ddr_hits:
    lyrics_ddr = ""
    for i in ddr_hits[jahr]:
        lyrics_ddr = lyrics_ddr + "\n\n\n\n" + i["lyrics"]
    ddr_string = open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/txt_years/DDR/ddr_{}.txt'.format(jahr), 'w')
    for line in lyrics_ddr:
        ddr_string.write(line)
    ddr_string.close()

#großen String mit allen Liedtexten der DDR erstellen
for jahr in brd_hits:
    lyrics_brd = ""
    for k in brd_hits[jahr]:
        lyrics_brd = lyrics_brd + "\n\n\n\n" + k["lyrics"]
    brd_string = open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/txt_years/BRD/brd_{}.txt'.format(jahr), 'w')
    for line in lyrics_brd:
        brd_string.write(line)
    brd_string.close()

    