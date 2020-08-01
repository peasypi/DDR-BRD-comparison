import json

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json') as file:
    ddr_hits = json.load(file)

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json') as file:
    brd_hits = json.load(file)


all_lyrics_ddr = ""
#großen String mit allen Liedtexten der DDR erstellen
for jahr in ddr_hits:
    for i in ddr_hits[jahr]:
        all_lyrics_ddr = all_lyrics_ddr + "\n\n\n\n" + i["lyrics"]

all_lyrics_brd = ""
#großen String mit allen Liedtexten der DDR erstellen
for jahr in brd_hits:
    for k in brd_hits[jahr]:
        all_lyrics_brd = all_lyrics_brd + "\n\n\n\n" + k["lyrics"]
    
ddr_string = open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_string.txt', 'w')

brd_string = open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_string.txt', 'w')

for line in all_lyrics_ddr:
    ddr_string.write(line)
ddr_string.close()

for line in all_lyrics_brd:
    brd_string.write(line)
brd_string.close()

