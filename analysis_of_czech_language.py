"""
This program makes analysis of occurrence of individual letters in czech language.

Author: Dominik Rumian
03-21-2019
"""

import operator
import matplotlib.pyplot as plt
import time

def readFile(nameOfFile, letters):
    """
    Reads file and stores data about letter count in dictionary letters
    :param nameOfFile: string, name of file to be analyzed
    :param letters: dictionary, containing count of individual letters
    :return: void
    """
    file = open(nameOfFile, "r")
    letterCount = 0
    for line in file:
        for char in line:
            if char.isalpha():
                letters[char.lower()] = letters.get(char.lower(), 0) + 1
                letterCount += 1
    file.close()
    print(letterCount)

def letterAnalysis(dictOfLetters):
    """
    Converts dictionary to list of tuples, this list is sorted by descending order
    :param dictOfLetters: dictionary
    :return: sorted list of tuples in format (letter, count)
    """
    lettersKeys = dictOfLetters.keys()
    lettersTupleList = []
    # Sorting letters according their occurrence in the text
    for key in lettersKeys:
        lettersTupleList.append((key, dictOfLetters[key]))
    lettersTupleList.sort(key = operator.itemgetter(1), reverse = True)
    return lettersTupleList


def createPlotDataAllLetters(tupleList):
    letters = []
    values = []
    positions = []
    i = 1

    for tup in tupleList:
        letters.append(tup[0])
        values.append(tup[1])
        positions.append(i)
        i += 1

    return letters, values, positions


def createPlotDataVowels(tupleList):
    vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'ě', 'í', 'ó', 'ú', 'ů', 'y', 'ý']
    vowelsCount = []
    vowelsValues = []
    vowelsPositions = []
    i = 1

    for tup in tupleList:
        if tup[0] in vowels:
            vowelsCount.append(tup[0])
            vowelsValues.append(tup[1])
            vowelsPositions.append(i)
            i += 1

    return vowelsCount, vowelsValues, vowelsPositions

def createPlotDataConsonants(tupleList):
    vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'ě', 'í', 'ó', 'ú', 'ů', 'y', 'ý']
    consonantsCount = []
    consonantsValues = []
    consonantsPositions = []
    i = 1

    for tup in tupleList:
        if tup[0] not in vowels:
            consonantsCount.append(tup[0])
            consonantsValues.append(tup[1])
            consonantsPositions.append(i)
            i += 1

    return consonantsCount, consonantsValues, consonantsPositions

def plotToPDF(xAxisLabels, yAxisValues, xAxisPositions, xDimension, yDimension, title):
    # Setting the dimensions of a graph in hundreds of pixels (width x height)
    plt.figure(figsize=(xDimension, yDimension))
    # Plotting the graph
    plt.bar(xAxisPositions, yAxisValues, tick_label=xAxisLabels, width=0.8, color=['red', 'green', 'blue'])
    # Naming the x-axis
    plt.xlabel('Písmeno')
    # Naming the y-axis
    plt.ylabel('Počet výskytů')
    # Plot title
    plt.title(title)
    # Printing to PDF file
    title = title + ".pdf"
    plt.savefig(title, format='pdf')

def main():
    # Starting point of time in the beginning
    start = time.time()

    letters = {}
    # List of books to be analyzed
    books = ["bible.txt"]

    for book in books:
        readFile(book, letters)
    tupleList = letterAnalysis(letters)

    # Plots graph for all letters
    (letters, values, positions) = createPlotDataAllLetters(tupleList)
    plotToPDF(letters, values, positions, 14, 6, "All_letters")
    # Plots graph for vowels
    (letters, values, positions) = createPlotDataVowels(tupleList)
    plotToPDF(letters, values, positions, 14, 6, "Vowels_Only")
    # Plots graph for consonants
    (letters, values, positions) = createPlotDataConsonants(tupleList)
    plotToPDF(letters, values, positions, 14, 6, "Consonants_Only")

    # Ending point of program run
    end = time.time()
    print("Time of running: ", end - start)

main()



