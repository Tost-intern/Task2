import csv
import os

class Student:
    MAX_MARKS = 50  # Maximum marks per subject
    
    def __init__(self, name, math, physics, geography):
        self.name = name
        self.math = self._validate_marks(math, "Math")
        self.physics = self._validate_marks(physics, "Physics")
        self.geography = self._validate_marks(geography, "Geography")
    
    def _validate_marks(self, marks, subject):
        """Validate that marks are numeric and within range"""
        try:
            marks = float(marks)
            if 0 <= marks <= self.MAX_MARKS:
                return marks
            else:
                raise ValueError(f"{subject} marks must be between 0 and {self.MAX_MARKS}")
        except ValueError as e:
            raise ValueError(f"Invalid input for {subject}: {str(e)}")
    
    def calculate_average(self):
        """Calculate average marks across all subjects"""
        total = self.math + self.physics + self.geography
        return round(total / 3, 2)
    
    def calculate_percentage(self):
        """Calculate percentage based on total possible marks"""
        total_obtained = self.math + self.physics + self.geography
        total_possible = self.MAX_MARKS * 3
        return round((total_obtained / total_possible) * 100, 2)

def get_student_input():
    """Get student details from user with validation"""
    while True:
        try:
            name = input("Enter student name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty")
            
            math = input("Enter Math marks (0-50): ")
            physics = input("Enter Physics marks (0-50): ")
            geography = input("Enter Geography marks (0-50): ")
            
            # Create student object to validate inputs
            student = Student(name, math, physics, geography)
            return student
            
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def save_to_csv(students, filename="students_data.csv"):
    """Save student data to CSV file"""
    headers = ["Name", "Math", "Physics", "Geography", "Average", "Percentage"]
    
    # Check if file exists to determine if we need headers
    file_exists = os.path.exists(filename)
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers if file is new
        if not file_exists:
            writer.writerow(headers)
        
        # Write student data
        for student in students:
            writer.writerow([
                student.name,
                student.math,
                student.physics,
                student.geography,
                student.calculate_average(),
                student.calculate_percentage()
            ])

def display_student_details(student):
    """Display formatted student information"""
    print(f"\nStudent: {student.name}")
    print(f"Math: {student.math}")
    print(f"Physics: {student.physics}")
    print(f"Geography: {student.geography}")
    print(f"Average Marks: {student.calculate_average()}")
    print(f"Percentage: {student.calculate_percentage()}%")
    print("-" * 40)

def main():
    print("=== Student Marks Management System ===")
    
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students <= 0:
                raise ValueError("Number must be positive")
            break
        except ValueError:
            print("Please enter a valid positive number")
    
    students = []
    
    # Get input for each student
    for i in range(num_students):
        print(f"\nEntering details for student {i + 1}:")
        student = get_student_input()
        students.append(student)
    
    # Display details and save to CSV
    print("\n=== Student Results ===")
    for student in students:
        display_student_details(student)
    
    save_to_csv(students)
    print(f"Data saved to students_data.csv successfully!")

if __name__ == "__main__":
    main()