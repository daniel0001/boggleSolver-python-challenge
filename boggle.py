# Boggle solver

import random
import string
# Read in the dictionary file to an object

dic = open("C:/Users/danie/Desktop/CodeInstitute/Stream 2/pythonChallenges/boggle/dictionary.txt")

# Read file object into an ordered array for searching
dicArray = []
for line in dic:
    dicLine = line[:-1]
    dicArray.append(dicLine)
# Test search dicArray for the word 'test'
if "test" in dicArray:
    print("Test if dictionary created passed")


letter = random.choice(string.ascii_lowercase)
# Test to see if letter is created
print("Test for random letter = " + letter)

def getRandomLetter():
    rLetter = random.choice(string.ascii_lowercase)
    return rLetter

#create square boggle grid ( n columns by n rows)
n = 4
board = [[getRandomLetter() for i in range(n)] for x in range(n)]
print("This is the board test =", board)

# reduce size of dictionary to match board
# def getLetterSet(row):
#     letters = set(row)
#     return letters

# letterSet = [getLetterSet(board[i]) for i in range(n)]

letterList = []
y = 0
for i in board:
    for x in board[y]:
        letterList.append(x)
    y = y + 1

letterSet = set(letterList)
print("Test of the letterSet = ", letterSet)

# now remove all words starting with each letter in letterSet from the dictionary
# for i in letterSet:
wordCount = 0
smallDicArray = []
for i in letterSet:
    for word in dicArray:
        if word[:1] == i:
            smallDicArray.append(word)
            wordCount = wordCount + 1
print("Test of reduced size dictioanry =", wordCount)

# Search the reduced dictionary to see if it contains the
# String str and return boolean
wordToSearch = "test"
def wordSearch(wordToSearch):
    return wordToSearch in dicArray

print("Test: If string test in smallDicSearch =", wordSearch(str))

subString = "te"
def checkSubStringInDictionary(subString, smallDicArray):
    charTotal = len(subString)
    for word in smallDicArray:
        if word[0 : charTotal] == subString:
            return True
    return False 
            

print("Test: If subString te in smallDicArray =", checkSubStringInDictionary(subString, smallDicArray))

# Build the string from the board - string is > 2 characters
# Search string not to repeat a square previously appended to string
# Test start square is row 1, col 1

row = 1
col = 1

searchStr = board[1][1] + board[0][1]

print("Test 2 char searchStr =", searchStr)
print("Test 2 char searchStr in reduced dictionary (False or True are ok)=", wordSearch(searchStr))

# find out how many serach results there should be for each square
# n = board size
boardSize = 4 
# sq* = number of neighbours the square has
sqMax = 8
sqMin = 3
sqSide = 5

def maxSearchSize(row, col, boardSize):
    if (row == 0 and col == 0) or (row == 0 and col == boardSize) or (row == boardSize and col == 0) or (row == boardSize and col == boardSize):
        return sqMin
    if ((row == 0 and col > 0) and (row == 0 and col < boardSize)) or ((row > 0 and col == 0) and (row < boardSize and col == 0)) or ((row == boardSize and col > 0) and (row == boardSize and col < boardSize)) or ((row > 0 and col == boardSize) and (row < boardSize and col == boardSize)):
        return sqSide
    if ((row > 0 and col > 0) and (row < boardSize and col < boardSize)):
        return sqMax
print("Test initial num neighbours to search for corner (pass = 3) = ", maxSearchSize(0, 0, boardSize))
print("Test initial num neighbours to search for corner (pass = 3) = ", maxSearchSize(boardSize, boardSize, boardSize))
print("Test initial num neighbours to search for corner (pass = 3) = ", maxSearchSize(boardSize, 0, boardSize))
print("Test initial num neighbours to search for corner (pass = 3) = ", maxSearchSize(0, boardSize, boardSize))

print("Test initial num neighbours to search for side (should be 5) = ", maxSearchSize(0, 1, boardSize))
print("Test initial num neighbours to search for side (should be 5) = ", maxSearchSize(1, 0, boardSize))
print("Test initial num neighbours to search for side (should be 5) = ", maxSearchSize(boardSize, 1, boardSize))
print("Test initial num neighbours to search for side (should be 5) = ", maxSearchSize(1, boardSize, boardSize))
print("Test initial num neighbours to search for side (should be 5) = ", maxSearchSize(1, 0, boardSize))

