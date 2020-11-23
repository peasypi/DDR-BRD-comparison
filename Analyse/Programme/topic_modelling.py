import dariah
#from nltk.corpus import stopwords
import matplotlib.pyplot as plt


#stopset = stopwords.words('german')
with open("/Users/pia/Desktop/Uni/Bachelor-Arbeit/DDR-BRD-comparison/Analyse/de_stopword_dariah.txt", "r") as file:
   content = file.readlines()

stopwords = []

for c in content:
    stopwords.append(c.replace("\n", ""))

#print(stopwords)
model, vis = dariah.topics(directory="/Users/pia/Desktop/Try_corpus", stopwords=stopwords, num_topics=5, num_iterations=10000)



print(model.topics.iloc[:5, :10])
fig = vis.topic_document()

plt.savefig("topicmodell_ddr.png")