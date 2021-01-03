# This is a description of the inverted index
# We will store the inverted index as a dictionary
# Filling the index:
#  0. Read the files in a directory
#  1. Read one file, get all the lemmatized words
#  2. using the words as keys, and the add the file.name to the list of values
#     a. If there is already a list, we add the file to it
#     b. If there is no list, we create an empty list as value and then
#        add the file to it.
#  3. Repeat 1,2 until we have gone through all files.
#  4. Save the inverted index in a JSON file

from file import File
import spacy
import os
import json

INDEX_JSON_FILE = 'my_index.json'

processor = spacy.load("en_core_web_md")
inverted_index = {}

def save_index(my_index):
    json_text = json.dumps(my_index)
    try:
        with open(INDEX_JSON_FILE, "w", encoding="utf-8") as json_file:
            json_file.write(json_text)
    except IOError as e:
        print(e)


def add_to_index(lemma, file):
    if lemma in inverted_index.keys():
        value = inverted_index[lemma]
    else:
        value = []
        inverted_index[lemma] = value
    if file not in value:
        value.append(file)

def index_files():
    for filename in os.listdir('./files'):
        current_file = File(os.path.join('./files', filename))
        tokens = processor(current_file.content)
        for token in tokens:
            add_to_index(token.lemma_, filename)

    save_index(inverted_index)
