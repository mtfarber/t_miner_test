import ds4se.facade as facade
import pandas as pd
import os
from collections import OrderedDict #allowed to import this?
import sys

os.chdir('../../')
sourcePath = os.getcwd() + sys.argv[1]
targetPath = os.getcwd()
targetList = open(os.getcwd() + sys.argv[2], 'r', encoding='latin1').read().splitlines()

for targetFilename in targetList:
    with open(os.path.join(targetPath, targetFilename), 'r', encoding='latin1') as f: # open in readonly mode
        targetData = f.read()
        f.close()
    values = {}
    for sourceFilename in os.listdir(sourcePath):
        with open(os.path.join(sourcePath,sourceFilename), 'r', encoding='latin1') as f:
            sourceData = f.read()
            f.close()
        result = facade.TraceLinkValue(sourceData,targetData,"word2vec",)
        # print("Source File: ",sourceFilename, "Target File: ", targetFilename, "Traceability: ",result)

    # new code added to keep track of/print just the four links with the highest traceability values
        values[result[1]] = sourceFilename
    final_four = sorted(values)
    final_four = final_four[len(final_four)-4:] 

    with open(os.getcwd() + sys.argv[3], 'w', encoding='latin1') as writeFile:
        for key in final_four:
            print("Source File: " + values[key] + ", Target File: " + targetFilename + ", Traceability: " + str(key) + '\n')
            writeFile.write("Source File: " + values[key] + ", Target File: " + targetFilename + ", Traceability: " + str(key) + '\n')