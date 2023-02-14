import nltk.corpus
import math
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

        #TF
        raw_idf_count = { }
        all_tf = { }
        numFiles = 0
        for fileid in self.corpus.fileids(): #iterate through each document
            numFiles += 1
            raw_tf_count = { } #FIXME eventually need to implement log term frequency
            for word in self.corpus.words(fileid): #finds tf for each document
                if word not in raw_tf_count:
                    raw_tf_count[word] = 1
                elif word in raw_tf_count:
                    raw_tf_count[word] += 1

                if word not in raw_idf_count: #if first instance of word across all documents
                    raw_idf_count[word] = [fileid]
                elif word in raw_idf_count and fileid not in raw_idf_count[word]: #if first instance of word in current document
                    raw_idf_count[word].append(fileid)
        
            all_tf[fileid] = raw_tf_count
            #print(fileid, raw_tf_count)
        
        idf_count = { }
        for word in raw_idf_count:
            idf_count[word] = math.log2(numFiles / len(raw_idf_count[word]))

        tf_idf = { } #tf-idf for each document in the corpus
        for fileid in all_tf:
            tf_idf[fileid] = { }
            for word in all_tf[fileid]:
                tf_idf[fileid][word] = all_tf[fileid][word] * idf_count[word]

        self.tf_idf = tf_idf
        self.idf = idf_count
        #FIXME do I need to save the tf???

        #print('Here')
        #print('Number of idf:', len(idf_count))

    
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
        print('Type 2', type(self.tf_idf[fileid]))
        return self.tf_idf[fileid]
        #FIXME should return a dictionary
        #FIXME need to implement returnZero
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
