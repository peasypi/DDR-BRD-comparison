import json
# Mit dieser Funktion werden doppelte Lieder aus dem Datensatz gelöscht
with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json') as f:
    brd_hits = json.load(f)

song_titel = []

for jahr in brd_hits:
    for song in brd_hits[jahr][:]:
        if song['titel'] in song_titel:
            print(song['titel'])
            brd_hits[jahr].remove(song)
        else:
            song_titel.append(song['titel'])

print(song_titel)

with open('ddr_charts.json', 'w') as f:
    json.dump(brd_hits, f, ensure_ascii=False, indent=4)



