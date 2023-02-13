import nltk.corpus
#FIXME take a look at Plaintext Corpus Reader (?)

class CorpusReader_TFIDF:
    # Constructor
    def __init__(self, corpus, tf = "raw", idf = "base", stopWord = "none", toStem = False, ignoreCase = True):
        self.corpus = corpus
        self.tf = tf
        self.idf = idf
        self.stopWord = stopWord
        self.toStem = toStem
        self.ignoreCase = ignoreCase
        #FIXME Professor recommends calculating all TF-IDF in the constructors
        #TF-IDF should be represented in a dictionary


    
    # Shared Methods
    def fileids(self):
        return self.corpus.fileids()
    
    def raw(self):
        return self.corpus.raw()
    
    def raw(self, fileids):
        return self.corpus.raw(fileids)
    
    def words(self):
        return self.corpus.words()
    
    def words(self, fileids):
        return self.corpus.words(fileids)
    
    # New Methods
    def tfidf(self, fileid, returnZero = False):
        # FIXME implement
        print('Temporary')
        #FIXME should return a dictionary
'''

    def tfidfAll(self, returnZero = False):
        #FIXME should return a dictionary of dictionaries

    def tfidfNew(self, [words]):


    def idf(self):


    def cosine_sim(self, [fileid1, fileid2]):


    def cosine_sim_new(self, [words], fileid):


    def query(self, [words]):
        # FIXME this is a bonus if you implement it

'''
