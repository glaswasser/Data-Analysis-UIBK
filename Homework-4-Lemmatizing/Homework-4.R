if (!require("pacman")) install.packages("pacman")
if (!require("readtext")) install.packages("readtext")
if (!require("tidyverse")) install.packages("tidyverse")
if (!require("tidytext")) install.packages("tidytext")
if (!require("udpipe")) install.packages("tidytext")


library(udpipe)
library(pacman)
pacman::p_load_gh("trinker/textstem")
library(readtext)
library(tidytext)
library(tidyverse)


# place texts.zip inside same directory as the current script - then run the following:
current_working_dir <- dirname(rstudioapi::getActiveDocumentContext()$path)
setwd(current_working_dir)

# read texts from zip
texts <- readtext("texts.zip")


### USING TEXTSTEM (see https://cran.r-project.org/web/packages/textstem/README.html for a tutorial)

## lemmatize strings using DEFAULT lemma dictionary:
texts$text[1] <- lemmatize_strings(texts$text[1])
texts$text[2] <- lemmatize_strings(texts$text[2])
texts$text[3] <- lemmatize_strings(texts$text[3])

# tokenize texts
texts_tokenized <- texts %>% unnest_tokens(token, text) %>% count(token, doc_id)

# check for diversity
diversity_default <- texts_tokenized %>% 
  group_by(doc_id) %>% 
  summarize(distinct_words = n_distinct(token))

diversity_default
# oscar wilde is the winner

diversity_default %>% 
  ggplot(aes(x = doc_id, y = distinct_words, fill = doc_id)) +
  geom_col()

# we can get the most frequent lemmas
# (not sure if this works right, though, as only twain seems to use "but":
texts_tokenized %>% 
  group_by(doc_id) %>% 
  top_n(20, wt = n) %>% 
  group_by(token) %>% 
  mutate(n_total = sum(n)) %>% 
  ggplot(aes(x = fct_reorder(factor(token), n_total), y = n, fill = doc_id)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  xlab("lemmas") +
  ylab("lemma count")



## lemmatize strings using koRpus dictionary and treetagger program:

texts <- readtext("texts.zip")

lemma_dictionary_hs <- make_lemma_dictionary(texts$text[1], engine = 'hunspell')

# get lemmatized texts:
texts$text[1] <- lemmatize_strings(texts$text[1], dictionary = lemma_dictionary_hs)
texts$text[2] <- lemmatize_strings(texts$text[2], dictionary = lemma_dictionary_hs)
texts$text[3] <- lemmatize_strings(texts$text[3], dictionary = lemma_dictionary_hs)


# tokenize lemmatize text:
texts_tokenized <- texts %>% unnest_tokens(token, text) %>% count(token, doc_id)

# check for diversity
diversity_hunspell <- texts_tokenized %>% 
  group_by(doc_id) %>% 
  summarize(distinct_words = n_distinct(token))

diversity_hunspell

# again, oscar wilde is the winner, but there are differences in the lemmas
# twain and wilde have about 1000 more distinct tokens.
# again, we can visualize this:
diversity_hunspell %>% 
  ggplot(aes(x = doc_id, y = distinct_words, fill = doc_id)) +
  geom_col()


texts_tokenized %>% 
  group_by(doc_id) %>% 
  top_n(20, wt = n) %>% 
  group_by(token) %>% 
  mutate(n_total = sum(n)) %>% 
  ggplot(aes(x = fct_reorder(factor(token), n_total), y = n, fill = doc_id)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  xlab("lemmas") +
  ylab("lemma count")



#### USING UDPIPE

texts <- readtext("texts.zip")

# This takes a minute to download the english dictionary
doyle_lemmas <- udpipe(x = texts$text[1],
            object = "english")

# it creates a whole dataframe with lemmas, sentences, tokens etc.
head(doyle_lemmas)

# number of unique lemmas at doyle:
n_doyle <- doyle_lemmas$lemma %>% 
  n_distinct()

##
# twain lemmas
twain_lemmas <- udpipe(x = texts$text[2],
                       object = "english")

# number of unique lemmas at twain:
n_twain <- twain_lemmas$lemma %>% 
  n_distinct()

##
# wilde lemmas
wilde_lemmas <- udpipe(x = texts$text[3],
                       object = "english")

# number of unique lemmas at wilde:
n_wilde <- wilde_lemmas$lemma %>% 
  n_distinct()


## visualize this:
# pre-process dataframes:
authors <- c("Doyle", "Twain", "Wilde")
diversity_udpipe <- data.frame(doc_id = authors,
                               distinct_words = c(n_doyle, n_twain, n_wilde),
                               library = "udpipe")

diversity_default <- diversity_default %>% add_column("library" = "default")
diversity_default$doc_id <- authors

diversity_hunspell <- diversity_hunspell %>% add_column("library" = "hunspell")
diversity_hunspell$doc_id <- authors

# combine dataframes
diversity_comb <- rbind(diversity_default, diversity_hunspell, diversity_udpipe)

# create plots
diversity_comb %>% 
  ggplot(aes(x = doc_id, y = distinct_words, fill = library)) +
  geom_col(position = "dodge") +
  xlab("Author") +
  ylab("distinct lemmas")

diversity_comb %>% 
  ggplot(aes(x = library, y = distinct_words, fill = doc_id)) +
  geom_col(position = "dodge") +
  xlab("Library") +
  ylab("Distinct lemmas") +
  scale_fill_discrete(name = "Author")


# another library to test - might add this next week, too tired now :(
#library(tm)
#tm::stemDocument(x$lemma)



