'''
Example calls:
educate
c

happy
a


'''

synonyms = {}   # Define dictionary
count = 0
import math
# Type your code here
fileName = input()
firstLetter = input()

with open(fileName + '.txt', 'r') as readPage:
    for lineNum, line in enumerate(readPage):
        if line[0].find(firstLetter) == 0:
            for word in line.split(' '):
                print(word)
        elif line[0].find(firstLetter) == -1:
            count += 1
    if count == lineNum + 1:
        print(f'No synonyms for {fileName} begin with {firstLetter}.')

