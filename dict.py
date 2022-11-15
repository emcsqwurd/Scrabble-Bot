import numpy as np
from utils import Utils



"""Function to read document containing all possible allowed scrabble words"""
def readDoc(txtFile):
    doc = open(txtFile, 'r') #open text document
    with doc as file:
        text = file.read().rstrip()
    doc.close()
    return text
#print(readDoc("dict.txt"))


"""FIX"""
"""Function to return list of all words contained in given input txt File"""
def txtFileToList(txtFile):
    file = open(txtFile, 'r')
    #yourResult = [line.split(',') for line in file.readlines()]
    data = file.read()
    #print(data)
    listData = data.split("\n")
    file.close()
    return listData
#print(txtFileToList("dict.txt"))


"""Function to output all possible english words allowed in scrabble"""
def listEnglishWords():
    txtFile = "dict.txt"
    listOfWords = txtFileToList(txtFile)
    return listOfWords
#print(listEnglishWords())



"""Function to obtain words of specified length from Dictionary"""
def getSpecifiedLengthWordFromDict(desiredLengthWord):
    dictWords = listEnglishWords()
    desiredWords = []
    for lengthWordIndex in range(len(dictWords)):
        if len(dictWords[lengthWordIndex]) == desiredLengthWord:
            desiredWords.append(dictWords[lengthWordIndex])
    return desiredWords
#print(getSpecifiedLengthWordFromDict(3))



"""FIX -- NOT WORKING"""
def sortDictByLengthOfWord():
    lengthList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    finalListOfLists = []
    for getIndexOfLength in range(len(lengthList)):
        for word in listEnglishWords():
            if lengthList[getIndexOfLength] == len(word):
                groupList = []
                groupList.append(word)
                finalListOfLists.append(groupList)
    print(len(finalListOfLists))
    return finalListOfLists #just creates 
#print(sortDictByLengthOfWord())















