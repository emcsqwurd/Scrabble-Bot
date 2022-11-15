

letterScoreDict = {

    "a" : 1, 
    "b" : 3, 
    "c" : 3,
    "d" : 2, 
    "e" : 1, 
    "f" : 4,
    "g" : 2, 
    "h" : 4, 
    "i" : 1,
    "j" : 8, 
    "k" : 5, 
    "l" : 1,
    "m" : 3, 
    "n" : 1, 
    "o" : 1,
    "p" : 3, 
    "q" : 10, 
    "r" : 1,
    "s" : 1, 
    "t" : 1, 
    "u" : 1,
    "v" : 4, 
    "w" : 4, 
    "x" : 8,
    "y" : 4, 
    "z" : 10,
    "!" : 1

}


"""Function to return letterScoreDict as a list of tuples"""
def letterScoreDictList():
    items = letterScoreDict.items()
    newList = list(items)
    return newList


letterScoreDictInvert = {
    1 : "a",
    3 : "b", 
    3 : "c",
    2 : "d", 
    1 : "e", 
    4 : "f",
    2 : "g",  
    4 : "h",  
    1 : "i",
    8 : "j", 
    5 : "k", 
    1 : "l",
    3 : "m", 
    1 : "n", 
    1 : "o",
    3 : "p", 
    10 : "q", 
    1 : "r",
    1 : "s", 
    1 : "t", 
    1 : "u",
    4 : "v", 
    4 : "w", 
    8 : "x",
    4 : "y", 
    10 : "z",
    1 : "!"
}


"""Function that returns letterScoreDictInvert as a list of tuples"""
def letterScoreDictInvertList():
    items = letterScoreDictInvert.items()
    newList = list(items)
    return newList


"""Function that returns dictionary organised by the values of each letter, results in [[], [],...] """
def organisedDict():
    valueList = [1,2,3,4,5,8,10]
    newList1 = []
    for value in valueList:
        subList = []
        for char in letterScoreDict:
            if letterScoreDict[char] == int(value):
                subList.append(char)
        newList1.append(subList) #newList1 = lists of grouped letters    
    return newList1
#print(organisedDict())







