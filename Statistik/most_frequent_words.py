from collections import Counter 
from spacy.lang.de.stop_words import STOP_WORDS
import spacy
import re

dic = {
            "titel": "Lachen und Schweigen",
            "interpret": "Puhdys",
            "platzierung": 4,
            "lyrics": "Trug der Wind ihr Lachen durch die Nacht und sie tanzte in seinem Blick\nTrug der Wind ihr Lachen durch die Nacht und er nahm sie mit sich mit.\nDoch eine Nacht ist schnell vorbei, eine Nacht ist schnell vorbei.\nWenn ein Traum, wenn ein Traum, wenn ein Traum beginnt, spielen Perlen im Licht.\nWenn ein Traum, wenn ein Traum, wenn ein Traum beginnt, sieht man vieles nicht.\n\nTrug der Wind Musik durch diese Nacht und sein Zimmer war viel zu heiß.\nTrug der Wind Musik durch diese Nacht und sie kannte nicht seinen Preis.\nDenn eine Nacht ist schnell vorbei, eine Nacht ist schnell vorbei.\nWenn ein Traum, wenn ein Traum, wenn ein Traum beginnt, spielen Perlen im Licht.\nWenn ein Traum, wenn ein Traum, wenn ein Traum beginnt, sieht man vieles nicht.\n\nTrug der Wind ihr Schweigen durch die Nacht und die Straßen waren so kalt.\nTrug der Wind ihr Schweigen durch die Nacht eine Nacht, die sie längst bereut.\nDenn eine Nacht ist schnell vorbei, eine Nacht ist schnell vorbei.\nWenn ein Traum, wenn ein Traum, wenn ein Traum beginnt, spielen Perlen im Licht.\nWenn ein Traum, wenn ein Traum, wenn ein Traum beginnt, sieht man vieles nicht.\nWenn ein Traum, wenn ein Traum, wenn ein Traum beginnt, spielen Perlen im Licht.\nWenn ein Traum, wenn ein Traum, wenn ein Traum beginnt, sieht man vieles nicht.\n            ",
            "tokenanzahl": 229,
            "typeanzahl": 54,
            "type/token": 23.58
        }

nlp = spacy.load('de')
spacy_doc = nlp(dic["lyrics"])

token = [tok.text.lower() for tok in spacy_doc]
# Löschen der new lines
for t in token:
    if re.match(r'(\n)+\s*', t):
        token.remove(t)
# Löschen der Sonderzeichen
for t in token:
    if re.match(r'\'|\.\.\.|\.|´|!|\?|,|:|-|;', t):
        token.remove(t)
    
removed_stopwords = [tok for tok in token if tok not in STOP_WORDS]

Counter = Counter(removed_stopwords)
most_occur = Counter.most_common(4) 

print(most_occur)