print("Test initial num neighbours to search for middle (should be 8) = ", maxSearchSize(1, 1, boardSize))

# Get location of square tl (top left),tr,bl,br / ts (top side), rs, bs, ls / middle
def location(row, col, boardSize):
    if (row == 0 and col == 0):
        return "tl"
    if (row == 0 and col == boardSize - 1):
        return "tr"
    if (row == boardSize - 1 and col == 0):
        return "bl"
    if (row == boardSize - 1 and col == boardSize - 1):
        return "br"
    if ((row == 0 and col > 0) and (row == 0 and col < boardSize - 1)):
        return "ts"
    if ((row > 0 and col == 0) and (row < boardSize - 1 and col == 0)):
        return "ls"
    if ((row == boardSize - 1 and col > 0) and (row == boardSize - 1 and col < boardSize - 1)):
        return "bs"
    if ((row > 0 and col == boardSize - 1) and (row < boardSize - 1 and col == boardSize - 1)):
        return "rs"
    if ((row > 0 and col > 0) and (row < boardSize - 1 and col < boardSize - 1)):
        return "middle"


#  1. build a search algorithm to check if search substring in dictionary
#  Assume that if the substring return false then stop building
#  that string eg. there are no words in the dictionary beginning "xz"
#  so a boolean False should stop searching where as "at" should return
#  true and continue to build: "ate" = True continue, "atex" = False so stop/break".

#  2. Track True subStrings by appending to a list called solutions.

# 3. Then check if each list index is in the dictionary to remove substrings that
# aren't whole words e.g "ang" is True as a substring of "anger" but not whole so remove
# from solutions

#  Test by building one string first

def neighbourLetterFinder(r, c, board, loc):
    neighbourSquares = []
    square = "{0}, {1}"
    if loc == "tl":
        neighbourSquares += [
            {square.format(r, c + 1): board[r][c + 1]},
            {square.format(r + 1, c + 1): board[r + 1][c + 1]},
            {square.format(r + 1, c): board[r + 1][c]},
        ]
    elif loc == "tr":
        neighbourSquares += [
            {square.format(r, c -1): board[r][c - 1]},
            {square.format(r + 1, c -1): board[r + 1][c - 1]},
            {square.format(r + 1, c): board[r + 1][c]},
        ]
    elif loc == "br":
        neighbourSquares += [
            {square.format(r, c -1): board[r][c - 1]},
            {square.format(r - 1, c -1): board[r - 1][c - 1]},
            {square.format(r - 1, c): board[r - 1][c]},
        ]
    elif loc == "bl":
        neighbourSquares += [
            {square.format(r, c + 1): board[r][c + 1]},
            {square.format(r - 1, c + 1): board[r - 1][c + 1]},
            {square.format(r - 1, c): board[r - 1][c]},
        ]
    elif loc == "ts":
        neighbourSquares += [
            {square.format(r, c -1): board[r][c - 1]},
            {square.format(r + 1, c -1): board[r + 1][c - 1]},
            {square.format(r + 1, c): board[r + 1][c]},
            {square.format(r + 1, c + 1): board[r + 1][c + 1]},
            {square.format(r, c + 1): board[r][c + 1]},
        ]
    elif loc == "rs":
        neighbourSquares += [
            {square.format(r - 1, c): board[r - 1][c]},
            {square.format(r - 1, c - 1): board[r - 1][c - 1]},
            {square.format(r, c -1): board[r][c - 1]},
            {square.format(r + 1, c -1): board[r + 1][c - 1]},
            {square.format(r + 1, c): board[r + 1][c]},
        ]
    elif loc == "bs":
        neighbourSquares += [
            {square.format(r, c -1): board[r][c - 1]},
            {square.format(r - 1, c -1): board[r - 1][c - 1]},
            {square.format(r - 1, c): board[r - 1][c]},
            {square.format(r - 1, c + 1): board[r - 1][c + 1]},
            {square.format(r, c + 1): board[r][c + 1]},
        ]
    elif loc == "ls":
        neighbourSquares += [
            {square.format(r - 1, c): board[r - 1][c]},
            {square.format(r - 1, c + 1): board[r - 1][c + 1]},
            {square.format(r, c + 1): board[r][c + 1]},
            {square.format(r + 1, c + 1): board[r + 1][c + 1]},
            {square.format(r + 1, c): board[r + 1][c]},
        ]
    else:
        neighbourSquares += [
            {square.format(r -1, c): board[r -1][c]},
            {square.format(r -1, c + 1): board[r - 1][c + 1]},
            {square.format(r, c + 1): board[r][c + 1]},
            {square.format(r + 1, c + 1): board[r + 1][c + 1]},
            {square.format(r + 1, c): board[r+ 1][c]},
            {square.format(r + 1, c -1): board[r + 1][c - 1]},
            {square.format(r, c -1): board[r][c - 1]},
            {square.format(r - 1, c -1): board[r - 1][c - 1]},
        ]
    return neighbourSquares


