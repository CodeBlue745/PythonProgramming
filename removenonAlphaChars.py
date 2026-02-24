userinput = input()

newString = ''
for i in userinput:
    if i.isalpha():
        newString += i
print(newString)