import csv

class Student:
    def __init__(self, name, math, physics, geography):
        self.name = name
        self.math = self.validate_marks(math)
        self.physics = self.validate_marks(physics)
        self.geography = self.validate_marks(geography)

    def validate_marks(self, marks):
        if not (0 <= marks <= 50):
            raise ValueError("Marks should be between 0 and 50.")
        return marks

    def calculate_average(self):
        return round((self.math + self.physics + self.geography) / 3, 2)

    def calculate_percentage(self):
        return round((self.calculate_average() / 50) * 100, 2)

    def to_list(self):
        return [self.name, self.math, self.physics, self.geography, self.calculate_average(), self.calculate_percentage()]


students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    try:
        math = int(input("Enter Math marks: "))
        physics = int(input("Enter Physics marks: "))
        geography = int(input("Enter Geography marks: "))
        student = Student(name, math, physics, geography)
        students.append(student)
    except ValueError as e:
        print(f"Invalid input: {e}")
        exit()

print("\nStudent Details:")
for student in students:
    print(f"\nStudent Name: {student.name}")
    print(f"Math: {student.math}, Physics: {student.physics}, Geography: {student.geography}")
    print(f"Average Marks: {student.calculate_average()}")
    print(f"Percentage: {student.calculate_percentage()}%")


file_name = "students_data.csv"
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Math", "Physics", "Geography", "Average Marks", "Percentage"])
    for student in students:
        writer.writerow(student.to_list())

print(f"\nStudent data has been saved to '{file_name}'.")
