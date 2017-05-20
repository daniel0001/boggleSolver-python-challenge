# Boggle solver

import random
import string
# Read in the dictionary file to an object

dic = open("C:/Users/danie/Desktop/CodeInstitute/Stream 2/pythonChallenges/dictionary.txt")

# Read file object into an ordered array for searching
dicArray = []
for line in dic:
    str = line[:-1]
    dicArray.append(str)
# Test search dicArray for the word 'test'
if "test" in dicArray:
    print("Test if dictionarray created passed")


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
print(smallDicArray)
print("Test of reduced size dictioanry =", wordCount)

# Search the reduced dictionary to see if it contains the
# String str and return boolean
str = "test"

def wordSearch(str):
   return str in dicArray

print("Test: If string test in smallDicSearch =", wordSearch(str))

# Build the string from the board - string is > 2 characters
# Search string not to repeat a square previously appended to string
# Test start square is row 1, col 1

row = 1
col = 1

searchStr = board[1][1] + board[0][1]

print("Test 2 char searchStr =", searchStr)
print("Test 2 char searchStr in reduced dictionary =", wordSearch(searchStr))