# Build a list of possible solutions like a snake, starting with each letter on board
# candidateString passed in to nextLetterArrayBuilder with visitedSquares
# returns list of more candidates
# Then candidate checked if a whole valid word and added to the finalSolution list

# TRack visited squares using dictionary = string : [square1, square 2, square3]
visitedSquares = []

candidateString = ""
finalSolutions = []
def nextLetterArrayBuilder(r, c, board, boardSize, visitedSquares, candidateString):
    currentSquare = [r, c]
    if visitedSquares == []:
        candidateString = board[r][c]
        visitedSquares.append({candidateString: currentSquare})
    neighbourSquares = []
    solutionList = []
    squareList = []
    loc = location(r, c, boardSize)
    neighbourLetters = neighbourLetterFinder(r, c, board, loc)
    for letter in neighbourLetters:
        val = list(letter.values())
        square = list(letter.keys())
        for visited in visitedSquares:
            candKey = list(visited.keys())
            if candKey[0] == candidateString:
                candSquareList = list(visited.values())
                if not square in candSquareList:
                    solutionString = candidateString +  val[0]
                    if checkSubStringInDictionary(solutionString, smallDicArray):
                        solutionList.append(solutionString)
                        visitedSquares.append({solutionString: [candSquareList + square]})
    solutions = [solutionList, visitedSquares]
    return solutions

# print("Test all solutions generated using r:0, c:0 = ", nextLetterArrayBuilder(0, 0, board, boardSize, visitedSquares, candidateString) )
print(board)

# Build 3rd square solution to add third valid character to the solutionArray without
# doubling back on a previously seen square

# First run pass in exact values for row and col ( r:0 , c:0) then get values from the returned array

def boardSolver(board, boardSize):
    finalSolutions = []
    for row in range(boardSize):
        for col in range(boardSize):
            visitedSquares = []
            candidateString = ""
            solutions = nextLetterArrayBuilder(row, col, board, boardSize, visitedSquares, candidateString)
            candidateList = solutions[0]
            visitedSquares = solutions[1]
            while len(candidateList) > 0:
                for candidate in candidateList:
                    solutions = nextLetterArrayBuilder(row, col, board, boardSize, visitedSquares, candidate)
                    candidateList = solutions[0]
                    finalSolutions = storeValidWords(candidateList, finalSolutions)
                    visitedSquares = solutions[1]
    finalSolutions = wholeWordCheck(finalSolutions)
    return finalSolutions


# Add valid words to the finalSolutions array by taking in an array
def storeValidWords (candidateList, finalSolutions):
    for word in candidateList:
        if checkSubStringInDictionary(word, smallDicArray):
            finalSolutions.append(word)
    return finalSolutions

def wholeWordCheck(finalSolutions):
    wholeWords = []
    for word in finalSolutions:
        charTotal = len(word)
        for dicWord in smallDicArray:
            if charTotal == len(dicWord):
                if word == dicWord:
                    wholeWords.append(dicWord)
    wholeWords = set(wholeWords)
    return wholeWords


print("Test that finalSolutions is being built =", boardSolver(board, boardSize))
