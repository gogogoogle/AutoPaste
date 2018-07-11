import re

def forTestFunction(fileName):
    fileType = re.search(r'\.[^\.]*$', fileName)
    print(fileType.group(0))

class FileContainer:
    def __init__(self, sourcePath, format=0):
        if (format == 0):
            fileType = re.search('\.[^\.]+$', sourcePath)
            print(fileType)
        self.filePath = sourcePath
        self.format   = format

    def openFile(self):
        self.content = open(self.filePath, "r")
        for line in self.content.readlines():
            print(line, end='')

    #def closeFile(self):

