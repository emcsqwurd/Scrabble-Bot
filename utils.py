from typing import List
from matplotlib import testing
import numpy as np
import itertools
import time

class Utils:

    def __init__(self, List, listOfLists, string, integer) -> None:
        self.List = List #1 - List 
        self.listOfLists = listOfLists #2 - listOfLists
        self.string = string #3 - String
        self.integer = integer #4 - Integer
        return 

    """Function to return a string from an input list of letters""" 
    def listOfLettersToString(self, listOfLetters):
        new = ""
        for let in listOfLetters:
            new += let
        return new 

    """Function to join elements of internal lists"""
    def joinInternalLists(self, listOfLists): #PREVIOUS -> arg = listOfLists
        finalList = []
        for lists in listOfLists:
            finalTerms = "".join(lists)
            finalList.append(finalTerms)
        return finalList

    """Function to convert input string to list of letters"""
    def stringToList(self, string):
        letterList = []
        for letter in string:
            letterList.append(letter)
        return letterList  

    """Function to return list of lengths of each item for some input list"""
    def findLengthsOfItemsInList(self, List):
        lenList = []
        for item in List:
            lengthValue = len(item)
            lenList.append(lengthValue)
        return lenList

    """Function to find all the Combinations of an input string"""
    def findAllCombinations(self, string):
        combin = []
        listLetters = Utils.stringToList(self, string)
        for letter in range(len(listLetters) + 1):
            for subset in itertools.combinations(listLetters, letter):
                    compositeLists = list(subset)
                    combin.append(compositeLists)
        for com in combin:
            if len(com) == 0:
                combin.remove(com)            
        return combin

    """Function to find all the Permutations of an input string"""
    def findAllPermutations(self, string):
        listLetters = Utils.stringToList(self, string)
        permLists = list(itertools.permutations(listLetters))
        return permLists

    """FIX"""
    """Function to find all the Combinations and Permutations of an input string"""
    def findAllPermAndComb(self, string):
        comb = Utils.findAllCombinations(self, string)
        combNew = []
        for item in comb:
            if len(item) >= 2: #FIX - MUST INCLUDE ALL LENGTH ITEMS - NOT CORRECT TO USE THINK!!!!!
                combNew.append(item)       
        combUPD8 = Utils.joinInternalLists(self, combNew)        
        outL = []
        for possW in combUPD8:
            final = Utils.findAllPermutations(self, possW)
            outL.append(final)
        finalL = []
        for CAP in outL:
            new = Utils.joinInternalLists(self, CAP)
            finalL.append(new) 
        outPutL = []
        for listW in finalL:
            for str in listW:
                outPutL.append(str)
        return outPutL
    
    """Function to return list of letters for each string in list of strings"""
    def listOfStringsToListOfLetters(self, listOfStrings):
        letList = []
        for string in listOfStrings:
            letters = Utils.stringToList(self, string)
            for let in letters:
                letList.append(let)
        return letList

    """Function to utilise when wishing to delete specified elements of a list by giving their indices"""
    def deleteMultipleElement(self, list_object, indices): #list_object = list, indicies = list
        indices = sorted(indices, reverse=True)
        for idx in indices:
            if idx < len(list_object):
                list_object.pop(idx)
        return       

    """Function to return the specified number of largest items from list"""
    def getSpecifiedMaxValuesFromList(self, list, N):
        result_list = []
        for i in range(0, N): 
            maximum = 0
            for j in range(len(list)):     
                if list[j] > maximum:
                    maximum = list[j]      
            list.remove(maximum)
            result_list.append(maximum)
        return result_list

    """Function that prints formatted string showing execution time of 
    the function object that is passed through"""
    def timerPrint(self, func):
        def wrap_func(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            print(f'Function {func.__name__!r} executed in {(t2-t1):.10f}s') # displays execution time to 10 d.p
            return result
        return wrap_func

    """Function that returns float - the execution time of the function object
    that is passed through"""
    def timerFloat(self, func):
        def wrap_func(*args, **kwargs)->float:
            t1 = time()
            func(*args, **kwargs)
            t2 = time()
            return (t2-t1)
        return wrap_func
            
        
        
        
        


        

testListOfLists = [["h", "i"], ["g", "u", "y", "s"]]
testList = [1,2,3,4,5,6]
utilObj = Utils(testList, testListOfLists, "hello", 3)
yup = utilObj.findAllPermAndComb("the")
#print(yup)
#print(len(yup))



