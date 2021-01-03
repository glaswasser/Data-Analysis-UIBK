import spacy

processor = spacy.load("en_core_web_md")

sentence = """
Deputy minister Hoa said that after this first pilot project, the training programme will be enlarged to include around 1,000 students who were looking to work abroad.
"""

tokens = processor(sentence)

for token in tokens:
    print(token.lemma_)

