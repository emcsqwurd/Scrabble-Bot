from re import L
import numpy as np
from board import Board
from conditions import conditionEmpty, conditionFit, checkLocWithCondit
from func import Func
from utils import Utils

#hard-coding coordinates of special blocks Letters on scrabble board
doubleLetterPos = [[3,0], [11,0], [6,2], [8,2], [7,3], [14,3], [12,6], [12,8], [11,7], [6,6], [8,6], [8,8], [14,11], [0,3], [0,11], [2,6], [2,8], [3,7], [3,14], [6,8], [6,12], [7,11], [8,12], [11,14]]
tripleLetterPos = [[5,1], [9,1], [5,5], [9,5], [13,5], [13,9], [9,9], [1,5], [1,9], [5,9], [5,13], [9,13]]

#need to still input UTH of special word blocks - UPDATE
doubleWordPos = [[1,1], [2,2], [3,3], [4,4], [7,7], [10,10], [11,11], [12,12], [13,13], [13,1], [12, 2], [11,3], [10,4]]
tripleWordPos = [[0,0], [7,0], [14,0], [14,7]]



boardObj = Board(1,2,3,4,5,6,7)

testMat = np.zeros((15,15))
testCoord = [[3,4], [3,5], [3,6], [3,7], [3,8]]
funcObj = Func(testMat, 3, 2, "h", "hello", testCoord)

testListOfLists = [["h", "i"], ["g", "u", "y", "s"]]
testList = [1,2,3,4,5,6]
utilsObj = Utils(testList, testListOfLists, "hello", 3)



"""Function to return a LOL describing the locations of all the starting letters of specified word on scrabble board"""
def checkLocationsOfSWLetter(board, word): #board = scrabble board, word = string
    LOLCoord = []
    for row in board:
        if word[0] in row:
            columnCoord = row.index(word[0]) + 1
            rowCoord = board.index(row) + 1 
            #Now have coordinate(s) of all this letter on Scrabble Board - NOT TRUE!!!
            coord = [rowCoord, columnCoord]
            LOLCoord.append(coord)
    return LOLCoord 

"""Function to return a LOL describing the locations of all the ending letters of specified word on scrabble board"""
def checkLocationsOfEWLetter(board, word):
    LOLCoord = []
    for row in board:
        if word[-1] in row:
            columnCoord = row.index(word[-1]) + 1 
            rowCoord = board.index(row) + 1 
            coord = [rowCoord, columnCoord]
            LOLCoord.append(coord)
    return LOLCoord 

"""Function to return a LOL of locations on the board that equal the specified letter in the argument"""
def checkBoardForLetter(board, letter): #FUNC WORKS - however, has shown not fully accurate on some cases
    coordList = []
    for rowList in board:
        if rowList == board[0]:
            rowIndex = 1
        elif rowList == board[1]:
            rowIndex = 2
        elif rowList == board[2]:
            rowIndex = 3
        elif rowList == board[3]:
            rowIndex = 4
        elif rowList == board[4]:
            rowIndex = 5
        elif rowList == board[5]:
            rowIndex = 6
        elif rowList == board[6]:
            rowIndex = 7
        elif rowList == board[7]:
            rowIndex = 8
        elif rowList == board[8]:
            rowIndex = 9
        elif rowList == board[9]:
            rowIndex = 10
        elif rowList == board[10]:
            rowIndex = 11
        elif rowList == board[11]:
            rowIndex = 12
        elif rowList == board[12]:
            rowIndex = 13
        elif rowList == board[13]:
            rowIndex = 14
        elif rowList == board[14]:
            rowIndex = 15
        for i in range(0, len(rowList)):
            loc = rowList[i]
            if letter == loc:
                desired = [rowIndex, i + 1]
                coordList.append(desired)
    return coordList

