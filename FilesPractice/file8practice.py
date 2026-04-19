# Complete the function to append the given new data to the specified file then print the contents of the file
def appendAndPrint(filename, newData):
    with open(filename, 'a') as f:
        f.write(newData)
    with open(filename, 'r') as f:
        contents = f.read()
        print(contents)
    # Student code goes here
 
# expected output: Hello World
with open("txtFiles/test.txt", 'w') as f: 
    f.write("Hello ")
appendAndPrint("txtFiles/test.txt", "World")