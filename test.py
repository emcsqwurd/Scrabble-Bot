from tabulate import tabulate
import numpy as np
from scrabbledict import letterScoreDict
from matrix import searchRow
from special import specialBlocksLetters
from itertools import permutations
import itertools
from matrix import searchAllNeighbourTiles
import itertools
from utils import Utils



testListOfLists = [["h", "i"], ["g", "u", "y", "s"]]
testList = [1,2,3,4,5,6]
utilObj = Utils(testList, testListOfLists, "hello", 3)
yup = utilObj.findAllPermAndComb("the")












