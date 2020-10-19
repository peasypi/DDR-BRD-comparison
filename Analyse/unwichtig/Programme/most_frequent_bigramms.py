from collections import Counter
import nltk
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from HanTa import HanoverTagger as ht
from wordcloud import WordCloud, ImageColorGenerator

txtfile = "Hallo wie geht es dir? Und wie geht es deinem Opa? Schmeckt es dir? Sagt man Hallo wie Hello?"
txtfile = re.sub(r'\'|\.\.\.|\.|´|!|\?|,|:|–|;|`|\"|\\', "", txtfile)
words = nltk.tokenize.word_tokenize(txtfile,language='german')
liste = list(nltk.bigrams(words))
bigrms = []
for i in liste:
    bigrms.append(' '.join(i).lower())
counts = Counter(bigrms)
print(counts.most_common())

'''wordcloud = WordCloud(max_words=20, background_color="white", colormap='GnBu').generate_from_frequencies(dict(counts))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/bigramm_cloud.png')
plt.show()'''