""""""
def possLocationsOfWordOP(board, word):
    wordLetterList = utilsObj.stringToList(word)
    testL = []
    for letter in word:
        letLoc = checkBoardForLetter(board, letter)
        for loc in letLoc:
            row = loc[0]
            column = loc[1]
            letEle = board[row - 1][column - 1]
            if letEle in wordLetterList:
                letterIndexOfWord = wordLetterList.index(letEle)
                RL = []
                LL = []
                UL = []
                DL = []
                for idx in range(0, len(word)):
                    right = [row, column - letterIndexOfWord + idx]
                    RL.append(right)
                    if len(right) == len(word):
                        testL.append(RL)
                    left = [row, column + letterIndexOfWord - idx]
                    LL.append(left)
                    if len(LL) == len(word):
                        testL.append(LL)
                        print(LL)
                    up = [row + letterIndexOfWord - idx, column]
                    UL.append(up)
                    if len(UL) == len(word):
                        testL.append(UL)
                    down = [row - letterIndexOfWord + idx, column]
                    DL.append(down)
                    if len(DL) == len(word):
                        testL.append(DL)
    print(len(testL))
    return testL



"""FUNCTION NEEDS TO BE EXTREMELY ROBUST - CONDUCT THOUGHOUR TESTING OF FUNCTION"""
#Need to split function up into 4 composite parts first, ones that search R,L,U,D, then this can be repeated for 
#every existence of said letter on the board, where from the outcome locations, locations can then be verified
#if they satisfy conditions
"""Function to return LLOL describing possible locations for word to be placed"""
def possLocationsOfWord(board, word): 
    possWordLocList = [] #old method
    for letter in word:
        letLoc = checkBoardForLetter(board, letter)
        for loc in letLoc:
            letLocR = []
            letLocL = []
            letLocU = []
            letLocD = [] 
            for num in range(0, len(word)): 
                nextLetR = [loc[0], loc[1] + num] #Search Right
                letLocR.append(nextLetR)
                if len(letLocR) == len(word):
                    possWordLocList.append(letLocR)
                nextLetL = [loc[0], loc[1] - num] #Search Left
                letLocL.append(nextLetL)
                if len(letLocL) == len(word):
                    possWordLocList.append(letLocL)    
                nextLetU = [loc[0] - num, loc[1]] #Search Up
                letLocU.append(nextLetU)
                if len(letLocU) == len(word):
                    possWordLocList.append(letLocU) 
                nextLetU = [loc[0] + num, loc[1]] #Search Down
                letLocD.append(nextLetU)
                if len(letLocD) == len(word):
                    possWordLocList.append(letLocD)
    
    print(len(possWordLocList))
    return possWordLocList #LLOL

"""Function to return the final LLOL describing the final locations for each given word within a wordlist that
a word can be placed on the scrabble board"""
def getFinalLocationsFromWordlist(board, wordList):
    possLocListForWords = [] #LLLOL
    for word in wordList:
        possLoc = possLocationsOfWordOP(board, word) #LLOL
        print("Possible locations of word")
        print(possLoc)
        wordLocList = []
        for loc in possLoc:
            print("loc")
            print(loc)
            conditionCheck = checkLocWithCondit(board, loc, word)
            print(conditionCheck)
            if conditionCheck == True:
                wordLocList.append(loc)
        possLocListForWords.append(wordLocList)        
    return possLocListForWords  #want output to be LLOL, so can be passed through for every LOL regarding conditions file



