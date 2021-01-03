# Searcher should perform a search
#  1. It should load the inverted index
#  2. It takes a search string
#  3. Look up in the index to get the list of documents
#     a. If there are multiple words, we will connect the query with "OR"
#     b. We can also implement a query using "AND"
#  4. Output those documents

import json
from my_index import INDEX_JSON_FILE, processor


def read_index():
    try:
        with open(INDEX_JSON_FILE, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except IOError:
        return {}

inverted_index = read_index()

def search(word):
    tokens = processor(word)
    # a: OR request
    lemmas = [token.lemma_ for token in processor(word)]
    files = set()
    for word in lemmas:
        if word in inverted_index.keys():
            for file in inverted_index[word]:
                files.add(file)
    return files

print(search("grand adventures"))
