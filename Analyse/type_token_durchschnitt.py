import json

DDR_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json'
BRD_PATH = '/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json'


with open(BRD_PATH) as file:
    brd_hits = json.load(file)
with open(DDR_PATH) as file:
    ddr_hits = json.load(file)

ddr = 0
anzahl_ddr = 0

brd = 0
anzahl_brd = 0

for jahr in ddr_hits:
    for l in ddr_hits[jahr]:
        if "type/token" in l:
            ddr += l["type/token"]
            anzahl_ddr += 1

ttddr = ddr/anzahl_ddr

for jahr in brd_hits:
    for k in brd_hits[jahr]:
        if "type/token" in k:
            brd += k["type/token"]
            anzahl_brd += 1

ttddr = ddr/anzahl_ddr
ttbrd = brd/anzahl_brd

print("Durchschnittliche Type-Token-Ratio der DDR: " + str(ttddr))
print("Durchschnittliche Type-Token-Ratio der BRD: " + str(ttbrd))        
