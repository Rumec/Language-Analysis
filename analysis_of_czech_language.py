"""
This program makes analysis of occurrence of individual letters in czech language.

Author: Dominik Rumian
03-21-2019
"""

import operator
import matplotlib.pyplot as plt

def readFile(nameOfFile):
    file = open(nameOfFile, "r")
    letters = {}
    letterCount = 0
    for line in file:
        for char in line:
            if char.isalpha():
                letters[char.lower()] = letters.get(char.lower(), 0) + 1
                letterCount += 1
    file.close()
    print(letterCount)
    return letters

def letterAnalysis(dictOfLetters):
    lettersKeys = dictOfLetters.keys()
    lettersTupleList = []
    # Sorting letters according their occurrence in the text
    for key in lettersKeys:
        lettersTupleList.append((key, letters[key]))
    lettersTupleList.sort(key = operator.itemgetter(1), reverse = True)
    return lettersTupleList


def createPlotData(tupleList):
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

def plotToPDF(xAxisLabels, yAxisValues, xAxisPositions, xDimension, yDimension):
    # Setting the dimensions of a graph in hundreds of pixels (width x height)
    plt.figure(figsize=(xDimension, yDimension))
    # Plotting the graph
    plt.bar(xAxisPositions, yAxisValues, tick_label=xAxisLabels, width=0.8, color=['red', 'green', 'blue'])
    # Naming the x-axis
    plt.xlabel('Písmeno')
    # Naming the y-axis
    plt.ylabel('Počet výskytů')
    # Plot title
    plt.title('Výskyty písmen v češtině')
    # Printing to PDF file
    plt.savefig('Vyskyt_pismen.pdf', format='pdf')



letters = readFile("bible.txt")
tupleList = letterAnalysis(letters)
(letters, values, positions) = createPlotData(tupleList)
plotToPDF(letters, values, positions, 14, 6)



