import sys
import DocParse.LoadFileHandler as fileHandler

def MainRoutine():
    print('test')
    for input in sys.argv:
        print(input)
        fileHandler.forTestFunction(input)

MainRoutine()