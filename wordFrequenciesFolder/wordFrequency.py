'''
SDR
Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method. The file contains a list of words separated by commas. The program must output the words and their frequencies (the number of times each word appears in the file) without any duplicates. The output should be in the format: word - frequency. You may assume that the file is not empty and that it contains only words separated by commas. You may also assume that the words are case-sensitive (i.e., "Word" and "word" are considered different words).
'''

'''
example input: wordFrequenciesFolder/input1.csv

contents of input1.csv: apple,banana,apple,orange,banana,grape

example output:
apple - 2
banana - 2
orange - 1
grape - 1
'''

import csv

# Type your code here. 
fileName = input()
outputNum = []
outputWord = []
with open(fileName, 'r') as csvFile:
    readcsvFile = csv.reader(csvFile)
    for line in readcsvFile:
        #print(line)
        for word in line:
            #line.count(word)
            if word not in outputWord:
                outputWord.append(word)
                outputNum.append(line.count(word))

for key, i in enumerate(outputWord):
    print(f'{i} - {outputNum[key]}')
#print(outputWord)
#print(outputNum)

#for line in readFile:
#    print(line)
#splitatComma = readFile.split(',')
#print(readFile)