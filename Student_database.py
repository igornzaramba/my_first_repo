class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return None


student1 = Student("Igor", 20, [85, 90, 78])
student2 = Student("Kimberley", 21, [92, 88, 95])

# Display student information
student1.display_info()
print(f"Average Grade: {student1.calculate_average():.2f}\n")

student2.display_info()
print(f"Average Grade: {student2.calculate_average():.2f}")

