from nltk.corpus import inaugural, brown, treebank, names, PlaintextCorpusReader
from CorpusReader_TFIDF import *

try:
    invalid1 = CorpusReader_TFIDF("word")
except:
   print("invalid1 not created")

try:
    invalid2 = CorpusReader_TFIDF(inaugural, tf=True)
except:
   print("invalid2 not created")

try:
    invalid3 = CorpusReader_TFIDF(inaugural, Idf=87)
except:
   print("invalid3 not created")

try:
    invalid4 = CorpusReader_TFIDF(inaugural, stopWord=False)
except:
   print("invalid4 not created")

try:
    invalid5 = CorpusReader_TFIDF(inaugural, toStem=77)
except:
   print("invalid5 not created")

try:
    invalid6 = CorpusReader_TFIDF(inaugural, ignoreCase="True")
except:
   print("invalid6 not created")

try:
    invalid7 = CorpusReader_TFIDF(inaugural, tf="log", Idf="smooth", toStem="Yes")
except:
   print("invalid7 not created")

corpus1 = CorpusReader_TFIDF(inaugural)

#print("Corpus1", corpus1.tfidf('1789-Washington.txt'))
print(corpus1.tfidfNew(['A', 'new', 'speech', 'about', 'being', 'a', 'president']))
print(corpus1.idf()['a'])

all = corpus1.tfidfAll()
for single in all:
    if 'a' not in all[single]:
        print(single)

print(corpus1.raw('1793-Washington.txt'))

#rootDir = 'C:\\Users\\mikec_g1kgiu8\\OneDrive\\Desktop\\CS 5322\\TF-IDF Custom Corpus'   # change that to the directory where the files are
#newCorpus = PlaintextCorpusReader(rootDir, '.*')

#corpus2 = CorpusReader_TFIDF(newCorpus, toStem=True)