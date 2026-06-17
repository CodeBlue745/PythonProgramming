''' Enter the amount of change as an integer representing the number of cents.
The program should then print the minimum number of dollars, quarters, dimes, nickels, and pennies needed to make that amount of change.
For example, if the user enters 92, the program should print:
3 Quarters
1 Dime
1 Nickel
2 Pennies'''
amountInteger = int(input())
flag = False

dollar = amountInteger // 100
print(f'{dollar} Dollar(s)')
amountInteger %= 100
quarter = amountInteger // 25
amountInteger %= 25
print(f'{quarter} Quarter(s)')
dime = amountInteger // 10
amountInteger %= 10
print(f'{dime} Dime(s)')
nickel = amountInteger // 5
amountInteger %= 5
print(f'{nickel} Nickel(s)')
print(f'{amountInteger} Penny(s)')

'''
while flag == False:
    if amountInteger == 0:
        print('No change')
        flag = True
    elif amountInteger == 1:
        print('1 Penny')
        flag = True
    elif amountInteger > 1 and amountInteger < 5:
        print(f'{amountInteger} Pennies')
        flag = True
    elif amountInteger == 5:
        print('1 Nickel')
        flag = True
    elif amountInteger > 5 and amountInteger < 10:
        print('1 Nickel')
        amountInteger -= 5
        continue
    elif amountInteger == 10:
        print('1 Dime')
        flag = True
    elif amountInteger > 10 and amountInteger < 20:
        print('1 Dime')
        amountInteger -= 10
        continue
    elif amountInteger == 20:
        print('2 Dimes')
        flag = True
    elif amountInteger > 20 and amountInteger < 25:
        print('2 Dimes')
        amountInteger -= 20
        continue
    elif amountInteger == 25:
        print('1 Quarter')
        flag = True
    elif amountInteger > 25 and amountInteger < 50:
        print('1 Quarter')
        amountInteger -= 25
        continue
    elif amountInteger == 50:
        print('2 Quarters')
        flag = True
    elif amountInteger > 50 and amountInteger < 75:
        print('2 Quarters')
        amountInteger -= 50
        continue
    elif amountInteger == 75:
        print('3 Quarters')
        flag = True
    elif amountInteger > 75 and amountInteger < 100:
        print('3 Quarters')
        amountInteger -= 75
        continue
    elif amountInteger // 100 == 1:
        print('1 Dollar')
        amountInteger -= 100
        continue
    elif amountInteger // 100 > 1:
        print(f'{amountInteger // 100} Dollars')
        #amountInteger -= ((amountInteger // 100) * 100)
        amountInteger = amountInteger % 100
        if amountInteger == 0:
            flag = True
        continue
'''