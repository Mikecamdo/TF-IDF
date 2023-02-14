#import nltk
#nltk.download('inaugural')
from nltk.corpus import inaugural, PlaintextCorpusReader
from CorpusReader_TFIDF import *

myCorpus = CorpusReader_TFIDF(inaugural)
print(myCorpus.tfidf('1789-Washington.txt'))
#print(inaugural.raw('1789-Washington.txt'))