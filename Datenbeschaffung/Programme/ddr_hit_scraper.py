from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json


# http://www.deutsche-mugge.de/index.php/ddr-hitparaden/7-ddr-hitparade-1975.html
hit_json = {}

def charts_crawlen(zahl, jahr):
    url = "http://www.deutsche-mugge.de/index.php/ddr-hitparaden/{}-ddr-hitparade-{}.html".format(zahl, jahr)

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    # Erstellen der leeren Json
    hit_json[jahr] = []
    liste = []

    # Heraussuchen der Charts aus HTML
    for span in soup.findAll('span', attrs={'style': 'font-family: Verdana,Arial,Helvetica,sans-serif; font-size: xx-small;'}):
        liste.append(span.text.strip())
    if not liste:
        for span in soup.findAll('span', attrs={'size': '1', 'face': 'Verdana, Arial, Helvetica, sans-serif'}):
            liste.append(span.text.strip())

    # Splitten des langen 'Chart'-Strings in einzelne Songs
    hits = re.split(r'\s?\d{1,2}\.\s{1}', liste[0])
    # Löschen der leeren Strings falls vorhanden
    hits = [song for song in hits if song != '']

    # Erstellen der Objekte und einfügen in Json
    platz = 1
    for i in hits:
        song = i.split(' - ')
        dic = {'titel': song[1], 'interpret': song[0], 'platzierung': platz}
        hit_json[jahr].append(dic)
        platz += 1

    #Json-Datei schreiben
    with open('ddr_charts.json', 'w') as f:
        json.dump(hit_json, f, ensure_ascii=False, indent=4)

    return hit_json




zahl = 7
jahr = 1975
for i in range(1975, 1991):
    charts_crawlen(zahl, i)
    zahl +=1
