import matplotlib.pyplot as plt
import json
import numpy as np


with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/meta_data/brd_meta_analyse.json', 'r') as f:
    meta_dict = json.load(f)

#print(meta_dict)

#def create_meta_barplot(kat_dict):
kat_dict = meta_dict['interpreten']
sonstige = 0
names = []
freq = ()
durchschnitt = int(sum(kat_dict.values())/len(kat_dict))
#print(durchschnitt)
for key, value in kat_dict.items():
    if value > 5:
        names.append(key)
        freq = freq + (value,)
    else:
        sonstige += value
names.append('Sonstige')
freq = freq + (sonstige,)

#print(names)
#print(freq)

index = np.arange(len(names))
bar_width = 0.8
plt.bar(index, freq, bar_width,  color="green", zorder = 2)
plt.xticks(index, names, rotation='vertical') # labels get centered
plt.tight_layout()
#plt.savefig('interpreten_barplot.png')
plt.grid(b=None, which='both', axis='y', zorder = 0)
plt.show()
#for kategorie in meta_dict:
#    create_meta_barplot(meta_dict[kategorie])