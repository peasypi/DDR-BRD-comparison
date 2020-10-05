from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import lyrix_scraper as lx



JSON_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json"
CHROMEDRIVER_PATH = "/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Utility/chromedriver"

#with open(JSON_PATH) as file:
#    ddr_hits = json.load(file)

ddr_hits = {
    "1975": [
        {
            "titel": "In jener Nacht",
            "interpret": "Veronika Fischer",
            "platzierung": 1,
            "lyrics": "Und da war eine Nacht\nUnd da war auch ein Traum\nHaa haa haa in jener Nacht\n\nUnd da war auch ein Lied\nUnd da war manch ein Wort\nHaa haa haa in jener Nacht\nHaa haa haa in jener Nacht\n\nDoch der Traum ist ertrunken\nim Morgentau ahhhaha\nUnd das Lied ist versunken\nim Morgengrau ahhhaha\n\n\nUnd doch waren wir zwei\nUnd doch waren wir eins\nHaa haa haa in jener Nacht\n\nUnd doch waren wir leis´\nUnd doch brannten wir heiß\nHaa haa haa in jener Nacht\nHaa haa haa in jener Nacht\n\nUnd behutsam wie einen sehr seltenen Stein haa haa\nSo fass ich jede Nacht in Erinnerung ein\nHaa haa\n\n\nHaa haa haa in jener Nacht\nHaa haa haa in jener Nacht\nHaa haa haa in jener Nacht\n            ",
            "tokenanzahl": 132,
            "typeanzahl": 42,
            "type/token": 31.82
        },
        {
            "titel": "Doch ich wollte es wissen",
            "interpret": "Kreis",
            "platzierung": 2,
            "lyrics": "So um zehn in der Disco fiel ein Mädchen mir auf,\ndas ich vorher noch niemals hier geseh'n.\nSchwarz ihre Haare,\nkapp siebzehn Jahre\nund ihre Augen schöööön.\nUnd ich sah sie an und ihr Blick hielt mir Stand,\nsonderbar, das ist mir nie passiert,\nirgendwie hat mich das irritiert.\n\nDoch ich wollte es wissen,\ndoch ich wollte es wissen,\nich ging sogleich zu ihr,\nsie tanzte auch mit mir.\n\nSo weit zurück, drückte ich sie ganz fest an mich heran,\nmit 'nem Lächeln, lies sie das auch geschehn.\nWeichn und so biegsam,\naber nicht schmiegsam\nwer sollte das versteh'n?\nUnd ich fragte sie dann, ob sie noch zu haben wär'.\nJa, vielleicht, das wisse sie noch nicht,\nsonderbar, was so ein Mädchen spricht.\n\nDoch ich wollte es wissen,\ndoch ich wollte es wissen,\nsie machte es mir schwer,\ndas reizte mich noch mehr.\n\nSo um zwei war die Disco dann wie immer schon aus,\nund ich brachte sie aufgeregt nach Haus.\nNicht mal ein bisschen,\nnein, nicht ein Küsschen,\ndas hält doch keiner aus.\nDoch ich fragte sie noch, ob ich wieder kommen könnt,\nwenn ich nicht so siegessicher wär',\nsagte sie, hätt' ich es halb so schwer,\nschwer, schwer.\n\nDoch ich werde es wissen,\ndoch ich werde es wissen,\ndas nächste Mal bin ich ganz lieb und fromm,\nmal sehn. Ob ich bei ihr dann weiter komm',\nkomm', komm'.\n\nDoch ich werde es wissen,\nha, ha ha, ha, ha, ha, ha.\n\n",
            "tokenanzahl": 247,
            "typeanzahl": 120,
            "type/token": 48.58
        },
        {
            "titel": "Auf der Wiese",
            "interpret": "Veronika Fischer",
            "platzierung": 3,
            "lyrics": "\nAuf Der Wiese haben wir gelegen\nUnd wir haben Gras gekaut.\nFolgen wollt' er mir auf allen Wegen.\nBlumen hat er mir geklaut.\n\nMontag hat er mir das Haar gekämmt.\nDienstag gingen wir ins Kino.\nMittwoch hab' ich ihm was vorgeflennt,\nDenn wir hatten nur Casino.\nUnd den Donnerstag, den ganzen,\nBlieben wir in unserm Bett.\nUnd den Freitag war'n wir tanzen.\nWenn ich nur den Freitag hätt'.\nSamstag sagte er mir in die Ohren,\nDaß er mich wie irre liebt.\nUnd er hätte sicher auch geschworen,\nDaß es keine andre gibt.\n\nAuf Der Wiese haben wir gelegen\nUnd wir haben Gras gekaut.\nFolgen wollt er mir auf allen Wegen.\nBlumen hat er mir geklaut.\n\nSonntag ist er fortgegangen,\nIst für immer mir entwischt.\nAch ich hätt' ihn aufgehangen,\nHätte ich ihn bloß erwischt.\nSamstag sagte er mir in die Ohren,\nDaß er mich wie irre liebt.\nUnd er hätte sicher auch geschworen,\nDaß es keine andre gibt.\n\nAuf Der Wiese habe ich gelegen\nUnd ich habe Gras gekaut.\nFolgen trage ich auf allen Wegen.\nBlumen klaun', hab' ich mich nicht\nGetraut.",
            "tokenanzahl": 184,
            "typeanzahl": 83,
            "type/token": 45.11
        },
        {
            "titel": "Langstreckenlauf",
            "interpret": "Puhdys",
            "platzierung": 4,
            "lyrics": "Es ist ein harter Kampf, wenn man Sieger werden will.\nMan quält sich jeden Morgen, alles liegt noch schlafend still.\nDas Herz schlägt an die Rippen keuchend zieht man Kreis um Kreis.\nUnd Krämpfe hämmern, bitter schmeckt der Schweiß.\n\nDie Lungen schmerzen, pfeifen wild.\nEin Feuer brennt in uns und wühlt.\nDas ist egal, egal. Man will ganz oben stehn.\n\nEs ist ein harter Kampf, wenn man Sieger werden will.\nMan jagt die fremden Schatten angetrieben von Gebrüll.\nUnd stößt sich selber weiter, unter Tausenden allein.\nSchwer die Zunge, als wäre sie ein Stein.\n\nDie Füße brennen heiß wie Blei.\nIn allen Gliedern steckt ein Schrei.\nDas ist egal, egal. Man will ganz oben stehn.\n\nJage und treibe und flieg! Reiß aus dem Leib Dir den Sieg.\nJage und treibe und flieg! Reiß aus dem Leib Dir den Sieg.\n\nJage und treibe und flieg! Reiß aus dem Leib Dir den Sieg.\nJage und treibe und flieg! Reiß aus dem Leib Dir den Sieg.\n\nEs ist ein harter Kampf, wenn man Sieger werden will.\nMan jagt die fremden Schatten angetrieben von Gebrüll.\nUnd stößt sich selber weiter, unter Tausenden allein.\nSchwer die Zunge, als wäre sie ein Stein.\n\nDie Füße brennen heiß wie Blei.\nIn allen Gliedern steckt ein Schrei.\nDas ist egal, egal. Man will ganz oben stehn.\n\nJage und treibe und flieg! Reiß aus dem Leib Dir den Sieg.\nJage und treibe und flieg! Reiß aus dem Leib Dir den Sieg.\n\nJage und treibe und flieg! Reiß aus dem Leib Dir den Sieg.\nJage und treibe und flieg! Reiß aus dem Leib Dir den Sieg.\n            ",
            "tokenanzahl": 266,
            "typeanzahl": 86,
            "type/token": 32.33
        },
        {
            "titel": "Sommer adé",
            "interpret": "Schubert Formation",
            "platzierung": 5,
            "lyrics": "Der letzte Sommer war ein heißer,\nnun scheint die Sonne wieder leiser.\nDas ist auch gut,\ndenn verzehrend war die Glut.\n\nSommer ade,\nich freu mich auf Schnee\nLeute.Und auch die Liebe war kein Segen,\nman war zu faul sich zu bewegen.\nEs war zu heiß\n\nund hoch der Preis.\nIn Strömen rann der Schweiß,\nman blieb abstinent\n\nselbst ohne Hemd\nLeute.Im Freibad gab es kaum `nen Stehplatz,\ndafür in jeder Kneipe Rabatz.\n\nDas Bier war warm, die Wurst war kalt,\nman stand und wurde alt.\n\nHoch war der Preis\nwie jeder weiß\nLeute.Der letzte Sommer war ein heißer,\nnun scheint die Sonne wieder leiser.\nDas tut so gut\nnach all der Glut\nich fühl mich wohlgemut.\nSommer ade\nich freu mich auf Schnee,\nLeute.Nun wird es langsam wieder kühle\nes reguliern sich die Gefühle,\nund weit und breit,\nda liebt man sich mit Freud.\nEs macht wieder Spaß\nim Bett und im Gras\nLeute.Der letzte Sommer war ein heißer,\nnun scheint die Sonne wieder leiser.\nDas tut so gut\nnach all der Glut\nich fühl mich wohlgemut.\nSommer ade\nich freu mich auf Schnee,\nLeute.",
            "tokenanzahl": 192,
            "typeanzahl": 89,
            "type/token": 46.35
        },
        {
            "titel": "Sieben Meter Seidenband",
            "interpret": "Prinzip",
            "platzierung": 6,
            "lyrics": "Sieben Meter Seidenband\n \nzwischen deinem und meinem Land. \nMädchen, das geht nicht. \nAlle Tage nur zu zwei `n \nund nicht einen Tag allein, \nMädchen, das geht nicht. \nImmer nur an deinem Hals \nda vergeht mir das Gefall`n \nMädchen, das geht nicht. \nStellst du das nur vor \ndann vergiss, was ich dir schwor. \nMädchen, das geht nicht.\nSie müssen treu sein\n \nob nah und fern, \ndann ich lieb sie lange, \ndann ich lieb sie gern. \nDann lieb sie lange, \ndann ich lieb sie gern. \n \nAlle Tage Hand in Hand\n \nund nichts andres` mehr gekannt, \nMädchen, das geht nicht. \nLiebste geht nur hinter mir, \ngehn` die Freunde mir verlor`n. \nMädchen, das geht nicht. \nUnd die Freunde brauch` ich sehr \nsonst fällt mir das atmen schwer, \nMädchen, das geht nicht. \nAlso lass uns unser Heim \nbitte kein Gefängnis sein. \nMädchen, das geht nicht. \n \nSie müssen treu sein\n \nob nah und fern, \ndann ich lieb sie lange, \ndann ich lieb sie gern. \nDann lieb sie lange, \ndann ich lieb sie gern. \n\n",
            "tokenanzahl": 175,
            "typeanzahl": 74,
            "type/token": 42.29
        }
    ]
}

driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get('https://www.discogs.com/')
# Cookies akzeptieren
driver.find_element_by_id("onetrust-accept-btn-handler").click()

for jahr in ddr_hits:
    for i in ddr_hits[jahr]:
        style = []
        genre = ""
        label = ""
        lied, titel, artist = lx.find_hits(i)

        # Artist + Titel + Single in Suchleiste eingeben - Return
        element = driver.find_element_by_id('search_q')
        element.send_keys(lied + ' single')
        element.send_keys(Keys.RETURN)
        
        try:
            # Result klicken
            results = driver.find_element_by_class_name('search_result_title')
            driver.execute_script("arguments[0].click();", results)
            # Metadaten crawlen
            lab = driver.find_element_by_css_selector("a[href*='label']")
            label = lab.get_attribute('innerHTML')
            gen = driver.find_element_by_css_selector("a[href*='genre']")
            genre = gen.get_attribute('innerHTML')
            st = driver.find_element_by_css_selector("a[href*='style']").get_attribute('innerHTML')
            style = st.split('-')

            i["label"]=label
            i["genre"]=genre
            i["style"]=style
        except NoSuchElementException:
            pass

print(ddr_hits)

