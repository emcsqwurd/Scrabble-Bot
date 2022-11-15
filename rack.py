from csv import list_dialects
import itertools
from random import random
import numpy as np
from utils import Utils
from words import Words
from func import Func
from itertools import permutations
from scrabbledict import letterScoreDict, letterScoreDictInvert
#from func import lettersAndValuesWord, valuesOfWord, totalValueOfWord
from dict import listEnglishWords
#from words import findMaxValueWORDFromWordList
from tabulate import tabulate



utilsObj = Utils(["h", "i"], [["h", "i"], ["g", "u", "y", "s"]], "hello", 5)
wordsObj = Words(["well", "whats", "the", "yup"], 3, "e", "e", "e", 5)

testMat = np.zeros((15,15))
testCoord = [[3,4], [3,5], [3,6], [3,7], [3,8]]
funcObj = Func(testMat, 3, 2, "h", "hello", testCoord)



class Rack:

    def __init__(self, randomString, desiredLengthOfWord, rack, wordInside) -> None:
        self.randomString = randomString #1 - String 
        self.desiredLengthOfWord = desiredLengthOfWord #2 - Integer
        self.rack = rack #3 - List
        self.wordInside = wordInside #4 - String
        return 

    """"Function to obtain all possible permutations (values) for given input string"""
    def findAllPermutationsWordInValues(self, randomString):
        valueList = funcObj.valuesOfWord(randomString)    
        permutationList = list(itertools.permutations(valueList))
        return permutationList

    """Function to return all possible permutations of random input string"""
    def findAllPermutationsWord(self, randomString):
        listLetters = utilsObj.stringToList(randomString)
        permLists = list(itertools.permutations(listLetters))
        return permLists    

    """Function to find allowed word from random string of letter"""
    """DOUBLE CHECK listEnglishWords() func !!!"""
    def findSameLengthWordFromRandomString(self, randomString):
        if len(randomString) > 7:
            raise TypeError("This amount of tiles is not possible for the rack.  Please ensure the word entered is correct.")
        permLists = Rack.findAllPermutationsWord(self, randomString)
        listOfPerms = utilsObj.joinInternalLists(permLists)
        possibilities = []
        for word in listOfPerms:
            if str(word) in listEnglishWords():
                possibilities.append(word)
        finalL = list(set(possibilities)) #gets rid of any duplicates
        """IMPORTANT
        optimize - only search words in dict that contain same no. characters as input string (shortn iteration length)"""
        return finalL #quite slow function, see if can be optimised  

    """Function to find all permutations AND combinations from a random input string"""
    def findALLWordsFromRandomString(self, randomString):
        listCombination = []
        listLetters = utilsObj.stringToList(randomString)
        for letter in range(len(listLetters) + 1):
            for subset in itertools.combinations(listLetters, letter):
                compositeLists = list(subset)
                listCombination.append(compositeLists)
        for listSet in listCombination:
            if len(listSet) == 0: #empty list not required
                listCombination.remove(listSet) 
        newListCombination = utilsObj.joinInternalLists(listCombination)
        orderPermList = []
        for listOrderWord in newListCombination:
            perms = Rack.findAllPermutationsWord(self, listOrderWord)
            orderPermList.append(perms)
        newOrderPermList = []
        for thing in orderPermList:
            if len(thing) >= 2: #single letters => no ordering/permutations
                newOrderPermList.append(thing)
        tupleList = []
        for setOfTuples in newOrderPermList:
            for tuple in setOfTuples:
                joinedTuple = utilsObj.joinInternalLists(tuple)
                tupleList.append(joinedTuple)
        newTupleList = utilsObj.joinInternalLists(tupleList)
        desiredWords = []
        for guess in newTupleList:
            if guess in listEnglishWords():
                desiredWords.append(guess)
        return desiredWords

    """Function to return the word of the highest value immediatly possible from the random string of the rack"""
    def findHighestValueWordFromRack(self, randomString):
        wordsFromRackList = Rack.findALLWordsFromRandomString(self, randomString)
        maxValueWord = wordsObj.findMaxValueWORDFromWordList(wordsFromRackList)
        return maxValueWord

    """Function to return the words possible from rack of specified length"""
    def findSpecifiedLengthWordsFromRandomString(self, randomstring, desiredLengthOfWord):
        wordsFromRackList = Rack.findALLWordsFromRandomString(self, randomstring)
        desiredLengthWords = []
        for word in wordsFromRackList:
            if len(word) == desiredLengthOfWord:
                desiredLengthWords.append(word)
        return desiredLengthWords    

    """Function to be utilized when a blank tile is included from the random pickup of tiles from the bag.
    This function will return a list of lists, such that each list includes the possible words for the blank
    tile corresponding to a->z.  If Blank Tile is obtained, enter as !"""
    def findALLWordsFromRandomStringBlankTileIncluded(self, randomString): #randomString includes ! symbol (check dict)
        possChoices = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        if "!" in randomString:
            listOfStrings = []
            for letter in possChoices:
                newStrings = randomString.replace("!", letter)
                listOfStrings.append(newStrings)
            listOfLists = []    
            for word in listOfStrings:
                desiredOutputs = Rack.findALLWordsFromRandomString(self, word)
                listOfLists.append(desiredOutputs)
        else:
            raise TypeError("Blank Tile has not been input in string. Please Check string / function.")        
        return listOfLists

    """Function to return the max value word from rack when the blank tile is included"""
    def findHighestValueWordFromRackIncludingBlankTile(self, randomString): #randomString includes ! symbol (check dict)
        wordsFromRackListIncludingBlank = Rack.findALLWordsFromRandomStringBlankTileIncluded(self, randomString) #listOfLists
        maxValueWords = []
        for wordList in wordsFromRackListIncludingBlank:
            highestWord = wordsObj.findMaxValueWORDFromWordList(wordList)
            maxValueWords.append(highestWord)
        topWord = wordsObj.findMaxValueWORDFromWordList(maxValueWords)    
        return topWord

    """Function to remove the word used in the previous round from the current rack.  The rack input argument
    must be a list of the letters contained within the rack"""
    def updateRackTakeAway(self, rack, wordTakeAway): 
        #rack = string made into list of Letters, wordTakeAway = string that is wished to be removed from rack
        rackL = utilsObj.stringToList(rack)
        for letter in wordTakeAway:
            if letter in rackL:
                rackL.remove(letter)
        finalString = utilsObj.listOfLettersToString(rackL)
        return finalString  #string

    """Function to add the selected word string to the rack that have been chosen at random from the bag.
    The rack argument must be a list of letters"""
    def updateRackAdd(self, rack, wordAdd):
        #rack = string made into list of letters, wordAdd = string of letters to be added to rack
        finalRack = []
        listLetters = utilsObj.stringToList(wordAdd)
        rackL = utilsObj.stringToList(rack)
        for char1 in listLetters:
            finalRack.append(char1)
        for char1 in rackL:
            finalRack.append(char1)    
        finalString = utilsObj.listOfLettersToString(finalRack)    
        return finalString   #string

    """Function to display the random 7 letter rack string as a table"""
    def rackTable(self, string):
        letList = utilsObj.stringToList(string)
        data = [letList]
        outP = tabulate(data)
        return outP


rackObj = Rack("hello", 3, ["h", "e", "l", "l", "o"], "well")
print(rackObj.updateRackAdd("hellopo", "opo"))





