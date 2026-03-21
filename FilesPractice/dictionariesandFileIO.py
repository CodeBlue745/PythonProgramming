'''
Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. The input file contains an unsorted list of number of seasons followed by the corresponding TV show. Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a Python list of TV shows are the values (since multiple shows could have the same number of seasons).

Sort the dictionary by key (greatest to least) and output the results to a file named output_keys.txt. Separate multiple TV shows associated with the same key with a semicolon (;), ordering by appearance in the input file. Next, sort the dictionary by values (in reverse alphabetical order), and output the results to a file named output_titles.txt.
'''

# Type your code here
getInput = input()#txtFiles/file1.txt or txtFiles/file2.txt
newDict = {}
with open(getInput, 'r') as readFile:
    readData = readFile.readlines()
    for data in range(0, len(readData), 2):
        key = readData[data].strip()
        value = readData[data + 1].strip()
        if key in newDict:#check if the key already exists in the dictionary
            newDict[key].append(value)#append the value to the existing list
        else:
            newDict[key] = [value]#create a new list entry with the value if the key does not exist in the dictionary
    print(newDict)
    sortedDict = sorted(newDict.items(), key=lambda x: int(x[0]), reverse=True)
with open('txtFiles/output_keys.txt', 'w') as writeFile:
    for key, value in sortedDict:
        writeFile.write(f'{key}: {"; ".join(value)}\n')
with open('txtFiles/output_titles.txt', 'w') as writeFile:
    sortedByValues = sorted(newDict.values(), key=lambda x: x[0], reverse=True)
    for value in sortedByValues:
        if len(value) == 2:
            writeFile.write(f'{value[1]}\n{value[0]}\n')
        else:
            writeFile.write(f"{''.join(value)}\n")    