import json
from visualisierung import create_metadata_piechart as create_piechart

DDR_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/ddr_meta_analyse.json"
BRD_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/brd_meta_analyse.json"

paths = {DDR_PATH, BRD_PATH}

#Erstellt Piechart-PNGs für jede einzelne Kategorie der Meta-Daten
def visualize_meta(meta_data, land):
    for kategorie in meta_data:
        create_piechart(land, kategorie, meta_data)

for p in paths: 
    if "ddr_meta" in p:
        land = "ddr"
        with open(p) as js:
            meta_data = json.load(js)
        visualize_meta(meta_data, land)
    else:
        land = "brd"
        with open(p) as js:
            meta_data = json.load(js)
        visualize_meta(meta_data, land)