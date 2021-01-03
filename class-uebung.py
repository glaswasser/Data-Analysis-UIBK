import os.path
import re

class File:

def __init__(self, path):
self.path = path
self.exists = os.path.isfile(self.path)
self.name = os.path.basename(self.path)

def isOfType(self, type):
path, ext = os.path.splitext(self.name)
return ext == '.' + type

# returns whether the File contains a match for the regex given as parameter
def contains(self, regex):
if not self.exists:
return False

with open(self.path, 'r') as file:
content = file.read()
return re.search(regex, content) is not None



###
import os.path
import re
from datetime import datetime

class File:

def __init__(self, path):
self.path = path
self.ID = path
self.name = os.path.basename(self.path)
self.lastModified = datetime.fromtimestamp(os.path.getmtime(self.path))
with open(self.path, 'r') as file:
self.content = file.read()


###

from File import File

file = File('./test.txt')

print(file.path)
print(file.ID)
print(file.lastModified)
print(file.content)

####
from datetime import datetime

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))


####
Class in Python

import os
from datetime import datetime

class File:

  def __init__(self, path):
    self.path = path
    self.ID = os.path.abspath(self.path)
    self.name = os.path.basename(self.path)
    self.lastModified = datetime.fromtimestamp(os.path.getmtime(self.path))
    self.size = os.stat(self.path).st_size # in byte
    with open(self.path, 'r') as file:
      self.content = file.read()
    self.length = len(self.content)
