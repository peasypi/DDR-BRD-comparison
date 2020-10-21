import json

with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json") as f:
    ddr_json = json.load(f)

interpreten = {}

for jahr in ddr_json:
    for song in ddr_json[jahr]:
        if song["interpret"] in interpreten.keys():
            interpreten[song["interpret"]] = interpreten[song["interpret"]]+1
        else:
            interpreten[song["interpret"]] = 1

interpreten = {k: v for k, v in sorted(interpreten.items(), key=lambda item: item[1], reverse=True)}
print(interpreten)
print(len(interpreten))

with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/brd_interpreten.json", 'w') as js:
    json.dump(interpreten, js, indent=4, ensure_ascii=False) 