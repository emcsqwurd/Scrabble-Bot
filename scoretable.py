import numpy as np
from tabulate import tabulate
from func import Func

testMat = np.zeros((15,15))
testCoord = [[3,4], [3,5], [3,6], [3,7], [3,8]]
funcObj = Func(testMat, 3, 2, "h", "hello", testCoord)


class ScoreTable:

    def __init__(self, tableLOL, word, location, round) -> None:
        self.tableLOL = tableLOL #1 - List of List
        self.word = word #2 - string
        self.location = location #3 - string of tuples e.g hey => "(3,4), (3,5), (3,6)""
        self.round = round
        return 

    """Function to utilize when wishing to add the current rounds data to the score table LOL (for the player of the
    Game NOT utilizing the Program)
    IMPORTANT: Make sure that, if tableLOL is being inout for first round, where only consisits of single list [],
    must ensure input takes the form [[]]"""
    def scoreTableUpdateOtherPlayer(self, tableLOL, word, location, round): #tableLOL = [word, location, p1, p2, round, FINALSCORE]
        table = tableLOL
        score = funcObj.totalValueOfWord(word)
        totalScoresList = []
        for dataList in tableLOL:
            playerScores = dataList[2]
            totalScoresList.append(playerScores)
        totalScoreP1 = sum(totalScoresList) + score
        LOLTable = [[word, location, score, 0, round, totalScoreP1, 0]]
        for item in table:
            LOLTable.append(item)
        return LOLTable

    """Function to output Final Score table for other Player NOT utilizing Program"""
    def finalScoreTableOutputOtherPlayer(self, tableLOL, word, location, round, nameOP, nameU):
        LOL = ScoreTable.scoreTableUpdateOtherPlayer(self, tableLOL, word, location, round)
        outPut = tabulate(LOL, headers = ["Word", "Location of Word", "Score:" + nameOP, "Score:" + nameU, "Round", "TOTAL Score:" + nameOP, "TOTAL Score:" + nameU])
        return outPut
   
    """Function to utilize when wishing to add the current rounds data to the score table LOL (for the player of the Game
    that IS utilizing the program)"""
    def scoreTableUpdateProgramUser(self, tableLOL, word, location, round):
        table = tableLOL
        score = funcObj.totalValueOfWord(word)
        totalScoresList = []
        for dataList in tableLOL:
            playerScores = dataList[3]
            totalScoresList.append(playerScores)
        print(totalScoresList)    
        totalScoreP2 = sum(totalScoresList) + score
        LOLTable = [[word, location, 0, score, round, 0, totalScoreP2]]
        for item in table:
            LOLTable.append(item)
        return LOLTable
    
    """Function to output Final Score table for Player that IS utilizing Program"""
    def finalScoreTableOutputProgramUser(self, tableLOL, word, location, round, nameOP, nameU):
        LOL = ScoreTable.scoreTableUpdateProgramUser(self, tableLOL, word, location, round)
        outPut = tabulate(LOL, headers = ["Word", "Location of Word", "Score:" + nameOP, "Score:" + nameU, "Round", "TOTAL Score:" + nameOP, "TOTAL Score:" + nameU])
        return outPut


testTable = [["hi","(3,4), (3,4)",40, 0,3], ["hi","(3,4), (3,4)",40, 0,3], ["hi","(3,4), (3,4)",40, 0,3]]
scoreTableObj = ScoreTable(testTable, "hi", "(3,4), (3,5)", 9 )
#print(scoreTableObj.finalScoreTableOutputOtherPlayer(testTable, "hi", "(3,4), (3,5)", 9 ))












