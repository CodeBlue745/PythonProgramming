# Complete the function to print every key and value
def printDict(mydict):
# Student code goes here
    for i in mydict:
        print(f'{i}={mydict[i]}')
# expected output: 
#        tomato=red
#        banana=yellow
#        lime=green
printDict({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'})
 
# expected output: 
#        Brazil=Brasilia
#        Ireland=Dublin
#        Indonesia=Jakarta
printDict({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'})