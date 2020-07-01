from os import listdir
from os.path import isfile, join
import json

hit_json = {}

for jahr in range(1975,1991):
    jahr = str(jahr)
    hit_json[jahr] = []
    filenames = [f for f in listdir('/Users/pia/Desktop/Uni/Bachelor-Arbeit/BRD_Charts_75-90/{}'.format(jahr)) if isfile(join('/Users/pia/Desktop/Uni/Bachelor-Arbeit/BRD_Charts_75-90/{}'.format(jahr), f))]

    for name in filenames:
        artit = name.split('_-_')
        artist = artit[0].replace('_',' ')
        titel = artit[1][:-4].replace('_',' ')
        path_end = jahr + "/" + name
        
        with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/BRD_Charts_75-90/{}'.format(path_end)) as f:
            content = f.readlines()
            lyrics = ""
            for line in content:
                lyrics += line
 
        
        dic = {"titel": titel, "interpret": artist, "lyrics": lyrics}
        hit_json[jahr].append(dic)

    #print(hit_json)
    print(len(hit_json[jahr]))

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json', 'w') as f:
    json.dump(hit_json, f, ensure_ascii=False, indent=4)
