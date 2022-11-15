import numpy as np
from sympy import Or
from board import Board
from dict import listEnglishWords
from scrabbledict import letterScoreDictList
import itertools
from utils import Utils

"""Idea is to introduce boolean condition functions, where if such functions are tried to ensure neccessary
conditions are met for the allowed input of words, such said functions will return TRUE, hence, when all 
condition functions return TRUE, => tested string for this location is indeed allowed"""

boardObj = Board(1,2,3,4,5,6,7)
utilsObj = Utils(["h", "i"], [["h", "i"], ["g", "u", "y", "s"]], "hello", 5)



#STILL MAY REQUIRE MORE ROBUST TESTING
"""Boolean Function to check if space (LOL describing locations of letters) is empty to place word, 
Returns True if all locations are empty, Returns False if even one of the locations is NOT empty"""
def conditionEmpty(board, location, string): # board -> listOfLists describing scrabble board, location = coordinate [row, column] of tile
    #board = List of Lists, location = List of Lists
    checkList = []
    for idx in range(0, len(location)):
        coord = location[idx]
        row = coord[0]
        column = coord[1]
        if board[row - 1][column - 1] != 0: # => some letter is already at this location
            #-----------Dealing with if input string matches position of element is okay--------
            wordTL = []
            let = board[row - 1][column - 1]
            if let == string[idx]:
                wordTL.append(True)    
            else:
                wordTL.append(False)    #FALSE => location is NOT empty
            for item in wordTL:
                checkList.append(item)
            #-----------------------------------------------------------------------------------
        else:
            checkList.append(True) #TRUE => location IS empty
    #print(checkList) 
    if False in checkList:
        return False
    else:
        return True #If function yields True, this location for the word is possible, false => not possible to place word at these locations
             
"""Boolean function to check if a possible location does fit on the board, i.e from the starting letter placement
position, can a word be placed in the given (1/4) direction(s) without overgoing boundaries, returns TRUE if 
satisfies condition, FALSE if not"""
def conditionFit(location): #location = LOL describing locations of letters in string
    testL = []
    for coord in location:
        row = coord[0]
        column = coord[1]
        if row <= 0: 
            testL.append(False)
        else:
            testL.append(True)    
        if column <= 0: 
            testL.append(False)
        else:
            testL.append(True)              
    if False in testL:
        return False
    else:
        return True

"""Function requires heavy optimisation - make sure to fic before implementation"""
#REQUIRES ROBUST TESTING - WILL NOT WORK FOR LOTS OF WORDS PLAYED - CHECK COMMENTS
"""Boolean Function to check if a possible location is allowed on the board, in the sense that, when a word is placed
onto the board, if a letter is directly connected (UDLR) to another letter, then these letters must formulate
an accepted word for this location to be allowed"""
def conditionAdjacency(board, location, string):
    boardObj.enterWordOnTable(board, location, string ) #- INVESTIGATE - SHOULD WORK BUT BREAKS MODEL
    startL = []
    for coord in location:
        row = coord[0]
        column = coord[1] #element = board[row - 1][column - 1]
        vertL = []
        horL = []
        for idxV in range(0, 15): #whole column of scrabble board where element is 
            newV = board[idxV - 1][column - 1]
            vertL.append(newV)
        for idxH in range(0, 15): #whole row of scrabble board where element is
            newH = board[row - 1][idxH - 1]
            horL.append(newH)
        startL.append(vertL)
        startL.append(horL)    
    finalL = []
    for possList in startL:
        wordL = []

        #--------------- MAKE BETTER START-----
        for sym in possList:
            if sym != 0:
                newString = ''.join(sym)
                wordL.append(newString)
        finalL.append(wordL)
        #--------------- MAKE BETTER END-----
        
    stringL = utilsObj.joinInternalLists(finalL) #NOT SUFFICIENT FOR LOTS OF WORDS ON BOARD - THINK!!!!
    for comb in stringL:
        if len(comb) == 1:        
            stringL.remove(comb)          
    boardObj.removeWordFromTable(board, location) #correct location for removal of string
    
    #---------------------OPTIMISE FROM HERE DOWN
    wasteL = []
    newStringL = []
    for idxE in range(0, len(stringL)):
        if stringL[idxE] == string:
            wasteL.append(stringL[idxE])
        else:
            newStringL.append(stringL[idxE])
    permL = []
    for possW in newStringL:
        perm = utilsObj.findAllPermutations(possW)
        permL.append(perm)
    finalP = []
    for permEle in permL:
        joined = utilsObj.joinInternalLists(permEle)
        finalP.append(joined)
    finalRes = []
    for listOfPoss in finalP:
        guessRes = []
        for guess in listOfPoss:
            if guess in listEnglishWords():
                guessRes.append(True)
            else:
                guessRes.append(False)    
        finalRes.append(guessRes)
    finalBoolList = []
    for boolList in finalRes:
        print(boolList)
        if True in boolList:
            finalBoolList.append(True)
        if False in boolList:
            finalBoolList.append(False)    
    if False in finalBoolList:
        return False
    else:
        return True 
            

