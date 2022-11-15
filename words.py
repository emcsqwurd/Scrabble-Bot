#from func import totalValueOfWord
from func import Func
import numpy as np

testMat = np.zeros((15,15))
testCoord = [[3,4], [3,5], [3,6], [3,7], [3,8]]
funcObj = Func(testMat, 3, 2, "h", "hello", testCoord)


class Words:

    def __init__(self, wordList, lengthOfWord, startOfWord, endOfWord, desiredLetter, desiredIndex) -> None:
        self.wordList = wordList #1 - List of strings
        self.lengthOfWord = lengthOfWord #2 - Integer
        self.startOfWord = startOfWord #3 - String (letter)
        self.endOfWord = endOfWord #4 - String (letter)
        self.desiredLetter = desiredLetter #5 - String (letter)
        self.desiredIndex = desiredIndex #6 - Integer
        return 

    """Function """
    def findWordOfGivenLength(self): #PREVIOUS -> arg = wordList, lengthOfWord
        return 

    """Function that returns the max value from a given list of words"""
    def findMaxValueFromWordList(self, wordList): #PREVIOUS -> arg = wordList
        outL = []
        for word in wordList:
            value = funcObj.totalValueOfWord(word)
            outL.append(value)
        maxValueWord = max(outL)    
        return maxValueWord

    """Function that returns the max value word from a given list of words"""
    def findMaxValueWORDFromWordList(self, wordList):  #PREVIOUS -> arg = wordList
        outL = []
        for word in self.wordList:
            value = funcObj.totalValueOfWord(word)
            outL.append(value)
        maxValue = max(outL)
        pos = outL.index(maxValue)
        return wordList[pos]

    """Function that obtains list of words of desired length from an input list of words"""
    def findSpecifiedLengthWord(self, wordList, lengthOfWord):  #PREVIOUS -> arg = wordList, lengthOfWord
        lengthWordsList = []
        for word in wordList:
            length = len(word)
            lengthWordsList.append(length)     
        if lengthOfWord not in lengthWordsList:
            raise ValueError("No words in list have this length.")      
        outL = []    
        for length in range(len(lengthWordsList)):
            if lengthWordsList[length] == lengthOfWord:
                outL.append(length)    
        finalL = []
        for indexValue in outL:
            desiredWords = wordList[indexValue]
            finalL.append(desiredWords) 
        return finalL

    """Function to find word beginning with certain letter"""
    def findWordStartLetter(self, wordList, startOfWord):  #PREVIOUS -> arg = wordList, startOfWord
        desiredWordList = []
        for word in wordList:
            if startOfWord == word[0]:
                desiredWordList.append(word)
        if len(desiredWordList) == 0:
            raise TypeError("No words from input word list begin with this letter.")
        return desiredWordList

    """Function to return the word ending for specified letter"""
    def findWordEndLetter(self, wordList, endOfWord):  #PREVIOUS -> arg = wordList, endOfWord
        desiredWordList = []
        for word in wordList:
            if endOfWord == word[-1]:
                desiredWordList.append(word)
        return desiredWordList

    """FIX - works but if len(word) in wordlist is less than the index specified, will fail"""
    """Function to return word that contains specified letters, as long as correct index is also specified"""
    def findWordContainingLetterSpecifiedIndex(self, wordList, desiredLetter, desiredIndex):  #PREVIOUS -> arg = wordList, desiredLetter, desiredIndex
        desiredIndex = desiredIndex - 1
        desiredWordList = []
        for word in wordList:
            if len(word) < desiredIndex:
                list(wordList).remove(word)        
            if desiredLetter == word[desiredIndex]:
                desiredWordList.append(word)   
        print(wordList)             
        return desiredWordList

    """"""
    def findTop10ValueWordsFromWordList(slef, wordList):
        top10Words = []
        valueList = []
        for word in wordList:
            value = funcObj.totalValueOfWord(word)
            valueList.append(value)
        return 

    """"""
    def findTop10ValuesOfWordsFromWordList():
        return     




WL = ["well", "whats", "the", "yup"]
wordObj = Words(WL, 3, "e", "e", "e", 5)
#print(wordObj.findWordEndLetter(WL, "s"))


