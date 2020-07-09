import nltk
import spacy

text = "Und da war eine Nacht\nUnd da war auch ein Traum\nHaa haa haa in jener Nacht\n\nUnd da war auch ein Lied\nUnd da war manch ein Wort\nHaa haa haa in jener Nacht\nHaa haa haa in jener Nacht\n\nDoch der Traum ist ertrunken\nim Morgentau ahhhaha\nUnd das Lied ist versunken\nim Morgengrau ahhhahaUnd doch waren wir zwei\nUnd doch waren wir eins\nHaa haa haa in jener Nacht\n\nUnd doch waren wir leis´\nUnd doch brannten wir heiß\nHaa haa haa in jener Nacht\nHaa haa haa in jener Nacht\n\nUnd behutsam wie einen sehr seltenen Stein haa haa\nSo fass ich jede Nacht in Erinnerung ein\nHaa haaHaa haa haa in jener Nacht\nHaa haa haa in jener Nacht\nHaa haa haa in jener Nacht"

liste = nltk.word_tokenize(text)

nlp = spacy.load('de')

spacy_doc = nlp(text)

print([tok.text for tok in spacy_doc])