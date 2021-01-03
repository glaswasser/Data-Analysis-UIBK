import nltk
from nltk.tokenize import NLTKWordTokenizer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

tokenizer = NLTKWordTokenizer()
sentence = """
Deputy minister Hoa said that after this first pilot project, the training programme will be enlarged to include around 1,000 students who were looking to work abroad.
"""
lemmatizer = WordNetLemmatizer()
words = tokenizer.tokenize(sentence)
# POS-Tagging
pos_tagged = nltk.pos_tag(words)

#print(pos_tagged)

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def my_lemmatize(word, tag):
    my_tag = get_wordnet_pos(tag)
    if my_tag is not None:
        return lemmatizer.lemmatize(word, my_tag)
    else:
        return word


for word, tag in pos_tagged:
    print(word + " --> " + my_lemmatize(word, tag))
