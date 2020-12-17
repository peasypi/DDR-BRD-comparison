from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import quote
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import login as log
import re
import json


hit_json = {}

def charts_crawlen(zahl, jahr):
    url = f"http://www.deutsche-mugge.de/index.php/ddr-hitparaden/{zahl}-ddr-hitparade-{jahr}.html"

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

def find_hits(i):
    # Sucht Daten aus Json-Datei
    art = i['interpret']
    tit = i['titel']
    # bereinigen
    tit = re.sub(r"\?|'|\.|,|!|\.\.\.", "", tit)
    tit = re.sub(r"ß", "ss", tit)

    lied = art + ' ' + tit
    return (lied, tit, art)


def capitalize_it(titel):
    tit = ""
    tit_list = titel.split(" ")
    for wort in tit_list:
        tit += wort.capitalize() + " "
    titel = tit[:-1]
    return titel

def login(driver):
    # Einloggen auf lyrix.at
    username = driver.find_element_by_id('user')
    username.clear()
    username.send_keys(log.username)

    password = driver.find_element_by_id('pass')
    password.clear()
    password.send_keys(log.password)

    login = driver.find_element_by_name('doLogin')
    driver.execute_script("arguments[0].click();", login)

    return True


def find_url(i, lied, titel, artist, driver):
    # Capitalized Titel
    cap_titel = capitalize_it(titel)
    # Titel mit ß statt ss/ohne ss -- oss
    titel_oss = re.sub("ss", "ß", titel)
    # Lied mit ß statt ss
    lied_oss = re.sub("ss", "ß", lied)
    # Titel -- capitalized und ohne ss
    cap_oss_titel = capitalize_it(titel_oss)
    # Suche nach Titel auf Artist-Seite
    try: 
        driver.get(f'https://lyrix.at/lyrics/{artist.lower()}/')                
        results = driver.find_element_by_link_text(titel)
    except NoSuchElementException:
        # Suche nach Titel auf Artist-Seite capitalized
        try:              
            results = driver.find_element_by_link_text(cap_titel)
        except NoSuchElementException:
            # Suche nach Titel auf Artist-Seite capitalized und ohne ss
            try:
                results = driver.find_element_by_link_text(cap_oss_titel)
            except NoSuchElementException:
                # Suche nach Titel auf Artist-Seite lower()
                try:
                    results = driver.find_element_by_link_text(titel.lower())
                except NoSuchElementException:
                    try:
                        element = driver.find_element_by_name('sartist')
                        element.send_keys(lied)
                        driver.find_element_by_name('ssubmit').click()
                        results = driver.find_element_by_link_text(titel)
                    except NoSuchElementException:
                        # Suche nach capitalized Titel
                        try:
                            results = driver.find_element_by_link_text(cap_titel)
                        except NoSuchElementException:
                            # Suche nach Titel in klein
                            try:
                                results = driver.find_element_by_link_text(titel.lower())
                            except NoSuchElementException:
                                # Suche nach Titel mit ß statt ss
                                try:
                                    element = driver.find_element_by_name('sartist')
                                    element.send_keys(lied_oss)
                                    driver.find_element_by_name('ssubmit').click()
                                    results = driver.find_element_by_link_text(titel_oss)
                                except NoSuchElementException:
                                    # Suche nach Titel mit ß statt ss und capitalized
                                    try:
                                        results = driver.find_element_by_link_text(cap_oss_titel)
                                    except NoSuchElementException:
                                        return "No Lyrics"

    driver.execute_script("arguments[0].click();", results)
    url = driver.current_url
    return url


def get_lyrics(url, driver):
    text = ""
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    song_json = {}
    song_json["Lyrics"] = []

    # Extract Title of the song
    song_json["Title"] = soup.title.string

    # Extract the Lyrics of the song
    for div in soup.findAll('div', attrs={'class': 'songtext'}):
        text = str(div).replace("<br/> <br/>", '\n\n')
        text = text.replace("<br/>", '\n')
        text = re.sub(r'<br/>', '\n', str(div))
    text = re.sub(r'<.*>','', text)
    text = re.sub(r'^\s+', '', text, re.MULTILINE)
    # i['lyrics'] = lyrics

    return text

##Ab hier: Funktionen für die Musixmatch/Genius-Suche
def m_find_hits(i):
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


JSON_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json"
CHROMEDRIVER_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Utility/chromedriver"

def main(driver):
    # Json öffnen
    with open(JSON_PATH) as file:
        ddr_hits = json.load(file)

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

    # Suche auf Musixmatch und Genius
    for jahr in ddr_hits:
        for i in ddr_hits[jahr]:
            if 'lyrics' not in i:
                art, tit = mg.find_hits(i)
                lied = art+"-"+tit
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