import numpy as np


"""Function to search a specified row of some given matrix"""
def searchRow(matrix, rowNumber):
    newMatrix = matrix[rowNumber, :]
    return newMatrix


"""Function to search a specified column of some given matrix"""
def searchColumn(matrix, columnNumber):
    newMatrix = matrix[:, columnNumber]
    return newMatrix


"""Function to return square (3,3) matrix, of such the middle coord = middleTupleCoord"""
def searchAllNeighbourTiles(inputMatrix, row, column):
    newMat = np.zeros((3,3))
    #Following can be MEGAAAA optimised
    newMat[1,1] = inputMatrix[row, column] #setting speciifed to middle (not special cases)
    newMat[0,0] = inputMatrix[row-1, column-1]
    newMat[0,1] = inputMatrix[row-1, column]
    newMat[0,2] = inputMatrix[row-1, column+1]
    newMat[1,0] = inputMatrix[row, column-1]
    newMat[1,2] = inputMatrix[row, column+1]
    newMat[2,0] = inputMatrix[row+1, column-1]
    newMat[2,1] = inputMatrix[row+1, column]
    newMat[2,2] = inputMatrix[row+1, column+1]
    return newMat



def optimisedSearchAllNeighbourTiles():
    return 











