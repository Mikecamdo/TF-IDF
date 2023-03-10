import nltk.corpus
import math
import numpy as np
from numpy.linalg import norm
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

class CorpusReader_TFIDF:
    # Constructor
    def __init__(self, corpus, tf = "raw", Idf = "base", stopWord = "none", toStem = False, ignoreCase = True):
        #Making sure parameters have valid values
        if type(corpus) != nltk.corpus.util.LazyCorpusLoader and type(corpus) != nltk.corpus.reader.plaintext.PlaintextCorpusReader:
            raise ValueError("corpus must be a valid NLTK corpus object")
        if tf != "raw" and tf != "log":
            raise ValueError("tf must have a value of 'raw' or 'log'")
        if Idf != "base" and Idf != "smooth":
            raise ValueError("idf must have a value of 'base' or 'smooth'")
        if type(stopWord) != str:
            raise ValueError("stopWord must have a value of 'none', 'standard', or a filename where stopwords are to be read")
        if toStem != True and toStem != False:
            raise ValueError("toStem must have a value of True or False")
        if ignoreCase != True and ignoreCase != False:
            raise ValueError("ignoreCase must have a value of True or False")
        
        #Set Values
        self.corpus = corpus
        self.tf = tf
        self.Idf = Idf
        self.stopWord = stopWord
        self.toStem = toStem
        self.ignoreCase = ignoreCase

        #TF-IDF should be represented in a dictionary
        stops = [ ] #leave empty if stopWord == "none"
        if stopWord == "standard": #standard nltk stopwords
            stops = set(stopwords.words('english'))
        elif stopWord != "none": #if stopWord == fileName (that contains a list of stop words)
            with open(stopWord, 'r') as file: #open stopword file
                for line in file:
                    for word in line.split():
                        stops.append(word) #add each word from the stopword file

        stemmer = SnowballStemmer('english') #stemmer
        allWords = [ ] #Every word that appears in the corpus
        for fileid in self.corpus.fileids(): #loops through all documents in the corpus
            for word in self.corpus.words(fileid):
                if toStem: #if toStem == true
                    word = stemmer.stem(word)
                
                if ignoreCase: #if ignoreCase == true
                    word = word.lower()

                if word not in allWords and word not in stops: #adds every word in the corpus to allWords
                    allWords.append(word)
        #TF
        raw_idf_count = { } #counts number of documents that each word appears in
        all_tf = { } #holds every document's tf values
        numFiles = 0
        for fileid in self.corpus.fileids(): #iterate through each document
            numFiles += 1
            raw_tf_count = { } #each individual document's tf values

            for word in allWords: #Ensures every dictionary is in the same order
                raw_tf_count[word] = 0

            for word in self.corpus.words(fileid): #finds tf for each document
                if toStem: #if toStem == true
                    word = stemmer.stem(word)

                if ignoreCase: #if ignoreCase == true
                    word = word.lower()

                raw_tf_count[word] += 1

                if word not in raw_idf_count and word not in stops: #if first instance of word across all documents
                    raw_idf_count[word] = [fileid]
                elif word in raw_idf_count and fileid not in raw_idf_count[word]: #if first instance of word in current document
                    raw_idf_count[word].append(fileid)
        
            if tf == "log": #Applies log normalization if requested
                for word in allWords:
                    if raw_tf_count[word] > 0:
                        raw_tf_count[word] = 1 + math.log2(raw_tf_count[word])

            all_tf[fileid] = raw_tf_count #add document's tf values to all_tf
        

        idf_count = { } 
        for word in raw_idf_count: #calculates idf for each word in the corpus
            if Idf == "smooth": #inverse frequency smoothed
                idf_count[word] = math.log2(1 + (numFiles / len(raw_idf_count[word])))
            else: #if idf == "base"
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
                
        #Set values
        self.tf_idf = tf_idf
        self.tf_idf_with_zeros = tf_idf_with_zeros
        self.idf_count = idf_count
        self.stops = stops
    
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
        if type(fileid) == list: #if the fileid is passed in a list
            if returnZero:
                return self.tf_idf_with_zeros[fileid[0]]
            else:
                return self.tf_idf[fileid[0]]
        else: #if the fileid is passes as a string
            if returnZero:
                return self.tf_idf_with_zeros[fileid]
            else:
                return self.tf_idf[fileid]

    def tfidfAll(self, returnZero = False):
        if returnZero:
            return self.tf_idf_with_zeros
        else:
            return self.tf_idf

    def tfidfNew(self, words):
        raw_tf_count = { }
        allWords = [ ] #holds each unique word
        stemmer = SnowballStemmer('english')
        for word in words: #loops through every word in the new "document"
            if self.toStem:
                word = stemmer.stem(word)

            if self.ignoreCase:
                word = word.lower()

            if word not in raw_tf_count and word not in self.stops:
                raw_tf_count[word] = 1
                allWords.append(word)
            elif word in raw_tf_count:
                raw_tf_count[word] += 1

        if self.tf == "log": #Applies log normalization if requested
            for word in allWords:
                if raw_tf_count[word] > 0:
                    raw_tf_count[word] = 1 + math.log2(raw_tf_count[word])

        new_tf_idf = { }
        for word in raw_tf_count: #calculating the new TF-IDF values
            if word in self.idf_count.keys(): #if the word appears in the original corpus (if it doesn't, we ignore it)
                new_tf_idf[word] = raw_tf_count[word] * self.idf_count[word]

        return new_tf_idf


    def idf(self):
        return self.idf_count


    def cosine_sim(self, fileid1, fileid2):
        A = np.array(list(self.tf_idf_with_zeros[fileid1].values()))
        B = np.array(list(self.tf_idf_with_zeros[fileid2].values()))
        bottom = norm(A)*norm(B)
        if bottom == 0:
            return 0
        else:
            return np.dot(A,B)/bottom

    def cosine_sim_new(self, words, fileid):
        A = self.tfidfNew(words)
        A_words = list(A.keys())

        if type(fileid) == list:
            B = self.tf_idf_with_zeros[fileid[0]]
        else:
            B = self.tf_idf_with_zeros[fileid]
        sum = 0
        for word in B: #Finding the dot product
            if word in A_words: #If word is not in A_words, then its value is 0 (and thus we add nothing)
                sum += A[word] * B[word]
        
        C = np.array(list(A.values()))
        D = np.array(list(B.values()))

        bottom = norm(C)*norm(D)
        if bottom == 0:
            return 0
        else:
            return sum/bottom

    def query(self, words):
        results = [ ]
        for fileid in self.tf_idf_with_zeros:
            cosine = self.cosine_sim_new(words, fileid)
            results.append((fileid, cosine))

        results.sort(reverse=True, key=lambda a: a[1]) #sorts in descending order

        return results