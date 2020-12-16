from collections import Counter 

#Counter zählt die most frequent words in der Liste ohne Stopwörter
def count_mfw(tokenliste):        
    Zaehler = Counter(tokenliste)
    most_occur = Zaehler.most_common(20)
    #print(most_occur)
    return most_occur

#Most frequent Bigramme
def get_bigrams(worte):
    liste = list(nltk.bigrams(worte))
    bigrms = []
    for i in liste:
        bigrms.append(' '.join(i).lower())
    counts = Counter(bigrms)
    most_bigrams = counts.most_common(20)
    for b in most_bigrams[:]:
        if b[0] == '-- --':
            most_bigrams.remove(b)
    return most_bigrams