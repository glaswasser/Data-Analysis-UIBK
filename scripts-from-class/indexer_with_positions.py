# Indexer used to create indices with word positions


from file import File
import spacy
import json
import os


INDEX_JSON_FILE = 'index_with_position.json'

PROCESSOR = spacy.load('en_core_web_md')


def read_index():
    try:
        with open(INDEX_JSON_FILE) as json_file:
            return json.load(json_file)
    except IOError:
        return {}


def save_index(my_index):
    json_text = json.dumps(my_index)
    try:
        with open(INDEX_JSON_FILE, "w", encoding="utf-8") as json_file:
            json_file.write(json_text)
    except IOError as e:
        print(e)

# {
# word1 : {
#    fileId1: [5, 8, 10],
#    fileId2: [19, 28, 2006]
# },
# word2 ...
# }

def add_tokens_to_index(file_id, tokens, index):
    for position, token in enumerate(tokens):
        if token in index.keys():
            entry = index[token]
            if file_id not in entry.keys():
                entry[file_id] = []
        else:
            entry = {file_id: []}
        entry[file_id].append(position)
        index[token] = entry


def index_file_using_index(my_index, path_to_file):
    file = File(path_to_file)
    tokens = PROCESSOR(file.content)
    add_tokens_to_index(file.ID, map(lambda x: x.lemma_, tokens), my_index)


def index_file(path_to_file):
    my_index = read_index()
    index_file_using_index(my_index, path_to_file)
    save_index(my_index)


def index_directory(path_to_directory):
    my_index = read_index()
    for filename in os.listdir(path_to_directory):
        if not filename.endswith('.txt'):
            continue
        index_file_using_index(my_index, os.path.join(path_to_directory, filename))
    save_index(my_index)
