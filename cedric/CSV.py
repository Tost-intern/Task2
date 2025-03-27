import csv

class Student:
    def __init__(self, name, math, physics, geography):
        self.name = name
        self.math = math
        self.physics = physics
        self.geography = geography

    def calculate_average(self):
        return (self.math + self.physics + self.geography) / 3

    def calculate_percentage(self):
        return (self.calculate_average() / 50) * 100

# Get number of students
num_students = int(input("Enter the number of students: "))
students = []

for _ in range(num_students):
    name = input("Enter student name: ")
    math = float(input("Enter Math marks (out of 50): "))
    physics = float(input("Enter Physics marks (out of 50): "))
    geography = float(input("Enter Geography marks (out of 50): "))
    student = Student(name, math, physics, geography)
    students.append(student)

# Save data to CSV file
with open("students_data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Math", "Physics", "Geography", "Average", "Percentage"])
    for student in students:
        writer.writerow([student.name, student.math, student.physics, student.geography, 
                         round(student.calculate_average(), 2), round(student.calculate_percentage(), 2)])

print("Student data saved to students_data.csv successfully!")
