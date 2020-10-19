import json

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json') as a:
    ddr_hits = json.load(a)

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts1.json') as b:
    hits = json.load(b)


for jahr in ddr_hits:
    for k in ddr_hits[jahr]:
        for j in hits:
            for i in hits[j]:
                if 'lyrics' not in i:
                    i["lyrics"] = k["lyrics"]



with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts1.json', 'w') as file:
    json.dump(hits, file, indent=4, ensure_ascii=False)