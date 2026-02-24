# Complete the function to add num1 to the front of the given list
def addToFront(mylist, num1):
# Student code goes here
    mylist.insert(0, num1)
    return mylist
 
# expected output: [3, 4, 5, 6]
print(addToFront([4,5,6], 3))
 
# expected output: [10, 9, 8, 7]
print(addToFront([9,8,7], 10))