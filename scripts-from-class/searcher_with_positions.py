# Searcher, check phrase, too

import indexer_with_positions


def perform_search(words, index):
    found_places = {}
    for i, word in enumerate(words):
        if word not in index:
            print(f"Cannot find {word}.")
            continue
        found_places[i] = index[word]
    if len(words) == 1:
        return found_places[0]
    places_with_all_hits = {}
    for document in found_places[0]:
        for position in found_places[0][document]:
            if in_all_document_with_position(document, position, found_places):
                if document not in places_with_all_hits:
                    places_with_all_hits[document] = []
                places_with_all_hits[document].append(position)
    return places_with_all_hits


def in_all_document_with_position(doc, position, found_places):
    for i, word in enumerate(found_places):
        expected_position = int(position) + i
        if doc not in found_places[i]:
            return False
        if expected_position not in found_places[i][doc]:
            return False
    return True


def search(phrase):
    words = list(map(lambda x: x.lemma_, indexer_with_positions.PROCESSOR(phrase)))
    index = indexer_with_positions.read_index()
    result = perform_search(words, index)
    return result


def search_with_words(index, phrase):
    words = list(map(lambda x: x.lemma_, indexer_with_positions.PROCESSOR(phrase)))
    result = {}
    for word in words:
        found = perform_search([word], index)
        result[word] = found
    return result