"""Optimised Adjacency condition"""
def conditionAdjacencyOP(board, location, string):
    boardObj.enterWordOnTable(board, location, string)
    startL = []
    for coord in location:
        row = coord[0]
        column = coord[1] #element = board[row - 1][column - 1]
        vertL = []
        horL = []
        for idxV in range(0, 15): #whole column of scrabble board where element is 
            newV = board[idxV - 1][column - 1]
            vertL.append(newV)
        for idxH in range(0, 15): #whole row of scrabble board where element is
            newH = board[row - 1][idxH - 1]
            horL.append(newH)
        startL.append(vertL)
        startL.append(horL)    
    finalL = []
    for possList in startL:
        wordL = []
        #--------------- MAKE BETTER START-----
        for sym in possList:
            if sym != 0:
                newString = ''.join(sym)
                wordL.append(newString)
        finalL.append(wordL)
        #--------------- MAKE BETTER END-----
    stringL = utilsObj.joinInternalLists(finalL) #NOT SUFFICIENT FOR LOTS OF WORDS ON BOARD - THINK!!!!
    for comb in stringL:
        if len(comb) == 1:        
            stringL.remove(comb)                 
    boardObj.removeWordFromTable(board, location)
    stringIndexL = [i for i in range(len(stringL)) if stringL[i] == string]  #Getting index's of elements in stringL == string
    utilsObj.deleteMultipleElement(stringL, stringIndexL)
    permL = []
    for test in stringL:
        perm = utilsObj.findAllPermutations(test)
        next = utilsObj.joinInternalLists(perm)
        permL.append(next)
    FBL = []
    for permGuessList in permL:
        boolL = []
        for guessIdx in range(len(permGuessList)):
            if permGuessList[guessIdx] in listEnglishWords():
                boolL.append(True)
            else:
                boolL.append(False)
        FBL.append(boolL)    
    finalBL = []
    for boolList in FBL:
        if True in boolList:
            finalBL.append(True)
        else:
            finalBL.append(False)   
    if False in finalBL:
        return False
    else:
        return True    




"""Function to check a given location satisfies all conditions required to be met"""
def checkLocWithCondit(board, locationOfString, string):
    totalResList = []
    resEmp = conditionEmpty(board, locationOfString, string)
    totalResList.append(resEmp)
    resFit = conditionFit(locationOfString)
    totalResList.append(resFit)
    resAdj = conditionAdjacencyOP(board, locationOfString, string)
    totalResList.append(resAdj)
    print(totalResList)
    if False in totalResList:
        return False
    else:
        return True




testB = boardObj.dataTable()
newTestB = boardObj.enterWordOnTable(testB, [[3,4], [3,5], [3,6], [3,7], [3,8]], "hello" )
#newTestB2 = boardObj.enterWordOnTable(testB, [[5,4], [5,5], [5,6], [5,7], [5,8]], "hello" )
#newTestB3 = boardObj.enterWordOnTable(testB, [[4,1],[4,2],[4,3],[4,4]], "hiya" )

print("-----------Scrabble output")
print(boardObj.scrabbleTableOutput(newTestB))

#print("-----------condition empty")
#print(conditionEmpty(newTestB3, [[5,5], [6,5], [7,5]], "hey")) 

#print("Checking Adjacency Condition")
#print(conditionAdjacency(newTestB, [[4,2],[4,3],[4,4],[4,5]], "hizh")) #may need to add word as argument into function

print("Checking optimised Adjacency Condition")
print(conditionAdjacencyOP(newTestB, [[4,2],[4,3],[4,4],[4,5]], "jwif"))

#print("-----------Checking overall conditions of given string for given location")
#print(checkLocWithCondit(newTestB, [[4,1],[4,2],[4,3],[4,4]], "hiyo"))



