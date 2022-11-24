import ds4se.facade as facade
import pandas as pd
import os
from collections import OrderedDict #allowed to import this?
import sys


os.chdir('../../')
sourcePath = os.getcwd() + sys.argv[1]
targetPath = os.getcwd()
targetList = open(os.getcwd() + sys.argv[2], 'r', encoding='latin1').read().splitlines()
outputThreshold = float(sys.argv[4]) 

for targetFilename in targetList:
    with open(os.path.join(targetPath, targetFilename), 'r', encoding='latin1') as f: # open in readonly mode
        targetData = f.read()
        f.close()
    values = {}
    for sourceFilename in os.listdir(sourcePath):
        with open(os.path.join(sourcePath,sourceFilename), 'r', encoding='latin1') as f:
            sourceData = f.read()
            f.close()
        result = facade.TraceLinkValue(sourceData,targetData,"word2vec")

    # new code added to keep track of/print just the four links with the highest traceability values
        values[result[1]] = sourceFilename
    final_out = sorted(values)
    key=0
    with open(os.getcwd() + sys.argv[3], 'w', encoding='latin1') as writeFile:
      while float(final_out[key]) >= outputThreshold and key < len(final_out):
          print("Source File: ",values[final_out[key]], "Target File: ", targetFilename, "Traceability: ",final_out[key])
          writeFile.write("Source File: " + values[final_out[key]] + ", Target File: " + targetFilename + ", Traceability: " + final_out[key] + '\n')
          key+=1
      writeFile.close()
