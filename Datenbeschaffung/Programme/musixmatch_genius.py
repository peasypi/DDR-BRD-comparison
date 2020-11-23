"""LYRICSCRAWLER."""

# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import re
from urllib.parse import quote
import json
import time

# art = sys.argv[1]
# tit = sys.argv[2]

def find_hits(i):
    art = i['interpret']
    tit = i['titel']

    return (art, tit)


def url_endung(art, tit, jahr):
    artist = ""
    i = 0
    k = 0
    while i < len(art.split(" ")):
        if i == 0:
            artist = art.split(" ")[i]
        else:
            artist = artist + '-' + art.split(" ")[i]
        i = i + 1

    while k < len(tit.split(" ")):
        if k == 0:
            tit = re.sub(r'\?|!|\.|\'', '', tit)
            title = tit.split(" ")[k]
        else:
            title = title + '-' + tit.split(" ")[k]
        k = k + 1

    endung = artist + "/" + title + '-' + jahr
    eventuelle_endung = artist + "/" + title
    return (endung, eventuelle_endung)


def request(endung, eventuelle_endung):
    lyrics = ""
    try:
        url = f"https://www.musixmatch.com/de/songtext/{quote(endung)}"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except HTTPError:
        try:
            url = f"https://www.musixmatch.com/de/songtext/{quote(eventuelle_endung)}"
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
        except HTTPError:
            print("[ERROR] Keine Lyrics für " + endung + " auf Musixmatch gefunden!")
            return("Kein Text gefunden!")

    soup = BeautifulSoup(webpage, 'html.parser')
    song_json = {}
    song_json["Lyrics"] = []

    # Extract Title of the song
    song_json["Title"] = soup.title.string

    # Extract the Lyrics of the song
    for span in soup.findAll('span', attrs={'class': re.compile(r'lyrics__content__\w+')}):
        song_json["Lyrics"].append(span.text.strip().split("\n"))

    # Falls Seite zwar vorhanden, aber keine Lyrics -- versuchs auf nem anderen Portal
    if not song_json["Lyrics"]:
        # print('[INFO] Ich suche jetzt nach ' + endung + ' auf genius')
        return("Kein Text gefunden!")

    # Save the json created with the file name as title + .json
    # with open(song_json["Title"] + '.json', 'w', encoding='utf8') as file:
    #    json.dump(song_json, file, indent=4, ensure_ascii=False)

    for i in song_json['Lyrics']:
        teil = "\n".join(i)
        lyrics = lyrics + "\n" + teil

    return lyrics


def secondrequest(eventuelle_endung):
    lyrics = ""
    split = eventuelle_endung.split('/')
    end = split[0] + '-' + split[1]
    try:
        url = f"https://genius.com/{quote(end)}-lyrics"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except HTTPError:
        print("[ERROR] Keine Lyrics für " + eventuelle_endung + " auf genius.com gefunden!")
        return("Kein Text gefunden!")

    soup = BeautifulSoup(webpage, 'html.parser')
    song_json = {}
    song_json["Lyrics"] = []
    # song_json["Comments"] = []

    # Extract Title of the song
    song_json["Title"] = soup.title.string

    # Extract the Lyrics of the song
    for div in soup.findAll('div', attrs={'class': 'lyrics'}):
        song_json["Lyrics"].append(div.text.strip().split("\n"))

    if not song_json['Lyrics']:
        print("[ERROR] Auch auf Genius nichts gefunden")
        return("Kein Text gefunden")

    # Save the json created with the file name as title + .json
    # with open(song_json["Title"] + '.json', 'w') as file:
    #   json.dump(song_json, file, indent=4, ensure_ascii=False)
    for i in song_json['Lyrics']:
        teil = "\n".join(i)
        lyrics = lyrics + "\n" + teil

    return lyrics
