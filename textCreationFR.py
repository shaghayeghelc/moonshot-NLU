#!usr/bin/env python3

# Importing Packages
import csv
import os

class TextCreationFR:
    ''' The following class is creating some french textual data and label them in order to use for AI modelling purposes'''
    def __init__(self):
        pass
    
    def textcreator(self):

        # Create the folder to save the textual data
        if not os.path.exists('data'):
            os.makedirs('data')
        cbc_tasks_file = "data/cbc_tasks_fr.tsv"

        tasks = {}

        sentence = ["", "Je cherche", "Je voudrais", "J'aimerais", "Je veux", "Je veux lire", "Je voudrais lire", "puis-je lire", \
            "pourrais-je lire", "puis-je avoir", "pourrais-je avoir", "pouvez-vous m'envoyer", "Qu'est qui se passe", \
            "Qu'est qui se arrive", "Qu'elles sont"]

        content = ["l'information", "information", "les nouvelles", "nouvelles", "les nouvelles locales", "nouvelles locales", "locales"\
                   "les nouvelles du monde", "nouvelles du monde", "l'actualité internationale", "actualité internationale"]
           
        with open(cbc_tasks_file, 'wt') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(['text', 'tag'])
            for word_i in sentence:
                for word_j in content:
                    a = word_i + " " + word_j
                    if word_j in ["l'information", "information", "les nouvelles", "nouvelles"]:
                        tag = 'top 5 stories'
                    elif word_j in ["les nouvelles du monde", "nouvelles du monde", "l'actualité internationale", "actualité internationale"]:
                        tag = 'international news'
                    else: 
                        tag = 'local news'
                    writer.writerow([a, tag])

if __name__ == "__main__":
    TextCreationFR = TextCreationFR()
    TextCreationFR.textcreator()