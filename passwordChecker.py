''' Type your code here. SDR 2026-04-28
This program checks if a password is valid. A valid password must be at least 8 characters long, contain at least one letter, at least one number, and at least one of the following special characters: !, #, %. The program should print "OK" if the password is valid. If the password is invalid, the program should print all of the reasons why it is invalid. For example, if the password is too short and missing a number, the program should print:
Too short'''
potentialPass = input()
lenFlag = False
lettFlag = False
numFlag = False
specFlag = False


if len(potentialPass) >= 8:
    lenFlag = True
for i in potentialPass:
    if ord(i) >= 65:
        lettFlag = True
    elif ord(i) >= 48 and ord(i) <= 57:
        numFlag = True
    elif ord(i) == 33 or ord(i) == 35 or ord(i) == 37:
        specFlag = True
if lenFlag == True and lettFlag == True and numFlag == True and specFlag == True:
    print('OK')
if lenFlag == False:
    print('Too short')
if lettFlag == False:
    print('Missing letter')
if numFlag == False:
    print('Missing number')
if specFlag == False:
    print('Missing special')