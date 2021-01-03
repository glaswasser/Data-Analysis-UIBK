from file import File
import re
import unicodedata

file1 = File("files/s1.txt")
file2 = File("files/s2.txt")

print(f"file1: {file1.content} / {file1.length} / {file1.filesize}")
print(f"file2: {file2.content} / {file2.length} / {file2.filesize}")

nfs1 = unicodedata.normalize("NFD", file1.content)
nfs2 = unicodedata.normalize("NFD", file2.content)

print(f"nfs1: {nfs1} has {len(nfs1)} characters")
print(f"nfs2: {nfs2} has {len(nfs2)} characters")

print(f"nfs1 has Ähnlichkeit: {re.search('Ähnlichkeit', nfs1)}")

without_diacritics = re.sub("[\u0300-\u036f]", "", nfs1)

print(f"Now without diacritics: {without_diacritics}" )
