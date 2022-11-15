import numpy as np
from func import Func
#from func import doubleLetter, tripleLetter
#from func import doubleWord, tripleWord


#hard-coding coordinates of special blocks Letters on scrabble board
doubleLetterPos = [[3,0], [11,0], [6,2], [8,2], [7,3], [14,3], [12,6], [12,8], [11,7], [6,6], [8,6], [8,8], [14,11], [0,3], [0,11], [2,6], [2,8], [3,7], [3,14], [6,8], [6,12], [7,11], [8,12], [11,14]]
tripleLetterPos = [[5,1], [9,1], [5,5], [9,5], [13,5], [13,9], [9,9], [1,5], [1,9], [5,9], [5,13], [9,13]]

#need to still input UTH of special word blocks - UPDATE
doubleWordPos = [[1,1], [2,2], [3,3], [4,4], [7,7], [10,10], [11,11], [12,12], [13,13], [13,1], [12, 2], [11,3], [10,4]]
tripleWordPos = [[0,0], [7,0], [14,0], [14,7]]

testMat = np.zeros((15,15))
testCoord = [[3,4], [3,5], [3,6], [3,7], [3,8]]
funcObj = Func(testMat, 3, 2, "h", "hello", testCoord)



"""NEED TO CONDUCT THOUROUGH TEST TO ENSURE DURABILITY"""
"""Function to perform the functions for special letter blocks on scrable matrix"""
#input matrix must be 15x15 to work
def specialBlocksLetters(inputMatrix):
    #now need to apply respective functions to special blocks on LH of matrix
    inputMatrixBegin = inputMatrix
    for coordListDL in doubleLetterPos:
        rowDL = coordListDL[0]
        columnDL = coordListDL[1]
        funcObj.doubleLetter(inputMatrix, rowDL, columnDL)
    for coordListTL in tripleLetterPos:
        rowTL = coordListTL[0]
        columnTL = coordListTL[1]
        funcObj.tripleLetter(inputMatrix, rowTL, columnTL) 
    """
    #if item has remained unchanged, then change that element to 0
    for rowitem in inputMatrix:
        for columnitem in inputMatrix:
            if inputMatrixBegin[rowitem, columnitem].astype(bool) == inputMatrix[rowitem, columnitem].astype(bool):
                inputMatrix[rowitem, columnitem] = 0
    """
    return inputMatrix



def specialBlocksWords():
    return 










