from nltk.corpus import inaugural, PlaintextCorpusReader
from CorpusReader_TFIDF import *
import numpy as np

a = 4
if a > 3:
    b = 19
else:
    b = 22

print(b)

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