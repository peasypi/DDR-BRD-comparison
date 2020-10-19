import json
# Mit dieser Funktion werden doppelte Lieder aus dem Datensatz gelöscht
with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json') as f:
    brd_hits = json.load(f)

# Erstellt leere Liste für Songtitel
song_titel = []

# Geht Songtitel durch ..
for jahr in brd_hits:
    for song in brd_hits[jahr][:]:
        # ..falls Song schon in Songtitel Liste - entferne das komplette dict aus Json-Datei
        if song['titel'] in song_titel:
            print(song['titel'])
            brd_hits[jahr].remove(song)
        # .. falls nicht, füge den Song zur Liste hinzu
        else:
            song_titel.append(song['titel'])

#print(song_titel)
with open('ddr_charts.json', 'w') as f:
    json.dump(brd_hits, f, ensure_ascii=False, indent=4)



