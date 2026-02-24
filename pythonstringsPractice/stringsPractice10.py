# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
# Student code goes here
    count = 0
    for char in mystring:
        if char.isupper():
            count += 1
    return count
# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary'))