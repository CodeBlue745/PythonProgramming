def add_grade(student_grades):
    print('Entering grade. \n')
    try:
        name, grade = input(grade_prompt).split()
        student_grades[name] = grade
    except ValueError:
        print(f'Invalid input. ', end='')
        add_grade(student_grades)  # Retry on invalid input
    print()  # Print a blank line after adding grade

# FIXME: Create delete_name function
def delete_name():
    print('Deleting grade.\n')
    name = input(delete_prompt)
    if name in student_grades: # Check if name exists
        del student_grades[name]
    else:
        print(f'{name} not found.')
    print()  # Print a blank line after deletion

# FIXME: Create print_grades function
def print_grades():
    print('Printing grades.\n')
    for name, grade in student_grades.items():
        print(f'{name} has a {grade}.')
    print()  # Print a blank line after all grades
student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
delete_prompt = "Enter name to delete:\n"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n\n")
minified_menu_prompt = "Enter 1, 2, 3, or 4:\n"

command = input(menu_prompt).lower().strip()

while command != '4':  # Exit when user enters '4'
    if command == '1':
        add_grade(student_grades)
    elif command == '2':
        # FIXME: Only call delete_name() here
        delete_name()
    elif command == '3':
        # FIXME: Only call print_grades() here
        print_grades()
    else:
        print('Unrecognized command.\n')

    command = input(minified_menu_prompt).lower().strip()
