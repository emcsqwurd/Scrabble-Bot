from msilib import Table
import numpy as np
#from func import totalValueOfWord
from tabulate import tabulate
from utils import Utils
from scoretable import ScoreTable




utilsObj = Utils(["h", "i"], [["h", "i"], ["g", "u", "y", "s"]], "hello", 5)
testTable = [["hi","(3,4), (3,4)",40, 0,3], ["hi","(3,4), (3,4)",40, 0,3], ["hi","(3,4), (3,4)",40, 0,3]]
scoreTableObj = ScoreTable(testTable, "hi", "(3,4), (3,5)", 9 )


class Board:

    def __init__(self, LOLBoard, table, row, column, desiredInputLetter, locationOfString, inputWord) -> None:
        self.LOLBoard = LOLBoard #1 - LOL used to represent scrabble board
        self.table = table #2 - LOL
        self.row = row #3 - Integer
        self.column = column #4 - Integer
        self.desiredInputLetter = desiredInputLetter #5 - String Letter 
        self.locationOfString = locationOfString #6 - LOL
        self.inputWord = inputWord #7 - String
        return 

    """Function that returns list containing 15 lists filled with zeros"""
    def dataTable(self):
        data = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        return data
 
    """Function that converts a LOLBoard into a table to present"""
    def scrabbleTableOutput(self, LOLBoard):
        dataTable = tabulate(LOLBoard)
        return dataTable
    #print(scrabbleTableOutput())

    """Function to change the desired index of the data table used to display the scrabble board with current words contained"""
    def changeElementOfDataTable(self, table, row, column, desiredInputLetter):
        desiredRow = table[row - 1]
        desiredRow[column - 1] = desiredInputLetter
        return table
    #print(changeElementOfDataTable(dataTable(),7,2,"h"))

    """Function to enter the input word onto the scrabble table, as long as LOLBoard for locations is also input"""
    def enterWordOnTable(self, table, locationOfString, inputWord): #locationOfString = LOL
        if len(inputWord) != len(locationOfString):
            raise TypeError("Input string and locations for string do not match.  Check input data.")
        inputWordList = utilsObj.stringToList(inputWord)
        for value in range(len(inputWordList)):
            pair = locationOfString[value]
            row = pair[0]
            column = pair[1]
            letter = inputWordList[value]
            table = Board.changeElementOfDataTable(self, table, row, column, letter)
        """IMPORTANT - Check extra points file for clarification
        if len(inputWord) == 7:
            tableOP = scoreTableObj.scoreTableUpdateOtherPlayer()
            tablePU = scoreTableObj.scoreTableUpdateProgramUser()"""
        return table
    #print(enterWordOnTable([[3,4], [3,5], [3,6], [3,7], [3,8]], "hello"))    

    """Function to replace a string on the board back to original 0's for each location of letter"""
    def removeWordFromTable(self, table, locationOfString):
        for coord in locationOfString:
            row = coord[0]
            column = coord[1]
            Board.changeElementOfDataTable(self, table, row, column, 0)
        return table

    """Function to return the amount of tiles currently on the Scrabble Board"""
    def countCurrentLettersOnBoard(self, LOLBoard):
        indexListOfNonZeroElements = [] #LOLBoard
        for listItem in LOLBoard:
            result = [index for index, value in enumerate(listItem) if value != 0]
            indexListOfNonZeroElements.append(result)
        amountLetters = []    
        for nonZeroIndex in indexListOfNonZeroElements:
            numberNonZeroElements = len(nonZeroIndex)
            amountLetters.append(numberNonZeroElements)
        totalLetters = sum(amountLetters)    
        return totalLetters
    #print(countCurrentLettersOnBoard([["h","i",0],["y", "u", "s"],[0,0,"s"]]))

    """Function to count the amount of remaining tiles to be played within the Game"""
    def countTilesRemainingToBePlayed(self, LOLBoard):
        tilesRemaining = 100 - Board.countCurrentLettersOnBoard(self, LOLBoard)
        if tilesRemaining == 0:
            raise TypeError("No more tiles left to be played.  Game Over.")
        return tilesRemaining
    #print(countTilesRemainingToBePlayed([["h","i",0],["y","u","s"],[0,0,"s"]]))





boardObj = Board(1,2,3,4,5,6,7)
#print(boardObj.countCurrentLettersOnBoard([["h","i",0],["y", "u", "s"],[0,0,"s"]]))
#print(boardObj.scrabbleTableOutput(boardObj.enterWordOnTable([[3,4], [3,5], [3,6], [3,7], [3,8]], "hello")))





