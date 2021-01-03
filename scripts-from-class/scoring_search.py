from searcher_with_positions import search_with_words
import math


# TF = Term count / Max Term-Count in the document
# Term count
def term_count_in_document(index, term, file):
    if term in index.keys():
        term_info = index[term]
        if file in term_info.keys():
            return len(term_info[file])
    return 0


# Max term count in document
def max_term_count_in_document(index, file):
    max_count = 0
    for term in index.keys():
        if file in index[term].keys():
            count = len(index[term][file])
            if max_count < count:
                max_count = count
    return max_count


# Calculate the normalized TF // Adapt this for other variants of TF
def normalized_tf(index, term, file):
    tf = term_count_in_document(index, term, file)
    max_term_count = max_term_count_in_document(index, file)
    return tf / max_term_count


# IDF = log(Total number of documents / number of documents with this term)
# Get the count of documents where the term shows up
def get_count_of_document_with_term(index, term):
    if term in index.keys():
        return len(index[term])
    else:
        return 0


# Get the total number of documents in the index
def count_documents(index):
    file_set = set()
    for word in index.keys():
        file_set.update(index[word].keys())
    return len(file_set)


# Calculate the IDF
def get_inverted_document_frequency(index, term):
    total_doc_count = count_documents(index)
    specific_doc_count = get_count_of_document_with_term(index, term)
    if specific_doc_count == 0:
        # Cannot find the term in index, so this is irrelevant
        return 0
    return math.log(total_doc_count / specific_doc_count)


# Calculate For a specific term and a file the tf*idf
def get_tfidf_for_term_and_file(index, term, file):
    n_tf = normalized_tf(index, term, file)
    idf = get_inverted_document_frequency(index, term)
    return n_tf * idf


def get_a_list_of_all_hits(search_result):
    file_set = set()
    for word in search_result.keys():
        set_now = search_result[word]
        if set_now is None:
            continue
        if len(file_set) == 0:
            file_set.update(set_now)
        else:
            file_set.update(file_set)
    return list(file_set)


# Perform search, rank the results, and give back the result with score
def search_and_score(index, query):
    search_result = search_with_words(index, query)
    document_to_be_scores = get_a_list_of_all_hits(search_result)
    _scoring = {}
    for file in document_to_be_scores:
        score = 0
        for word in search_result.keys():
            score += get_tfidf_for_term_and_file(index, word, file)
        _scoring[file] = score
    return dict(sorted(_scoring.items(), key=lambda item: item[1], reverse=True))

