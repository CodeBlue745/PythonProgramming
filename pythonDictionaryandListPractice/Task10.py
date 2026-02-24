# Complete the function to return a dictionary value 
# if it exists or return Not Found if it doesn't exist
def findDictItem(mydict, key):
# Student code goes here
    if key in mydict:
        return mydict[key]
    else:
        return "Not Found"
# expected output: yellow
print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: Not Found
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'},'Cameroon'))