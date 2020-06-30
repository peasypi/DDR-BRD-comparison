from bs4 import  BeautifulSoup
from urllib.request import Request, urlopen
import json
import re
import pprint

hit_json = {}
# jahr = "1975"
def brd_crawlen(jahr):
    url = "https://www.chartsurfer.de/musik/single-charts-deutschland/jahrescharts/hits-{}/top-100".format(jahr)

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    # Initialisierung
    hit_json[jahr] = []
    #liste = []
    platz = 1

    for a,b in zip(soup.findAll('a', attrs={'class':'style-1 font-weight-bold icon-magnifier'}),soup.findAll('a', attrs={'class':'style-2 icon-magnifier'})):
        dic = {'titel': a.text, 'interpret': b.text, 'platzierung': platz}
        hit_json[jahr].append(dic)
        platz += 1


    with open('brd_charts.json', 'w') as f:
        json.dump(hit_json, f, ensure_ascii=False, indent=4)

    return hit_json

# brd_crawlen("1975")
for i in range(1975, 1991):
    brd_crawlen(i)
