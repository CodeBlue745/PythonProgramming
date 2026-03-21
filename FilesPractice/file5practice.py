import os

# Complete the function to print all files in the given directory
def printFiles(someDirectory):
    for item in os.listdir(someDirectory):
        if os.path.isfile(os.path.join(someDirectory, item)):#checks if the item in the directory is a file
            print(item)
    # Student code goes here
    
# expected output: main.py    
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())