import re
def forTestFunction(fileName):
    fileType = re.findall(r'\.[^\.]*$', fileName)
    print(fileType)