size = 5

def get_numbers(num):
    numbers = []
    user_input = input(f'Enter {num} integers:\n') #Format of input: 23 -5 0 12 -8

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list
        
        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    #allNum_string.join(numbers)
    allNum_list = []
    for value in numbers:
        allNum_list.append(str(value))
    allNum_string = ' '.join(allNum_list)
    print(f'Numbers: {allNum_string}')

def print_odd_numbers(numbers):
    oddNum_list = []
    for value in numbers:
        if value % 2 == 0:
            continue
        else:
            oddNum_list.append(str(value))
    oddNum_string = ' '.join(oddNum_list)
        
    # Print all odd numbers
    print(f'Odd numbers: {oddNum_string}')

def print_negative_numbers(numbers):
    negNum_list = []
    for value in numbers:
        if value >= 0:
            continue
        else:
            negNum_list.append(str(value))
    negNum_string = ' '.join(negNum_list)
    
    # Print all negative numbers
    print(f'Negative numbers: {negNum_string}')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
