import math
from core.optimization.tokenizers.header_all_tokenizers import *
from core.text.constants import *
from libraries.tf_idf.common.constants import *
import pickle
import os
from os.path import dirname
from core.optimization.custom_hasher.header_hasher import *

cdef class Idf:

    cdef dict vocabulary
    cdef dict idf
    cdef object token_pattern
    cdef object hasher

    def __init__(self, vocabulary={}):
        self.vocabulary = vocabulary
        self.idf = dict()
        self.token_pattern = WordTokenizer(algo=ALGO_TYPE.SIMPLE, split_symbols=TOKENIZER_PARAMS.SPLIT_SYMBOLS)


    cpdef void load_idf(self, path_idf):
        if os.path.exists(dirname(path_idf)):
            with open(path_idf, 'rb') as f:
                self.idf = pickle.load(f)


    cpdef void save_idf(self, path_idf):
        if not os.path.exists(dirname(path_idf)):
            os.makedirs(dirname(path_idf))
        with open(path_idf, 'wb') as f:
            pickle.dump(self.idf, f)


    cpdef void preprocess_idf_terms(self, int corpus_len, min_count=20):
        cdef object word

        min_count = max(min_count, 1)

        for word in self.vocabulary:
            if self.vocabulary[word] >= min_count:
                self.idf[word] = math.log10(corpus_len / self.vocabulary[word])


    cpdef set __tokenize_data_set(self, object data):
        cdef set words = set()
        cdef object word
        cdef int check_len
        if isinstance(data, str):
            for word in self.token_pattern.tokenize(data.lower()):
                words.add(self.hasher.hash(word.data))
        elif isinstance(data, list):
            for word in data:
                words.add(word)
        return words


    cpdef void add_in_vocabulary(self, list corpus):
        cdef object token
        for token in self.__tokenize_data_set(corpus):
            try:
                self.vocabulary[token] += 1
            except:
                self.vocabulary[token] = 1


    def get_vocabulary(self):
        result = []
        if self.vocabulary:
            for key in self.vocabulary:
                result.append(self.hasher.unhash(key))
            return result
        elif self.idf:

            return self.idf.keys()
        else:
            return []


    def get_idf_dict(self):
        return self.idf


    def __getitem__(self, item):
        try:
            return self.idf[item]
        except:
            return 0


cdef class Tf:

    cdef object pattern

    def __init__(self):
        self.pattern = WordTokenizer(algo=ALGO_TYPE.SIMPLE, split_symbols=TOKENIZER_PARAMS.SPLIT_SYMBOLS)


    cpdef float calc(self, object term, object text):
        if isinstance(term, str) and isinstance(text, str):
            return text.count(term)/len(self.pattern.tokenize(text))
        elif isinstance(term, int) and isinstance(text, list):
            return text.count(term)/len(text)


cdef class Tfidf:

    cdef object idf
    cdef object tf

    def __init__(self, idf):
        if idf is None:
            raise Exception('idf is None')

        self.idf = idf
        self.tf = Tf()


    cpdef float calc(self, object term, object data):
        cdef float tf = self.tf.calc(term, data)
        cdef float idf = self.idf[term]
        return  tf*idf
