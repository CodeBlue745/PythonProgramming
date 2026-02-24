nameInput = input()
def processInitials(nameInput):
    namesList = nameInput.split()
    if len(namesList) == 3:
        return f'{namesList[2]}, {namesList[0][0]}.{namesList[1][0]}.'
    elif len(namesList) == 2:
        return f'{namesList[1]}, {namesList[0][0]}.'
print(processInitials(nameInput))