# Complete the function to read the contents of the specified file and print the contents
def printFileContents(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        print(contents)
    # Student code goes here

# expected output: Hello
with open("test.txt", 'w') as f: 
    f.write("Hello")
printFileContents("test.txt")