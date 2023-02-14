import nltk.corpus
import math
import numpy as np
from numpy.linalg import norm

#FIXME take a look at Plaintext Corpus Reader (?)

class CorpusReader_TFIDF:
    # Constructor
    def __init__(self, corpus, tf = "raw", idf = "base", stopWord = "none", toStem = False, ignoreCase = True):
        #FIXME what should happen if non-supported parameters are given?? like tf = "random"
        self.corpus = corpus
        self.tf = tf
        self.idf = idf
        self.stopWord = stopWord
        self.toStem = toStem
        self.ignoreCase = ignoreCase
        #FIXME Professor recommends calculating all TF-IDF in the constructors
        #TF-IDF should be represented in a dictionary

        allWords = [ ] #Every word that appears in the corpus
        for fileid in self.corpus.fileids():
            for word in self.corpus.words(fileid):
                if word not in allWords:
                    allWords.append(word)
        #TF
        raw_idf_count = { }
        all_tf = { }
        numFiles = 0
        for fileid in self.corpus.fileids(): #iterate through each document
            numFiles += 1
            raw_tf_count = { } #FIXME eventually need to implement log term frequency

            for word in allWords: #Ensures every dictionary is in the same order
                raw_tf_count[word] = 0

            for word in self.corpus.words(fileid): #finds tf for each document
                if word in raw_tf_count:
                    raw_tf_count[word] += 1

                if word not in raw_idf_count: #if first instance of word across all documents
                    raw_idf_count[word] = [fileid]
                elif word in raw_idf_count and fileid not in raw_idf_count[word]: #if first instance of word in current document
                    raw_idf_count[word].append(fileid)
        
            if tf == "log": #Applies log normalization if requested
                for word in allWords:
                    if raw_tf_count[word] > 0:
                        raw_tf_count[word] = 1 + math.log2(raw_tf_count[word])

            all_tf[fileid] = raw_tf_count
        

        idf_count = { }
        for word in raw_idf_count:
            idf_count[word] = math.log2(numFiles / len(raw_idf_count[word]))

        tf_idf = { } #tf-idf for each document in the corpus (without terms that have 0 value)
        tf_idf_with_zeros = { } #tf-idf for each document in the corpus (with terms that have 0 value)
        for fileid in all_tf:
            tf_idf[fileid] = { }
            tf_idf_with_zeros[fileid] = { }
            for word in all_tf[fileid]:
                value = all_tf[fileid][word] * idf_count[word] #calculating tf-idf
                if value > 0: #only add if not 0
                    tf_idf[fileid][word] = value
                tf_idf_with_zeros[fileid][word] = value
                

        self.tf_idf = tf_idf
        self.tf_idf_with_zeros = tf_idf_with_zeros
        self.idf_count = idf_count
        #FIXME do I need to save the tf???

    
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
        if returnZero:
            return self.tf_idf_with_zeros[fileid]
        else:
            return self.tf_idf[fileid]
        #FIXME should return a dictionary
        #FIXME need to implement returnZero


    def tfidfAll(self, returnZero = False):
        if returnZero:
            return self.tf_idf_with_zeros
        else:
            return self.tf_idf
        #FIXME should return a dictionary of dictionaries
        #FIXME need to implement returnZero


    def tfidfNew(self, words): #FIXME need to implement different tf type, etc.
        #FIXME do I need to include values with 0??
        raw_tf_count = { }
        allWords = [ ] #holds each unique word
        for word in words:
            if word not in raw_tf_count:
                raw_tf_count[word] = 1
                allWords.append(word)
            elif word in raw_tf_count:
                raw_tf_count[word] += 1

        if self.tf == "log": #Applies log normalization if requested
            for word in allWords:
                if raw_tf_count[word] > 0: #FIXME this if statement is redundant (I think)
                    raw_tf_count[word] = 1 + math.log2(raw_tf_count[word])


        new_tf_idf = { }
        for word in raw_tf_count:
            new_tf_idf = raw_tf_count[word] * self.idf_count[word]

        return new_tf_idf


    def idf(self):
        return self.idf_count


    def cosine_sim(self, fileid1, fileid2):
        A = np.array(list(self.tf_idf_with_zeros[fileid1].values()))
        B = np.array(list(self.tf_idf_with_zeros[fileid2].values()))
        return np.dot(A,B)/(norm(A)*norm(B))

    ''' FIXME this is an example
        # define two lists or array
        A = np.array([2,1,2,3,2,9])
        B = np.array([3,4,2,4,5,5])
        
        print("A:", A)
        print("B:", B)
        
        # compute cosine similarity
        cosine = np.dot(A,B)/(norm(A)*norm(B))
        print("Cosine Similarity:", cosine)
    '''
'''

    def cosine_sim_new(self, [words], fileid):


    def query(self, [words]):
        # FIXME this is a bonus if you implement it

'''
