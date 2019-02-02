#!usr/bin/env python3

# Importing Packages
import os
from utils import *
import sys
import json

class DialogueManager():
    def __init__(self):
        # Intent classification - English
        self.intent_classifier_en = unpickle_file('intentClassifierEN')
        self.intent_classifier_fr = unpickle_file('intentClassifierFR')
        self.tfidf_vectorizer = unpickle_file('tfidfVectorizer')

    def intentClassifierEN(self, request):
        # Find the intent of request.
        preprocessed_request = text_prepare(request) 
        print(preprocessed_request)
        features = self.tfidf_vectorizer.transform([preprocessed_request]) 
        print(features)
        intent = self.intent_classifier_en.predict(features)[0] 
        print(intent)
        return intent

    def intentClassifierFR(self, request):
        # Find the intent of request.
        preprocessed_request = text_prepare(request) 
        print(preprocessed_request)
        features = self.tfidf_vectorizer.transform([preprocessed_request]) 
        print(features)
        intent = self.intent_classifier_fr.predict(features)[0] 
        print(intent)
        return intent

if __name__ == "__main__":
    request = sys.argv[1]
    DM = DialogueManager()
    DM.intentClassifierEN(request)

