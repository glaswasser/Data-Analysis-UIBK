# install.packages("SnowballC")

library(SnowballC)

# Write a reusable R script:
# Read file content and get other “properties” of a file
# Stem the content of a given file (see above) using the Snowball English Stemming algorithm
# The result should be a list of stemmed words.


# get function for this. Just run the function without an argument and select a file yourself :)

get_properties <- function(filepath) {
  # ID: Absolute Path of the file
  filepath <- file.choose()
  
  # get file info:
  file_info <- file.info(filepath)
  
  # Content: the content of the file
  content <- paste(readLines(filepath), collapse = " ")
  
  # Name: The name of the file
  filename <- basename(filepath)
  
  # lastModified: Last Modified Date#
  last_modified <- file_info$mtime
  
  # filesize: file size
  file_size <- file_info$size
  
  # print the output
  print(paste("Filepath: ", filepath))
  print(paste("Filename: ", filename))
  print(paste("Last modified: ", last_modified))
  print(paste("File Size: ", file_size, " Byte"))

  print(paste("Content: \"", content, "\""))
  
  # now tokenize the content
  word_tokens <- unlist(strsplit(content, split = " "))
  
  # and get the stems:
  stems <- wordStem(word_tokens, language = "en")
  
  print("Stems list:")
  print(list(stems))
}

get_properties()