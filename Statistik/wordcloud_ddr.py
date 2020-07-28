import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import json
import re
from nltk.tokenize import word_tokenize
from spacy.lang.de.stop_words import STOP_WORDS
from nltk.corpus import stopwords

stopset = stopwords.words('german')
#from stop_words import get_stop_words

with open('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Datenbeschaffung/Data/ddr_charts.json') as file:
    ddr_hits = json.load(file)

all_lyrics_ddr = ""
for jahr in ddr_hits:
    for i in ddr_hits[jahr]:
        all_lyrics_ddr = all_lyrics_ddr + "\n\n" + i["lyrics"]

all_lyrics_ddr = re.sub(r'\'|\.\.\.|\.|´|!|\?|,|:|–|;|`|\"|\\', "", all_lyrics_ddr)

text_tokens = text_tokens = word_tokenize(all_lyrics_ddr)
tokens_without_sw= [word for word in text_tokens if not word.lower() in stopset]

text = " ".join(tokens_without_sw)

wordcloud = WordCloud(max_words=50, background_color="white").generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#print(stopset)