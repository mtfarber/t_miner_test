import ds4se.facade as facade
import os
import sys
import ast

def new_probability(num1, num2):   #written as a function to be more easily updated to a different algorithm later
    return (num1+num2)/2

os.chdir('../../')
sourcePath = os.getcwd() + sys.argv[1]
targetPath = os.getcwd()
targetList = open(os.getcwd() + sys.argv[2], 'r', encoding='latin1').read().splitlines()
outputThreshold = float(sys.argv[4]) 
print(sys.argv[5])
input = ast.literal_eval(sys.argv[5]) #the dictionary with (targetFile, sourceFile) -- a tuple -- as the key and the probability as the value
#dictionary to be filled later

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
        tmpStr = targetFilename+" "+sourceFilename
        if tmpStr in input:  #check if the file pair is in the input from the user
            result = new_probability(result, float(input[tmpStr]))  #recalculating the probability
        # print("Source File: ",sourceFilename, "Target File: ", targetFilename, "Traceability: ",result)

    # new code added to keep track of/print just the four links with the highest traceability values
        values[sourceFilename] = result[1]
    with open(os.getcwd() + sys.argv[3], 'w', encoding='latin1') as writeFile:
        for key in values:
            if (float(values[key]) >= outputThreshold):
                print("Source File: ",key, "Target File: ", targetFilename, "Traceability: ",values[key])
                writeFile.write("Source File: " + key + ", Target File: " + targetFilename + ", Traceability: " + str(values[key]) + '\n')
        writeFile.close()
