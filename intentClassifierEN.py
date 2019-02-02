#!usr/bin/env python3

# Importing Packages
from utils import *
import numpy as np
import pandas as pd
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class Model():

    # Initializer / Instance Attributes
    def __init__(self):
        pass

    def tfidf_features(self, X_train, X_test):
        """ Performs TF-IDF transformation and dumps the model. """
        
        # Train a vectorizer on X_train data.
        # Transform X_train and X_test data.
        
        tfidf_vectorizer_en = TfidfVectorizer(ngram_range=(1, 2), max_df=0.9, min_df=5, token_pattern ='(\S+)')
        
        X_train = tfidf_vectorizer_en.fit_transform(X_train)
        X_test = tfidf_vectorizer_en.transform(X_test)
        
        with open('tfidfvectorizeren', 'wb') as f:
            pickle.dump(tfidf_vectorizer_en, f)
        
        return X_train, X_test

    def train_model(self):

        # sample_size = 6171

        # dialogue_df = pd.read_csv('data/dialogues.tsv', sep='\t').sample(sample_size, random_state = 0)
        cbc_task_df = pd.read_csv('data/cbc_tasks_en.tsv', sep='\t')

        # dialogue_df.head()
        # cbc_task_df.head()

        # dialogue_df['text'] = dialogue_df['text'].apply(lambda x: text_prepare(x)) 
        cbc_task_df['text'] =  cbc_task_df['text'].apply(lambda x: text_prepare_en(x)) 

        # X = np.concatenate([dialogue_df['text'].values, cbc_task_df['text'].values])
        X = np.concatenate([cbc_task_df['text'].values])
        # y = ['dialogue'] * dialogue_df.shape[0] + ['Task'] * cbc_task_df.shape[0]
        y = (cbc_task_df['tag'].values).tolist()
       
        # y = ['dialogue'] * dialogue_df.shape[0] + (cbc_task_df['tag'].values).tolist()
        # print(X)
        # print(y)
        # print(len(X))
        # print(len(y))

        X_train, X_test, y_train, y_test =  train_test_split(X, y, train_size = 0.9, random_state = 0) 
        print('Train size = {}, test size = {}'.format(len(X_train), len(X_test)))

        X_train_tfidf, X_test_tfidf = self.tfidf_features(X_train, X_test)
        # print(X_train_tfidf)
        # print(X_test_tfidf)

        intent_classifier = LogisticRegression(penalty = 'l2', C = 10, random_state = 0, multi_class = 'multinomial', solver = 'newton-cg')
        intent_classifier.fit(X_train_tfidf, y_train)

        # Check test accuracy.
        y_test_pred = intent_classifier.predict(X_test_tfidf)
        print(y_test_pred)
        test_accuracy = accuracy_score(y_test, y_test_pred)
        print('Test accuracy = {}'.format(test_accuracy))

        pickle.dump(intent_classifier, open('intentClassifierEN', 'wb'))

if __name__ == "__main__":
    model = Model()
    model.train_model()    
    

    