#!usr/bin/env python3

# Importing Packages
import nltk
import pickle
import re
import numpy as np
# nltk.download('stopwords')
nltk.download('stopwords', download_dir='/opt/python/current/app')
nltk.data.path.append('/opt/python/current/app')
from nltk.corpus import stopwords

def text_prepare(text):
    """ Tokenization- Preprocessing """
    
    replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
    bad_symbols_re = re.compile('[^0-9a-z #+_]')
    stopwords_set = set(stopwords.words('english'))

    text = text.lower()
    text = replace_by_space_re.sub(' ', text)
    text = bad_symbols_re.sub('', text)
    text = ' '.join([x for x in text.split() if x and x not in stopwords_set])

    return text.strip()

def load_embeddings(embeddings_path):
    
    embeddings = dict()
    for line in open(embeddings_path, encoding = 'utf-8'):
        row = line.strip().split('\t')
        embeddings[row[0]] = np.array(row[1:], dtype = np.float32)
    embeddings_dim = embeddings[list(embeddings)[0]].shape[0]
    
    return embeddings, embeddings_dim
    
def question_to_vec(question, embeddings, dim):
    """ Transforms a string to an embedding. """
    
    vec = []
    for word in question.split():
        if word in embeddings:
            vec.append(embeddings[word])
    if vec == []:
        return np.zeros(dim)
    result = np.array(vec).mean(axis=0)
    return result

def unpickle_file(filename):
    """ unpickling the file."""

    with open(filename, 'rb') as f:
        return pickle.load(f)
