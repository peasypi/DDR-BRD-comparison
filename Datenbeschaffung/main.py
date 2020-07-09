# -*- coding: UTF-8 -*-

from selenium import webdriver
# from lyrix_scraper import login
import lyrix_scraper as lx
import try_musixmatch as mg
import time
import json

JSON_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json"
CHROMEDRIVER_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Utility/chromedriver"

def main(driver):
    # Json öffnen
    with open(JSON_PATH) as file:
        ddr_hits = json.load(file)

    # lx = lyrix_scraper()
    # mg = try_musixmatch()

    s = 0
    e = 0
    length = 0
    # Anzahl der Lieder berechen
    for jahr in ddr_hits:
        for i in ddr_hits[jahr]:
            length += 1

    # Lyrix.at-Suche
    for jahr in ddr_hits:
        for i in ddr_hits[jahr]:
            if 'lyrics' not in i:
                lied, titel, artist = lx.find_hits(i)
                url = lx.find_url(i, lied, titel, artist, driver)
                if url == "No Lyrics":
                    print("[ERROR] Keine Lyrics zu " + lied + ' gefunden!')
                else:
                    print("[SUCCESS] Lyrics zu " + lied + " gefunden!")
                    lyrics = lx.get_lyrics(url, driver)
                    i['lyrics'] = lyrics
            else:
                pass

    # erfolgsquote = (s * 100) / length
    # fehlerquote = 100 - erfolgsquote
    # print("Nach der Suche nur auf Lyrix.at:\n" + str(s) + " Lyrics gefunden \n" + str(e) + " nicht gefunden\n" + str(erfolgsquote) + "% der Lyrics wurden gefunden.\nDaraus ergibt sich eine Fehlerquote von " + str(fehlerquote) + "%")

    # Suche auf Musixmatch und Genius
    for jahr in ddr_hits:
        for i in ddr_hits[jahr]:
            if 'lyrics' not in i:
                art, tit = mg.find_hits(i)
                lied = art+"-"+tit
                # jahr = '1975'
                endung, eventuelle_endung = mg.url_endung(art, tit, jahr)
                lyrics = mg.request(endung, eventuelle_endung)
                time.sleep(10)
                if not lyrics:
                    print("[INFO] Keine Lyrics bekommen!")
                if lyrics == "Kein Text gefunden!":
                    print('[INFO] Ich suche jetzt nach ' + endung + ' auf genius')
                    lyrics = mg.secondrequest(eventuelle_endung)
                    if lyrics == "Kein Text gefunden!":
                        print("[ERROR] Keine Lyrics zu " + lied + ' gefunden!')
                        pass
                    else:
                        i['lyrics'] = lyrics
                        print('[SUCCESS] Habe ' + endung + ' auf genius.com gefunden!')
                else:
                    i['lyrics'] = lyrics
                    print('[SUCCESS] Habe ' + endung + ' auf Musixmatch gefunden!')
            else:
                pass

# Erfolg berechnen
    for jahr in ddr_hits:
        for i in ddr_hits[jahr]:
            if 'lyrics' in i:
                s += 1
            else:
                e += 1

    erfolgsquote = (s * 100) / length
    fehlerquote = 100 - erfolgsquote

    print("Es wurde nach " + str(length) + " Liedtexten gesucht\n" + "Nach der vollständigen Suche:\n" + str(s) + "/" + str(length) + " Lyrics gespeichert \n" + str(e) + "/" + str(length) + " Lyrics nicht gefunden\n" + str(erfolgsquote) + "% der Lyrics wurden gefunden.\nDaraus ergibt sich eine Fehlerquote von " + str(fehlerquote) + "%")

    with open(JSON_PATH, 'w') as file:
        json.dump(ddr_hits, file, indent=4, ensure_ascii=False)

driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get('https://lyrix.at')
log = lx.login(driver)
if log == True:
    main(driver)