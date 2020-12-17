import json

with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json", 'r') as js:
    ddr_json = json.load(js)

with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/brd_charts.json", 'r') as js:
    brd_json = json.load(js)

rocksongs_ddr = []
popsongs_ddr = []
rocksongs_brd = []
popsongs_brd = []

for jahr in ddr_json:
    for song in ddr_json[jahr]:
        if "genre" in song.keys():
            if "Rock" in song["genre"]:
                rocksongs_ddr.append(song["lyrics"])
            elif "Pop" in song["genre"]:
                popsongs_ddr.append(song["lyrics"])

for jahr in brd_json:
    for song in brd_json[jahr]:
        if "genre" in song.keys():
            if "Rock" in song["genre"]:
                rocksongs_brd.append(song["lyrics"])
            elif "Pop" in song["genre"]:
                popsongs_brd.append(song["lyrics"])

print(len(rocksongs_ddr))
print(len(popsongs_ddr))
print(len(rocksongs_brd))
print(len(popsongs_brd))

a = len(rocksongs_brd) + len(rocksongs_ddr)
b = len(popsongs_brd) + len(popsongs_ddr)

print(a)
print(b)
#print(int(len(rocksongs_brd)/30))


"""def chunks(lst, n):
    #Yield successive n-sized chunks from lst.
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

chunks_rock_brd = list(chunks(rocksongs_brd, 30))
chunks_rock_ddr = list(chunks(rocksongs_ddr, 30))
chunks_pop_brd = list(chunks(popsongs_brd, 30))
chunks_pop_ddr = list(chunks(popsongs_ddr, 30))

counter = 1
for chunk in chunks_rock_brd:
    counter += 1
    for song in chunk:
        for line in song:
    with open(f'/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/txt_genres/rock_brd_{counter}', 'w') as file:"""
