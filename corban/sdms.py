import csv

# Define the Student class
class Student:
    def __init__(self, name, math, physics, geography):
        self.name = name
        self.math = math
        self.physics = physics
        self.geography = geography

    def calculate_average(self):
        return (self.math + self.physics + self.geography) / 3

    def calculate_percentage(self):
        total_marks = self.math + self.physics + self.geography
        return (total_marks / 150) * 100  # Maximum marks are 150 (50 per subject)

# Function to write data to a CSV file
def save_to_csv(students):
    with open("students_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Math Marks", "Physics Marks", "Geography Marks", "Average", "Percentage"])

        for student in students:
            writer.writerow([
                student.name,
                student.math,
                student.physics,
                student.geography,
                student.calculate_average(),
                student.calculate_percentage()
            ])
        print("Data has been saved to students_data.csv.")

# Main program
def main():
    students = []

    # Get the number of students
    num_students = int(input("Enter the number of students: "))

    # Get input for each student
    for _ in range(num_students):
        name = input("Enter student's name: ")
        math = int(input("Enter Math marks (out of 50): "))
        physics = int(input("Enter Physics marks (out of 50): "))
        geography = int(input("Enter Geography marks (out of 50): "))

        # Create a Student object and add it to the list
        student = Student(name, math, physics, geography)
        students.append(student)

        # Display average and percentage
        print(f"\n{name}'s Average Marks: {student.calculate_average()}")
        print(f"{name}'s Percentage: {student.calculate_percentage()}%\n")

    # Save all student data to a CSV file
    save_to_csv(students)

# Run the program
if __name__ == "__main__":
    main()
