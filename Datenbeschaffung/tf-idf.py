import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documentA = "Der Hund läuft durch den schönen Wald"
documentB = "Die schönen Haare des Mädchen gefallen mir sehr."

bagOfWordsA = documentA.split(" ")
bagOfWordsB = documentB.split(" ")

uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))

#print(uniqueWords)

numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1

numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1

print(numOfWordsA)
print(numOfWordsB)

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)

print(tfA)
print(tfB)