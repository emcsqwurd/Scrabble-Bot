import numpy as np
from func import Func
from locations import getFinalLocationsFromWordlist
from locations import getValueOfLocationOfStringAfterSpecialApplied
from utils import Utils

testMat = np.zeros((15,15))
testCoord = [[3,4], [3,5], [3,6], [3,7], [3,8]]
funcObj = Func(testMat, 3, 2, "h", "hello", testCoord)

testListOfLists = [["h", "i"], ["g", "u", "y", "s"]]
testList = [1,2,3,4,5,6]
utilsObj = Utils(testList, testListOfLists, "hello", 3)



"""Function to return the table of choices for the possible words for the user to play - top 5 value words to be played"""
def choiceTableData(board, wordList):
    locations = getFinalLocationsFromWordlist(board, wordList) #LLLOL => [[[[], [],...[]], [[], []...[]]],  [[[], [],...[]], [[], []...[]]]]  
    locValueList = []
    for idx in range(0, len(locations)):
        correspondingWord = wordList[idx]
        listOfLocs = locations[idx] #listOfLocs => LLOL
        for loc in listOfLocs: #loc => LOL
            locValue = getValueOfLocationOfStringAfterSpecialApplied(loc, correspondingWord) #locValue => integer
            locValueList.append(locValue)
    
    top10ValueList = utilsObj.getSpecifiedMaxValuesFromList(locValueList, 10) #obtaining the 10 max values from corresponding value list
    return 



























