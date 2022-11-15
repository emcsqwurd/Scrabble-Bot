from matplotlib.widgets import LassoSelector
from pandas import Index
from sklearn import utils
from rack import Rack
from utils import Utils
from words import Words
import numpy as np
from dict import listEnglishWords


rackObj = Rack("hello", 3, ["h", "e", "l", "l", "o"], "well")
utilsObj = Utils(["h", "i"], [["h", "i"], ["g", "u", "y", "s"]], "hello", 5)
WL = ["well", "whats", "the", "yup"]
wordObj = Words(WL, 3, "e", "e", "e", 5)



"""Function to input a letter into every index of list of letters, and to return a LOL
of possible words from performing said action"""
def letterPlaceWord(string, letter):
    letterList = utilsObj.stringToList(string)
    BASE = []
    for item in letterList:
        BASE.append(item)
    indexList = []
    for i in range(0, len(BASE)):
        indexList.append(i)
    final = []
    for idx in indexList:
        BASE.insert(idx, letter)
        NEW = BASE[:]
        final.append(NEW)
        BASE.pop(idx)
    lastL = letterList[:]
    lastL.append(letter)
    final.append(lastL) 
    outputPoss = utilsObj.joinInternalLists(final)
    return outputPoss
#print(letterPlaceWord("ethan", "e"))

"""Function to check if any actual words are in the dictionary obtained from placing specified letter
at each index of input string"""
def checkEnglishLetterPos(string, letter):
    items = letterPlaceWord(string, letter)
    correct = []
    for ele in items:
        if ele in listEnglishWords():
            correct.append(ele)
    return correct 
#print(checkEnglishLetterPos("ethan", "e"))

"""Function to obtain list of all possibilities regarding placing a specified letter at every
index of every string obtained from all possible combinations and permutations of some
specified input string"""
def checkLetterPosALLCAP(string, letter): #string = RACK
    CAP = utilsObj.findAllPermAndComb(string)
    possEachWordList = []
    for item in CAP:
        checkLetterPos = letterPlaceWord(item, letter)
        possEachWordList.append(checkLetterPos)  
    outP = [item for sublist in possEachWordList for item in sublist] #LOL -> L of strings    
    return outP #LOL
#print(checkLetterPosALLCAP("the", "x"))    

"""Function to check if word from LCAP is allowed in scrabble, if True, appends to list (output
is list of allowed strings)"""
def checkEnglishWordsLetterPosALLCAP(string, letter): #string = RACK
    poss = checkLetterPosALLCAP(string, letter)
    correct = []
    for item in poss:
        if item in listEnglishWords():
            correct.append(item)
    return correct
#print(checkEnglishWordsLetterPosALLCAP("the", "y"))

"""Function to return LOLOL detailing the allowed words that are placeable on the board, using the words
that have already been placed on the board combined with the random string that the user has for the rack """
def findWordsToPlaceUsingBoardAndRack(wordList, rackString): #wordList = all words that have been played, rackString = randomString
    """Think then obtaining wordlist of all words that have been played at any given time (this can be 
    done by summing all the words in column from the score table)"""
    letter = []
    for word in wordList:
        let = utilsObj.stringToList(word)
        letter.append(let)
    final = []
    for idx in range(0, len(letter)):
        desiredLetList = letter[idx]
        possL = []
        for let in desiredLetList:
            poss = checkEnglishWordsLetterPosALLCAP(rackString, let)
            possL.append(poss)
        final.append(possL)
    outP = [item for sublist in final for item in sublist] #LOLOL -> LOL
    DONE = [item for sublist in outP for item in sublist] #LOL -> L
    return DONE
print(findWordsToPlaceUsingBoardAndRack(["hello", "hey", "yolo", "oscar", "running", "gang" ], "the"))



#IMPORTANT
"""Have to check, from the already possible english words resulting from placing the letter
at every index of word, from wordList of all possible combinations and permutations
ADDITIONALLY, have to check 

MAKE SURE TO FIX DICTIONARY SEARCH I.E IF WORD = LEN 3, THE ONLY SEARCH DICTIONARY UP TO WORDS OF LEN 3"""





#---------------------------------------MAY NOT BE NECCESSARY, DO CALCULATIONS --------------------------------------------

""""""
def findIfWordFromBoardMatchesRack(word, rackString):
    rackWords = rackObj.findALLWordsFromRandomString(rackString)
    print(rackWords)
    for idx1 in range(0, len(rackWords)):
        singleRackWord = rackWords[idx1]
        poss = []
        for let in utilsObj.stringToList(word):
            for idx2 in range(0, len(singleRackWord)):
                if let == singleRackWord[idx2]:
                    poss.append(singleRackWord)
    return poss
#print(findIfWordFromBoardMatchesRack("hello", "the"))



"""Function to find words from the words already played on the board, with the words that can be immediatly
formulated from the rack string, such that for each word on the board, if the letter in that word matches a letter
in the words immediatly obtained from the rack, it is added to the list, as technically (on blank scrabble board)
this word is placeable"""
def findWordsToPlaceBoardMatchingRack(wordList, rackString):
    rackWords = rackObj.findALLWordsFromRandomString(rackString) #List of Words obtained from Rack
    print("--------Rack Words")
    print(rackWords)
    listOfSWLetters = utilsObj.listOfStringsToListOfLetters(wordList)
    print("--------Scrabble Words in letters")
    print(listOfSWLetters)
    desiredWords = []
    for idxR in range(0, len(rackWords)):
        RW = rackWords[idxR]
        for idxL in range(0, len(RW)):
            letR = RW[idxL]
            print("-----Letters")
            print(letR)
            if letR in listOfSWLetters: #weirdddddddddddddnessssssssss
                desiredWords.append(True)
    print("------Desired Words")            
    return desiredWords
#print(findWordsToPlaceBoardMatchingRack(["hello", "hey"], "the"))      #FIX THE FUCK - PROPER WEIRDNESS



def findWordsToPlaceBoardMatchingRack(wordList, rackString):
    rackWords = rackObj.findALLWordsFromRandomString(rackString)
    print("------rack Words")
    print(rackWords)
    listOfSWLetters = utilsObj.listOfStringsToListOfLetters(wordList)
    print("------list of Scrabble board word letters")
    print(listOfSWLetters)
    desired = []
    for idxW in range(0, len(rackWords)):
        word = rackWords[idxW]

        for idxL in range(0, len(word)):
            let = word[idxL]
            if let in listOfSWLetters:
                desired.append(let)
    return desired
#print(findWordsToPlaceBoardMatchingRack(["hello", "hey"], "the"))    
#think if all letters of word are contained in letters list, then and only then append the word



""""""
def findWordsToPlaceBoardMatchingRackSortedIndex():
    return 
























