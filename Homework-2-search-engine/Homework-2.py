# A program that does the follows:
# By passing a regular expression to the program, the program will search all files within a certain folder for matches.
# The program should print the matching files to the console.

import pandas as pd
import os

#### settings for myself
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.options.display.max_colwidth = 150
####

##### program #####
# string: the string that you look for
# directory: The directory of your files
# complete: show complete info (file name and text) [True], or only filename [False]

def lookup(string,
           directory = "/Users/alexanderheinz/Library/Mobile Documents/com~apple~CloudDocs/UIBK/Data Analysis 2/english_sentences/",
           complete = False):
    # get file names
    file_names = os.listdir(directory)
    # Create Dictionary for File Name and Text
    file_name_and_text = {}
    # make dataframe
    for file in file_names:
        with open(directory + file, "r") as target_file:
             file_name_and_text[file] = target_file.read()
    df = (pd.DataFrame.from_dict(file_name_and_text, orient = 'index')
                 .reset_index().rename(index = str, columns = {'index': 'file_name', 0: 'text'}))

    # look inside dataframe #
    if complete:
        result = df[df['text'].str.contains(string, case = False)]
    if not complete:
        result = df[df['text'].str.contains(string, case = False)]["file_name"].to_list()

    # what to print if there are no matches:
    if len(result) == 0:
        result = "no matches"
    return result



# example
print(lookup("Feel"))

print(lookup("blabla"))

print(lookup("Feel good", complete = True))


# example using RegEx
print(lookup("\s[Vv]isit[a-z]*"))

# all files with digits
print(lookup("\d"))


# user stories:
# story 1:
# A student wants to scan academic articles for certain keywords, and return only those containing e.g.
# the term "psychology", so then he will use the lookup() function to see in which documents that term appears

# story 2:
# A user has a lot of text files, but only some of them contain salary information from potential employers.
# So he uses the RegEx \d to find all documents that contain digits in his txt files.

# story 3:
# A teacher wants to see whether many students used the same sentence ("plagiarism") and would insert one sentence
# that he particularly finds suspicious to see in how many documents that exact sentence appears
