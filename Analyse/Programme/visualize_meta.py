import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker

with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/ddr_meta_analyse.json") as js:
    meta_data = json.load(js)

land = "ddr"
for kategorie in meta_data:
    anzahl = []
    label = []
    analyze_cat = {}
    sonst = 0
    for key in meta_data[kategorie]:
        if meta_data[kategorie][key] <= 10:
            sonst = sonst + meta_data[kategorie][key]
        else:
            anzahl.append(meta_data[kategorie][key])
            label.append(key)
    
    anzahl.append(sonst)
    label.append("Sonstige")
    
    x = np.array(anzahl)
    
    #locator = matplotlib.ticker.MultipleLocator(50)
    #plt.gca().xaxis.set_major_locator(locator)
    plt.figure(figsize=(15, 12), dpi=400)
    plt.title(f'{land.upper()}: {kategorie.capitalize()}')
    plt.pie(x, labels=label)
    #plt.show()
    plt.savefig(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{land.upper()}_pics/pie_{kategorie}_{land}.png')
