import os

# Complete the function to create the specified file and return the file name
def createFile(filename):
    with open(filename, 'w') as f:
        f.write("")
    return filename
    # Student code goes here
 
# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))