import re

def forTestFunction(fileName):
    print(fileName)
    fileType = re.search(r'\.[^\.]*$', fileName)
    print(fileType.group(0))
'''==============================================================================
class: FileContainer
function:
Declare a class object to keep a file parsing record in memory.
The purse of declare an object is to prevent file size too large, and is hard to load the whole file at once.

==============================================================================s'''
class FileContainer:
    def __init__(self, sourcePath, format=0):
        if (format == 0):
            fileType = re.search('\.[^\.]+$', sourcePath)
        self.filePath = sourcePath
        self.format   = format

    def openFile(self):
        self.content = open(self.filePath, "r")
        for line in self.content.readlines():
            print(line, end='')

    #def closeFile(self):

