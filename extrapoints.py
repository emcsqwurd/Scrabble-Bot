#from func import valuesOfWord
from func import Func
import numpy as np



"""
The following bonus points and conditions are required to be implemented:

(1): There is a max amount of 100 letter tabs to be distributed:
out of these 100, 98 are are score letters, but there are 2 blank tiles, that have
no score value, but can be utilized as any letter

(2): Any player who uses all 7 letters from the rack to make a word gets awarded
an additional 50 points on top of the score awarded by the word.  (STAR: this is AFTER
the double or triple word case)

(3): you may use your turn to replace any or all of the tiles in your rack, however
this exchange of tiles counts for the players turn

(4): you are allowed to pass your turn if a word cannot be formulated. However, if both
players pass twice in a row, the game ends

(5): the same word can be played more than once

(6): pluralised words are not allowed

(7): Once the first player has used all their tiles and the tile bag is empty, the game
is over

"""


testMat = np.zeros((15,15))
testCoord = [[3,4], [3,5], [3,6], [3,7], [3,8]]
funcObj = Func(testMat, 3, 2, "h", "hello", testCoord)




"""Function to obtain values of strings from list of strings"""
def turnStringsToValues(wordList):
    output = []
    for word in wordList:
        value = funcObj.valuesOfWord(word)
        output.append(value)
    return output








