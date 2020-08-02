# Main program to parse a text file containing words and its meanings and printing those as output

from collections import defaultdict


# Function to check if file exists on the path provided
def doesFileExist(path):
    try:
        filePointer = open(path, 'r')
        return filePointer
    except FileNotFoundError:
        print("File does not exist on the path specified!")
        exit()


# Function to parse the test_input.txt file and output
# the terms and its meaning
def readingDictionary(pointerToFile):
    myDictionary = defaultdict(int)
    for line in pointerToFile:
        # splitting the terms by '-'
        (key, val) = line.split('-')
        myDictionary[key] = val
    for terms in myDictionary:
        print(terms)
        # splitting the different meaning separated  by ','
        meanings = myDictionary[terms].split(',')
        for i in meanings:
            print(i)


# Calling functions
fileHandle = doesFileExist("test_input.txt")
readingDictionary(fileHandle)
