import os

# Complete the function to return the file name part only from the given file name
def getFileName(fileName):
    return os.path.basename(fileName)
    # Student code goes here
 
# expected output: test.html
print(getFileName("/var/www/test.html"))
 
# expected output: names.txt
print(getFileName("/var/www/apple/names.txt"))