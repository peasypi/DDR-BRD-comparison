from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import re
import login as log

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
