# Tokenizer2 as FSM
# Inputs: Characters
# States: current word in editing, break_on_next_space
# Starting state: current word is empty
# Ending state: When there are no more characters.
# Transition rule:
#   1. When input is a word-character (alphanumeric), then add the character to the current-word buffer
#   2. If the current word is "St", then if the input is ".", we do not want break on the next space (set the
#      "break on next space" to false).
#   3. When input is a space and we do want to break on next space, flush out the buffer as a word
#   4. When input is a space and we do not want to break, then add the current character to current word, and set the
#      state "break on next space" to true again.
#   5. When there is no more character to be "eaten", then stop.



import re

class Tokenizer2:

    def flushout(self):
        if len(self.current_word) > 0:
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
        if self.is_alphanumeric(current_char): # 1. TR
            self.add_to_word_buffer(current_char)
        elif current_char == '.' and self.current_word == 'St': # 2. TR
            self.add_to_word_buffer(current_char)
            self.break_on_next_space = False
        elif not self.break_on_next_space and current_char == ' ': # 3. TR
            self.add_to_word_buffer(current_char)
            self.break_on_next_space = True
        else: # 4. TR
            self.flushout()
        self.character_position += 1
        self.eat()

    def tokenize(self):
        # do the tokenizing work
        self.eat()
        self.flushout()

    def get_tokenized_words(self):
        return self.tokenized_words

    def __init__(self, content):
        self.content = content
        self.tokenized_words = []
        self.current_word = ''
        self.character_position = 0
        self.break_on_next_space = True
        self.tokenize()


sentence = 'The second lock-down in St. Johann will be much more fun than the first one.'
# Result tokens should be: "The" "second" "lock-down" "in" "Austria" "will" "be" "much" more" "fun" "than" "the" "first" "one"

tokenizer = Tokenizer2(sentence)
print(tokenizer.tokenized_words)


sentence2 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam id dictum libero, non accumsan magna. Nulla a tellus sed diam dapibus efficitur. Nullam sit amet quam tincidunt, viverra tortor id, faucibus ante. Aenean nec malesuada turpis. Pellentesque sit amet placerat sapien. Nullam ligula velit, maximus et mauris quis, semper accumsan lectus. Suspendisse potenti. Aliquam erat volutpat. Nullam porttitor neque a suscipit porttitor.
Morbi elementum, urna ut elementum aliquam, nunc elit tempor nisi, quis pellentesque lorem velit rhoncus arcu. Nullam euismod, sem eget dictum posuere, leo dui tempus purus, vel egestas nisi erat et nibh. Sed finibus sapien ac metus blandit, eu ultricies ipsum facilisis. Donec iaculis posuere interdum. Donec nec est sit amet tellus rutrum scelerisque quis non tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur malesuada turpis sem, et maximus massa egestas eget. Ut vitae maximus nisi. Sed elementum, nibh semper rhoncus suscipit, ipsum dolor lacinia ligula, sed volutpat dui magna a magna. Donec ut massa in ante hendrerit rhoncus vitae a urna. Morbi vitae accumsan massa, a aliquam magna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum suscipit dolor a ligula malesuada, malesuada egestas lorem pretium. Curabitur sollicitudin ante non lectus volutpat, nec gravida ex bibendum. Pellentesque id ultricies augue.
Suspendisse a est vel elit interdum condimentum. Mauris scelerisque at nisl ac venenatis. Pellentesque tempor vulputate massa, sit amet dapibus elit congue tempus. Nullam metus purus, placerat ut pretium vitae, feugiat sed augue. Duis nec diam mi. Suspendisse quam massa, commodo eget elementum et, sodales et eros. Phasellus volutpat sapien auctor eros tristique tempor. Sed dignissim a enim nec feugiat. Vestibulum luctus odio nec leo rhoncus placerat. In dignissim mi odio, in porta libero sollicitudin non. Nam a maximus erat, at sodales nisi. Donec id dolor purus. Donec porta augue at rutrum vulputate. Integer vel diam id lacus dapibus varius. Vestibulum commodo sit amet lorem consequat commodo. Nunc id eleifend nibh.
Nullam posuere elit sodales sapien dictum pharetra. Suspendisse gravida mattis consectetur. Pellentesque vel nunc vitae nisl finibus finibus vitae egestas turpis. Duis augue nunc, molestie sed leo posuere, aliquam eleifend ligula. In a feugiat nibh. Morbi et nisi quis nibh ornare tristique sit amet non risus. Integer dolor purus, iaculis eu vehicula non, auctor id ipsum. Donec porta arcu in ligula feugiat, vitae ornare nibh suscipit. Quisque ultricies pellentesque neque ut venenatis. Vivamus at purus urna. Mauris eu nulla sed nulla tristique condimentum. In ipsum eros, interdum efficitur nisi a, venenatis elementum ante.
Nam dui arcu, rhoncus quis consectetur sit amet, placerat sit amet mauris. Etiam id dapibus nunc. Donec vel sodales leo. Sed ultrices commodo nulla, eget auctor ligula aliquet vitae. Curabitur erat ante, vulputate in eros ac, pretium interdum nisl. Aenean feugiat congue quam, sit amet viverra quam placerat et. Vestibulum vel feugiat tortor, vel ullamcorper augue. Proin et massa tincidunt, convallis sem eu, pharetra eros.
"""



# The following models a Tokenizer and its states
#
# copy it out in order to see it formatted
#
#      | read new character | <--- + ------ +
#               |                  |        |
#              ` ´                 |        |
# + -- | process character |       |        |
# |             |                  |        |
# |            ` ´                 |        |
# |    | add character to token buffer |    |
# |                                         |
# |                                         |
# + -> | spit out token, clear buffer |     |
#               |                           |
#              ` ´                          |
#      | check if character is terminating symbol |
#               |
#              ` ´
#      |     stop     |