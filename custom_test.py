from nltk.corpus import inaugural, PlaintextCorpusReader
from CorpusReader_TFIDF import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import pandas as pd
import re
from numpy.linalg import norm

rootDir = 'C:\\Users\\mikec_g1kgiu8\\OneDrive\\Desktop\\CS 5322\\TF-IDF Custom Corpus'   # change that to the directory where the files are
newCorpus = PlaintextCorpusReader(rootDir, '.*')
tfidfCorpus = CorpusReader_TFIDF(newCorpus)

q = tfidfCorpus.tfidfAll()
for x in q:
   print(x, q[x])

print(tfidfCorpus.cosine_sim('Temp1.txt', 'Temp5.txt'))
print(tfidfCorpus.query(['good']))


#print("Doc6.txt", tfidfCorpus.tfidf("Doc6.txt"))
#print("New", tfidfCorpus.tfidfNew(['My', 'name', 'is', 'Bob', 'and', 'you', 'are', 'about', 'to', 'die']))
#print(tfidfCorpus.query(['My', 'name', 'is', 'Bob', 'and', 'you', 'are', 'about', 'to', 'die']))

'''
sentences = list()
with open("C:\\Users\\mikec_g1kgiu8\\OneDrive\\Desktop\\CS 5322\\TF-IDF Custom Corpus\\Test1.txt") as file:
    for line in file:
        for l in re.split(r"\.\s|\?\s|\!\s|\n",line):
            if l:
                sentences.append(l)
cvec = CountVectorizer(stop_words='english', min_df=3, max_df=0.5, ngram_range=(1,2))
sf = cvec.fit_transform(sentences)

transformer = TfidfTransformer()
transformed_weights = transformer.fit_transform(sf)
weights = np.asarray(transformed_weights.mean(axis=0)).ravel().tolist()
weights_df = pd.DataFrame({'term': cvec.get_feature_names_out(), 'weight': weights})

weights_df.sort_values(by='weight', ascending=False).head(50)

print(weights_df)


'''




#print(inaugural.sents(['1789-washington.txt', '1793-washington.txt']))
#print(inaugural.sents('1789-washington.txt'))
#temp = [ 7, 8, 9]
#print(type(temp))
#print(type(['1789-washington.txt']) == list)

#print(inaugural.fileids())
#print(type(inaugural))
#print(type(nltk.corpus.brown))
#print(type(nltk.corpus.alpino))
#print(type(nltk.corpus.switchboard))
#print(type(nltk.corpus.stopwords))
#print(type(nltk.corpus.universal_treebanks))
#print(type(inaugural) == nltk.corpus.util.LazyCorpusLoader)
#myCorpus = CorpusReader_TFIDF(inaugural, stopWord=14)
#print('Outside')

#print(myCorpus.tfidfNew(['citizens', 'economic', 'growth', 'economic']))
#print(myCorpus.query(['citizens', 'economic', 'growth']))

#tfidf = myCorpus.tfidfAll(True)
#for document in tfidf:
#    print(document, len(tfidf[document]))

#print(myCorpus.cosine_sim('2009-Obama.txt', '2013-Obama.txt'))
#print(myCorpus.cosine_sim('2013-Obama.txt', '2009-Obama.txt'))
#print(myCorpus.cosine_sim('2013-Obama.txt', '2013-Obama.txt'))
#print(myCorpus.cosine_sim('1789-Washington.txt', '1793-Washington.txt'))
#print(myCorpus.cosine_sim('1793-Washington.txt', '2013-Obama.txt'))

#print(len(myCorpus.tfidf('2009-Obama.txt')))
#print(len(myCorpus.tfidf('2009-Obama.txt', True)))


'''
i = 0
for key in tfidf['1789-Washington.txt']:
    i += 1
    if i % 1000 == 0:
        print(i, key, tfidf['1789-Washington.txt'][key])

print('Between the two')

i = 0
for key in tfidf['1793-Washington.txt']:
    i += 1
    if i % 1000 == 0:
        print(i, key, tfidf['1793-Washington.txt'][key])
'''
    
    #for word in tfidf[document]:
    #    if tfidf[document][word] == 0:
    #        print(word, tfidf[document][word])
#print(myCorpus.tfidf('1789-Washington.txt'))
#print(inaugural.raw('1789-Washington.txt'))
#for word in inaugural.words('1789-Washington.txt'):
#    print(word, end=" ")