import json

DDR_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json"
BRD_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json"

paths = [DDR_PATH, BRD_PATH]

for p in paths:
    if "ddr_charts" in p:
        land = "ddr"
    else:
        land = "brd"
    
    with open(p) as js:
        hit_json = json.load(js)
    
    for jahr in hit_json:
        for song in hit_json[jahr]:
            text = song["lyrics"]
            titel = song["titel"]
            artist = song["interpret"]
            name = f"{jahr}-{titel.replace(' ', '_')}-{artist.replace(' ','_')}"
            txtfile = open(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/txt_songs/{land.upper()}/{name}.txt', 'w')
            for line in text:
                txtfile.write(line)
            txtfile.close()