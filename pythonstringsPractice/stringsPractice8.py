# Complete the function to remove trailing spaces from the first string
# and leading spaces from the second string and return the combined strings
def removeSpaces(string1, string2):
# Student code goes here
    lstriped = string2.lstrip()
    rstriped = string1.rstrip()
    return rstriped + lstriped
# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))
    
# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))