#You can also find an extensive and larger English word list here http://www.wordgamedictionary.com/english-word-list/download/english.txt

from lib2to3.pytree import LeafPattern
from scrabbledict import letterScoreDict
from utils import Utils
import numpy as np


utilsObj = Utils(["h", "i"], [["h", "i"], ["g", "u", "y", "s"]], "hello", 5)


class Func:

    def __init__(self, matrix, row, column, result, string, listOfCoords) -> None:
        self.self = self
        self.matrix = matrix #1 - matrix
        self.row = row #2 - Integer
        self.column = column #3 - Integer
        self.result = result #4 - String Letter
        self.string = string #5 - String
        self.listOfCoords = listOfCoords #6 - listOfLists for coords
        return 

    """Function to represent Scrabble Board as 15x15 Matrix"""
    def scrabbleMatrix(self):
        scrabbleBMatrix = np.zeros((15,15))
        return scrabbleBMatrix  #returns 15x15 scrabble board matrix representation

    """Function to find the value of a given position on the board"""
    def findPositionValue(self, matrix, row, column):
        letterPosition = matrix[row, column]
        return letterPosition #returns the value of the position rowxcolumn input on board
    
    """Function to place letter at given x,y coordinate"""
    def placeValuePosition(self, matrix, row, column, result):
        matrix[row, column] = result
        return matrix  #allows for the assignment of input value for specified position

    """Function to triple the amount of points when letter lands"""
    def tripleLetter(self, inputMatrix, row, column):
        inputMatrix[row, column] = 3*inputMatrix[row, column]
        return inputMatrix #allows to triple any designated rowxcolumn element of the scrabble board matrix

    """Function to return the score of a triple letter tile acting on a letter"""
    def triplL(self, letter):
        letVal = letterScoreDict[letter]
        final = 3*letVal
        return final

    """Function to double the amount of points when letter lands"""
    def doubleLetter(self, inputMatrix, row, column):
        inputMatrix[row, column] = 2*inputMatrix[row, column]
        return inputMatrix #allows to double any designated rowxcolumn element of the scrabble board matrix

    """Function to return the score of a double letter tile acting on a letter"""
    def doubleL(self, letter):
        letVal = letterScoreDict[letter]
        final = 2*letVal
        return final

    """Function to return list of values corresponding to the letters within the input string"""
    def valuesOfWord(self, string):
        charList = []
        for char in string:
            charList.append(char)
        valueList = []    
        for item in charList:
            charValue = letterScoreDict[item]
            valueList.append(charValue)
        return valueList

    """Function to determine total value of input string"""
    def totalValueOfWord(self, string):
        valuesList = Func.valuesOfWord(self, string)
        total = sum(valuesList)
        return total

    """Function to double the value of input word"""
    def doubleWord(self, string):
        stringValue = Func.totalValueOfWord(self, string)
        newValue = 2*stringValue
        return newValue

    """Function to triple the value of input word"""
    def tripleWord(self, string):
        stringValue = Func.totalValueOfWord(self, string)
        newValue = 3*stringValue
        return newValue

    """Function to call when letters and values are required from input string"""
    def lettersAndValuesWord(self, string):
        listLetters = utilsObj.stringToList(string)
        listValues = Func.valuesOfWord(self, string)
        return listLetters, listValues    

    """Function to enter location of word onto board, enter both location of letters on board
    and the string itself being entered"""
    def enterWordValues(self, matrix, listOfCoords, string): #listOfCoords = locations of letters on board, string = input word
        if len(string) != len(listOfCoords):
            raise TypeError("Location length and Word length do not match.  Please double check inputs.")
        #matrix = Func.scrabbleMatrix(self)
        letterValues = Func.valuesOfWord(self, string)
        for value in range(len(letterValues)):
            pair = listOfCoords[value]
            row = pair[0] 
            column = pair[1]
            result = letterValues[value] 
            board = Func.placeValuePosition(self, matrix, row, column, result)
        return board  #example arg = [[3,4], [3,5], [3,6], [3,7], [3,8]], "hello"



testMat = np.zeros((15,15))
testCoord = [[3,4], [3,5], [3,6], [3,7], [3,8]]
funcObj = Func(testMat, 3, 2, "h", "hello", testCoord)
#print(funcObj.enterWordValues(testCoord, "hello"))










