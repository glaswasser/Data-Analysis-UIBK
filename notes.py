
# get folder path
folderpath = "/Users/alexanderheinz/Library/Mobile Documents/com~apple~CloudDocs/UIBK/Data Analysis 2/english_sentences/"

# get complete file paths:
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

# init data for dataframe
data = {}
# get data content
for file in filepaths:
    with open(file, "r") \
        as f:
        data[file] = (f.readlines())

# store in dataframe
df = pd.DataFrame.from_dict(data)

print(df)

#df = pd.DataFrame(data.items(), columns = ["filepath", "content"])

# get short filename
#df["filename"] = os.listdir(folderpath)


#print(str(df["content"]))

#test = df[df['content'].str.contains('feel')]
#print(test)
