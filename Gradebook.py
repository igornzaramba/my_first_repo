def read_grades(filename):
    try:
        with open(filename, 'r') as file:
            grades = [float(line.strip()) for line in file]
            return grades
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new one.")
        return []

def write_grades(filename, grades):
    with open(filename, 'w') as file:
        for grade in grades:
            file.write(f"{grade:.2f}\n")
        print("Grades saved successfully!")

def calculate_average(grades):
    if not grades:
        return None
    total = sum(grades)
    return total / len(grades)


grade_filename = "my_grades.txt"

grades = read_grades(grade_filename)

while True:
    print("\n1. Add a new grade")
    print("2. View existing grades")
    print("3. Calculate average grade")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        try:
            new_grade = float(input("Enter the new grade: "))
            grades.append(new_grade)
            write_grades(grade_filename, grades)
        except ValueError:
            print("Invalid input. Please enter a valid numeric grade.")
    elif choice == '2':
        print("Existing grades:")
        for grade in grades:
            print(f"{grade:.2f}")
    elif choice == '3':
        average = calculate_average(grades)
        if average is not None:
            print(f"Average grade: {average:.2f}")
        else:
            print("No grades available.")
    elif choice == '4':
        print("Exiting the grade tracker. Have a great day!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

