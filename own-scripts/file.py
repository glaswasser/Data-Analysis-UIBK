import os
from datetime import datetime


class File:

    def __init__(self, path):
        self.path = path
        self.ID = os.path.abspath(self.path)
        self.name = os.path.basename(self.path)
        self.lastModified = datetime.fromtimestamp(os.path.getmtime(self.path))
        self.size = os.stat(self.path).st_size  # in byte
        with open(self.path, 'r') as file:
            self.content = file.read()
            self.filesize = os.path.getsize(self.path)
        self.length = len(self.content)
