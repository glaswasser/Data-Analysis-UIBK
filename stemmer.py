#from file import File
import unicodedata
from tokenizer import Tokenizer
from nltk.stem import SnowballStemmer


file1 = open("files/s1.txt", r)

nfs1 = unicodedata.normalize("NFC", file1.content)

tokenized_words = Tokenizer(nfs1).tokenized_words
stemmer = SnowballStemmer("german")
for word in tokenized_words:
    print(stemmer.stem(word))


