import os
import spacy
from file import File
import json

processor = spacy.load("en_core_web_md")

# the file to be written
INDEX_JSON_FILE = 'my_index.json'

inverted_index = {}

# 3.
def save_index(my_index):
    json_text = json.dumps(my_index)
    try:
        # write json file with content
        with open(INDEX_JSON_FILE, "w", encoding = "utf-8") as json_file:
            json_file.write(json_text)
    except IOError as e:
        print(e)



# 2.
def add_to_index(lemma, file):
    # if the lemma is inside the inverted index,
    # the value will be the index of the lemma (file name?)
    if lemma in inverted_index:
        value = inverted_index[lemma]
    # if it is not in the inverted index yet, we will create an entry:
    else:
        value = []
        inverted_index[lemma] = value
    # if the file is not yet in the values, we will add it.
    if file not in value:
        value.append(file)


# 1.
def index_files():
    for filename in os.listdir("./own-scripts/sentences"):
        # the files
        current_file = File(os.path.join("./own-scripts/sentences", filename))
        # add each file content in the tokens via processor (processed via spacy)
        tokens = processor(current_file.content)
        # using the above function, add each token and lemmatize it
        for token in tokens:
            add_to_index(token.lemma_, filename)

# run index_files
index_files()
# print the inverted index:
print(inverted_index)


save_index(inverted_index)