"""Function to check locations against special tiles and to return total points that said string with location obtains"""
def getValueOfLocationOfStringAfterSpecialApplied(locationOfString, string):
    DLL = []
    TLL = []
    DWL = []
    TWL = []
    DLLsym = []
    TLLsym =[]
    for idx in range(0, len(locationOfString)):
        coord = locationOfString[idx]
        coord[0] = coord[0] - 1 #correct logic to ensure index of row coord is correct
        coord[1] = coord[1] - 1  #correct logic to ensure index of column coord is correct
        if coord in doubleLetterPos:
            letter = string[idx]
            extraValueDL = funcObj.doubleL(letter)
            DLL.append(extraValueDL)
            DLLsym.append(letter)
        if coord in tripleLetterPos:
            letter = string[idx]
            extraValueTL = funcObj.triplL(letter)
            TLL.append(extraValueTL)
            TLLsym.append(letter)
    #combing all effected double/triple letters into LOL of such letters
    DTEffect = []
    DTEffect.append(DLLsym)
    DTEffect.append(TLLsym)
    #Getting rid of empty letter lists (e.g if double/triple letter doesnt play a part in score update) get rid of empty list
    for letList in DTEffect:
        if len(letList) == 0:
            DTEffect.remove(letList)
    stringValue = funcObj.totalValueOfWord(string) #getting total value of string
    f = []
    for letListItem in DTEffect:
        ex = []
        for item in letListItem:
            wordValue = funcObj.totalValueOfWord(item) #finding out sum value of such letters
            ex.append(wordValue)
        f.append(ex)
    outL = []
    for vList in f:
        sumTypeTile = sum(vList)
        outL.append(sumTypeTile)
    finalS = sum(outL)
    extraV = (sum(DLL) + sum(TLL)) - finalS #obtaining the values to be added to value of string as result of doubling/tripling
    letD = "".join(DLLsym) #getting double letter effected letters from string
    letT = "".join(TLLsym) #getting triple letter effected letters from string
    for newidx in range(0, len(locationOfString)):
        coord = locationOfString[newidx]
        coord[0] = coord[0]   #correct logic to ensure index of row coord is correct
        coord[1] = coord[1] #correct logic to ensure index of column coord is correct
        if coord in doubleWordPos:
            extraValueDW = funcObj.doubleWord(string + letD) #if word is doubled, double value of string after double letters effect (ensuring accurate sum of letters after special tiles)
            DWL.append(extraValueDW) 
        if coord in tripleWordPos:
            extraValueTW = funcObj.tripleWord(string + letT) #if word is tripled, double value of string after triple letters effect (ensuring accurate sum of letters after special tiles)
            TWL.append(extraValueTW)      
    #final output process
    if len(DWL) > 0: #if double word tile has been utilised:
        return DWL[0] #return the final score of double word (after double/triple letter tiles have been implemented)
    if len(TWL) > 0: #if triple word tile has been utilized
        return TWL[0] #return the final score of triple word (after double/triple letter tiles have been implemented)
    else: #if string has not landed on any double/triple word tiles (only double or triple letter tiles)
        return stringValue + extraV





testB = boardObj.dataTable()
newTestB = boardObj.enterWordOnTable(testB, [[6,6], [6,7], [6,8], [6,9], [6,10]], "hello" ) #FURTHER TESTING REQUIRED - THINK HANNAH
#update1 = boardObj.enterWordOnTable(newTestB, [[7,4], [7,5], [7,6], [7,7], [7,8], [7,9]], "uheuat")
#update2 = boardObj.enterWordOnTable(update1, [[1,1], [2,1], [3,1], [4,1], [5,1], [6,1]], "hatuyh")
print(boardObj.scrabbleTableOutput(newTestB))
#print("--------locations of start letter")
#print(checkLocationsOfSWLetter(update2, "hannah"))

#print("--------locations of end letter")
#print(checkLocationsOfEWLetter(update2, "hannah"))

print("--------ways to place word")
print(possLocationsOfWord(newTestB, "howdy"))

print("--------ways to place word optimised")
print(possLocationsOfWordOP(newTestB, "howdy"))

#print("---------Checking board for letter")
#print(checkBoardForLetter(newTestB, "e"))

#print("---------Checking Locations are okay")
#print(checkLocWithCondit(newTestB, [[1,1], [2,1], [3,1], [4,1], [5,1], [6,1]]))

#print("final locations list for list of choice words")
#print(getFinalLocationsFromWordlist(newTestB, ["howdy", "hiya"]))

#print("check locations with special tiles")
#print(getValueOfLocationOfStringAfterSpecialApplied([[1,1],[1,2],[1,3],[1,4]], "guys"))







