
""" Your solution goes here """
def number_of_pennies(numDoleros, numPennies=0):
    totalPennies = numDoleros * 100 + numPennies
    return totalPennies
    # if numPennies < 10:
    #     print(f'{numDoleros}0{numPennies}', end='')
    # elif numPennies < 100:
    #     print(f'{numDoleros}{numPennies}', end='')
    # else:
    #     numDoleros += numPennies % 100
    #     numPennies = numPennies // 100
    #     print(f'{numDoleros}{numPennies}', end='')



print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))         