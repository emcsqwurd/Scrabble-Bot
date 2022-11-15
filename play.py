from board import Board
from func import Func
from rack import Rack
from utils import Utils
from words import Words
from scoretable import ScoreTable
import numpy as np



testMat = np.zeros((15,15))
testCoord = [[3,4], [3,5], [3,6], [3,7], [3,8]]
funcObj = Func(testMat, 3, 2, "h", "hello", testCoord)
utilsObj = Utils(["h", "i"], [["h", "i"], ["g", "u", "y", "s"]], "hello", 5)
boardObj = Board(1,2,3,4,5,6,7)
testTable = [["hi","(3,4), (3,4)",40, 0,3], ["hi","(3,4), (3,4)",40, 0,3], ["hi","(3,4), (3,4)",40, 0,3]]
scoreTableObj = ScoreTable(testTable, "hi", "(3,4), (3,5)", 9 )
WL = ["well", "whats", "the", "yup"]
wordObj = Words(WL, 3, "e", "e", "e", 5)
rackObj = Rack("hello", 3, ["h", "e", "l", "l", "o"], "well")



#Confirming the user wants to run the program
print("Would you like to use the Scrabble Helper? (Type YES to use Program)")
answerInitialQ = input()
if answerInitialQ == "YES":
    print("The Following Lists the Rules and Keys for playing Scrabble:")
print("")    


#Detailing the rules and conditions of the Game for the user, including extra points information
rules = """(1): The scrabble board describes a 15x15 square grid, where each tile of the game can fit 
into each element of the scrabble grid.

(2): 
"""
print(rules)


#Aquiring user information: Player Names
print("Enter Opponents First Name:")
oppName = input()

print("Enter Your First Name:")
myName = input()

print("")
print("GAME: ON")
print("")


"""Firstly want to give all the 5 base branches of the code firstly without any input, e.g. 
1) scrabble board, 2) value matrix, 3) score table, 4) choice table and 5) rack."""




#Showing initial Score Table (empty)
base = [["", "", 0, 0, 0]]
zeroSTOtherPlayer = scoreTableObj.finalScoreTableOutputOtherPlayer(base, "", "", 0, oppName, myName)
print("Score Table")
print(zeroSTOtherPlayer)
print("")

#Showing intital Scrabble Board
zeroT = boardObj.dataTable()
print("Scrabble Board")
t0SB = print(boardObj.scrabbleTableOutput(zeroT))
print("")

#Showing initial Value Matrix
zeroM = funcObj.scrabbleMatrix()
print("Scrabble Value Table")
print(zeroM)
print("")


#List of all the Words that have been played during the Game
wordList = []


#Main function to be looped for playing the Game
def main():
    i = 0
    while True:

        #Asking the user for the letters chosen from the bag for the rack
        print("Enter the 7 random letters chosen for your rack:")
        rackString = input()
        print("")
        print("Scrabble Rack")
        print(rackObj.rackTable(rackString))
        print("")

        #Asking the user from such letters, what ones are wished to be considered when determining playable words
        print("Enter the letters from Rack you wish to use:")
        desiredRackString = input()
        rackMinus = rackObj.updateRackTakeAway(rackString, desiredRackString)
        print("")
        print("Scrabble Rack (Updated)")
        newRackMinus = rackObj.rackTable(rackMinus)
        print(newRackMinus)

        #First round user must fromulate word strictly from Rack letters
        if i == 0:
            wordsR0 = rackObj.findALLWordsFromRandomString(desiredRackString)

        #display R0 choice table


















        i+= 1
        return 
    return 
print(main())




"""
if __name__ == "main()":
    main()"""






