from os import listdir
from os.path import isfile, join
import json
#Speichern der Daten von Roman Schneider in Json-Datei -- gleiches Format wie DDR-Korpus
#Initialisiert leeres Dictionary 
hit_json = {}
#For-Schleife, welche die Jahre durchgeht
for jahr in range(1975,1991):
    #Casten zum String für Dateinamen
    jahr = str(jahr)
    #Erstellt leere Liste innerhalb des Dictionaries mit Jahr als Key
    hit_json[jahr] = []
    filenames = [f for f in listdir(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/BRD_Charts_75-90/{jahr}') if isfile(join(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/BRD_Charts_75-90/{jahr}', f))]
    #Geht Filenamen aus dem Ordner durch
    for name in filenames:
        #Splitet Dateinamen zwischen Artist und Titel
        artit = name.split('_-_')
        #Speichert Artistnamen in artist (ersetzt _ mit Leerzeichen)
        artist = artit[0].replace('_',' ')
        #löscht Dateiendung und speichert den Rest in titel
        titel = artit[1][:-4].replace('_',' ')
        #Erstellt Pfadende
        path_end = jahr + "/" + name
        
        with open(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/BRD_Charts_75-90/{path_end}') as f:
            content = f.readlines()
            lyrics = ""
            for line in content:
                lyrics += line
 
        #Speichert Daten in Dict
        dic = {"titel": titel, "interpret": artist, "lyrics": lyrics}
        #Fügt Dict in Liste
        hit_json[jahr].append(dic)

    #print(hit_json)
    print(len(hit_json[jahr]))
#Speichert Doppel-Dict in Json-Datei
with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json', 'w') as f:
    json.dump(hit_json, f, ensure_ascii=False, indent=4)
