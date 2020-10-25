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
# output: show complete info (file name and text) [complete], or only filename [filename]

def lookup(string,
           directory = "/Users/alexanderheinz/Library/Mobile Documents/com~apple~CloudDocs/UIBK/Data Analysis 2/english_sentences/",
           output = "filename"):
    # get file names
    file_names = os.listdir(directory)
    # Create Dictionary for File Name and Text
    file_name_and_text = {}
    # make dataframe
    for file in file_names:
        with open(directory + file, "r") as target_file:
             file_name_and_text[file] = target_file.read()
    df = (pd.DataFrame.from_dict(file_name_and_text, orient='index')
                 .reset_index().rename(index = str, columns = {'index': 'file_name', 0: 'text'}))

    # look inside dataframe #
    if output == "complete":
        result = df[df['text'].str.contains(string)]
    if output == "filename":
        result = df[df['text'].str.contains(string)]["file_name"].to_list()

    # what to print if there are no matches:
    if len(result) == 0:
        result = "no matches"
    return result



# example
print(lookup("feel"))
print(lookup("blabla"))
