import sys

class LoadData():

    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.file.close()

    def __iter__(self):
        return self

    def next(self):
        line = self.file.readline()

        if line == None or line == "":
            raise StopIteration

        return line


with LoadData(sys.stdin) as f:
    for line in f:
        print f

#with LoadData(open('tmpfile') as f:
#    for line in f:
#
#         print f