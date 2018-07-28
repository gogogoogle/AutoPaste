import sys
import DocParse.LoadFileHandler as fileHandler


def MainRoutine():
    print('test')
    container = fileHandler.FileContainer(sys.argv[1])
    container.openFile()
    '''
    for input in sys.argv:
        print(input)
        fileHandler.forTestFunction(input)
    '''
MainRoutine()