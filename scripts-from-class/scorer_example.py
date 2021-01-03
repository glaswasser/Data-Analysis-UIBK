from indexer_with_positions import index_directory, read_index
from scoring_search import search_and_score


DIRECTORY = './sentences'


# index_directory(DIRECTORY)

index = read_index()

result = search_and_score(index, "say without")

for file in result.keys():
    print(file, '   ', result[file])
