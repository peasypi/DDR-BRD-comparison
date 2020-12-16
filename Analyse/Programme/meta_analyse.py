import json

DDR_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json"
BRD_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json"

paths = {DDR_PATH, BRD_PATH}


def analyze_meta(path):
    label = {}
    länder = {}
    styles = {}
    genres = {}
    interpreten = {}
    with open(p) as file:
        hit_json = json.load(file)
    for jahr in hit_json:
        for song in hit_json[jahr]:
            #Interpreten-Dict bestücken
            if "interpret" in song.keys():
                if song["interpret"] in interpreten.keys():
                    interpreten[song["interpret"]] = interpreten[song["interpret"]]+1
                else:
                    interpreten[song["interpret"]] = 1
            #Länder-Dict bestücken
            if "land" in song.keys():
                if song["land"] in länder.keys():
                    länder[song["land"]] = länder[song["land"]]+1
                else:
                    länder[song["land"]] = 1
            #Style-Dict bestücken -- jeder Style aus Style-Liste
            if "style" in song.keys():
                for sty in song["style"]:
                    if sty in styles.keys():
                        styles[sty] = styles[sty]+1
                    else:
                        styles[sty] = 1
            #Genre-Dict bestücken -- jedes Genre in der Genre-Liste
            if "genre" in song.keys():
                for gen in song["genre"]:
                    if gen in genres.keys():
                        genres[gen] = genres[gen]+1
                    else:
                        genres[gen] = 1
            #Label-Dict bestücken -- nur das 1. Label
            if "label" in song.keys():
                if song["label"][0] in label.keys():
                    label[song["label"][0]] = label[song["label"][0]]+1
                else:
                    label[song["label"][0]] = 1

    interpreten = {k: v for k, v in sorted(interpreten.items(), key=lambda item: item[1], reverse=True)}
    label = {k: v for k, v in sorted(label.items(), key=lambda item: item[1], reverse=True)}
    länder = {k: v for k, v in sorted(länder.items(), key=lambda item: item[1], reverse=True)}
    styles = {k: v for k, v in sorted(styles.items(), key=lambda item: item[1], reverse=True)}
    genres = {k: v for k, v in sorted(genres.items(), key=lambda item: item[1], reverse=True)}

    meta_analyse = {"interpreten": interpreten, "label": label, "länder": länder, "styles": styles, "genres": genres}

    return meta_analyse

for p in paths: 
    analyse = analyze_meta(p)
    if "ddr_charts" in p:
        land = "ddr"
    else:
        land = "brd"

    with open(f"/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/Ergebnisse/{land}_meta_analyse.json", 'w') as js:
        json.dump(analyse, js, indent=4, ensure_ascii=False)
    




    



