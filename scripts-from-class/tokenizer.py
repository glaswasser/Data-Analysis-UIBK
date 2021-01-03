# Tokenizer as FSM
# Inputs: Characters
# States: current word in editing.
# Starting state: current word is empty
# Ending state: When there are no more characters.
# Transition rule:
#   1. When input is a word-character (alphanumeric), then add the character to the current-word buffer
#   2. When input is not a word-character, the flush out the buffer as a word
#   3. When there is no more character to be "eaten", then stop.

import re

class Tokenizer:

    def flushout(self):
        self.tokenized_words.append(self.current_word)
        self.current_word = ''

    def add_to_word_buffer(self, character):
        self.current_word += character

    def is_alphanumeric(self, character):
        return re.match("\\w|\\d|-", character)

    def eat(self):
        if self.character_position >= len(self.content):
            return
        current_char = self.content[self.character_position]
        if self.is_alphanumeric(current_char):
            self.add_to_word_buffer(current_char)
        else:
            self.flushout()
        self.character_position += 1
        self.eat()

    def tokenize(self):
        # do the tokenizing work
        self.eat()

    def get_tokenized_words(self):
        return self.tokenized_words

    def __init__(self, content):
        self.content = content
        self.tokenized_words = []
        self.current_word = ''
        self.character_position = 0
        self.tokenize()
