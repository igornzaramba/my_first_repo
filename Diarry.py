def read_diary(filename):

    try:
        with open(filename, 'r') as file:
            entries = file.read()
            print("Your diary entries:\n")
            print(entries)

    except FileNotFoundError:
        print("Diary file not found. Creating a new one.")
        with open(filename, 'w') as file:
            pass  # Create an empty file

def write_diary(filename):

    entry = input("Write your diary entry: ")
    with open(filename, 'a') as file:
        file.write(entry + "\n")
        print("Entry saved successfully!")

diary_filename = "my_diary.txt"

while True:
    print("\n1. Read previous entries")
    print("2. Write a new entry")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        read_diary(diary_filename)
    elif choice == '2':
        write_diary(diary_filename)
    elif choice == '3':
        print("Exiting the diary application. Have a great day!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

