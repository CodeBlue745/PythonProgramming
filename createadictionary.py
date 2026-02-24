# Create a dictionary to store patient data, where the key is the patient's name and the value is their age.
#Example input:
# John 25
# Jane 30
# The program should read input until the user types 'end', and then print the dictionary.

patients_data = {}

getInput = input()
while getInput != 'end':
    readInput = getInput.split()
    patients_data[readInput[0]] = int(readInput[1])
    
    
    getInput = input()



print('Patients data:')
print(patients_data)