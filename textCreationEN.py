#!usr/bin/env python3

# Importing Packages
import csv
import os

class TextCreationEN:
    ''' The following class is creating some english textual data and label them in order to use for AI modelling purposes'''
    def __init__(self):
        pass
    
    def textcreator(self):

        # Create the folder to save the textual data
        if not os.path.exists('data'):
            os.makedirs('data')
        cbc_tasks_file = "data/cbc_tasks_en.tsv"

        tasks = {}

        sentence = ["", "I'm looking for", "I look for", "I want", "I would like", "Can I have some", "Could I have some", \
                    "I want some", "I like some", "I would like some", "I want to read", "I would like to read", "Can I read some", \
                    "Could I read some", "Please give me some", "Please send me some", "Could you give me some", "Can you give me some", \
                    "Can you send me some", "Could you send me some", "Could I read", "Please give me", "Please send me", "Could you give me",\
                    "Can you give me", "Can you send me", "Could you send me", "What is happening in the", "what is going on in the"]

        content = ['news', 'top 5 stories', 'local news', 'locally', 'world', 'in the world', 'international news', \
                    'sport', 'top stories of sport', 'sports', 'radio', 'radio one', 'live radio', 'music', 'musics', 'radio two', 'live music', \
                    'podcasts']

        with open(cbc_tasks_file, 'wt') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(['text', 'tag'])
            for word_i in sentence:
                for word_j in content:
                    a = word_i + " " + word_j
                    if word_j in ['news', 'top 5 stories']:
                        tag = 'news-top-stories'
                    elif word_j in ['world', 'international new', 'in the world']:
                        tag = 'news-international'
                    elif word_j in ['sport', 'top stories of sport', 'sports']:
                        tag = 'sports-top-stories'
                    elif word_j in ['radio', 'radio one', 'live radio']:
                        tag = 'radio-live'
                    elif word_j in [ 'music', 'musics', 'radio two', 'live music']:
                        tag = 'music-live'
                    elif word_j in ['podcasts']:
                        tag = 'podcasts'
                    else: 
                        tag = 'news-local'
                    writer.writerow([a, tag])

if __name__ == "__main__":
    TextCreationEN = TextCreationEN()
    TextCreationEN.textcreator()
    





