import os

class Path(str):
    def __init__(self, path):
        self.path = path
        
    def dirname(self):
        return Path(os.path.dirname(self))

    @property
    def ext(self):
        return os.path.splitext(self.path)[-1]
        
    @property
    def name(self):
        return os.path.splitext(os.path.split(self.path)[-1])[0]
	
# s = Path("/Users/thibh/Documents/test.txt")
# print(s.dirname().dirname())
# print(s.name)
# print(s.ext)