import csv

class Student:
    def __init__(self, name, math, physics, geography):
        self.name = name
        self.math = self.validate_marks(math)
        self.physics = self.validate_marks(physics)
        self.geography = self.validate_marks(geography)
    
    def validate_marks(self, marks):
        if not (0 <= marks <= 50):
            raise ValueError("Marks should be between 0 and 50")
        return marks
    
    def calculate_average(self):
        return round((self.math + self.physics + self.geography) / 3, 2)
    
    def calculate_percentage(self):
        return round((self.math + self.physics + self.geography) / 150 * 100, 2)
    
    def get_student_details(self):
        return [self.name, self.math, self.physics, self.geography, self.calculate_average(), self.calculate_percentage()]

def get_student_data(predefined_data=None):
    students = []
    if predefined_data:
        for data in predefined_data:
            students.append(Student(*data))
        return students
    
    num_students = 2  # Default number of students for testing in sandbox
    sample_data = [("Alice", 45, 40, 48), ("Bob", 38, 42, 39)]
    
    for data in sample_data:
        students.append(Student(*data))
    
    return students

def save_to_csv(students, filename='students_data.csv'):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Math", "Physics", "Geography", "Average Marks", "Percentage"])
            for student in students:
                writer.writerow(student.get_student_details())
        print(f"\nStudent data has been saved to '{filename}'.")
    except OSError as e:
        print(f"Error saving to file: {e}")

def main():
    students = get_student_data()
    print("\nStudent Details:")
    for student in students:
        print(f"\nStudent Name: {student.name}")
        print(f"Math: {student.math}, Physics: {student.physics}, Geography: {student.geography}")
        print(f"Average Marks: {student.calculate_average()}")
        print(f"Percentage: {student.calculate_percentage()}%")
    
    save_to_csv(students)

if __name__ == "__main__":
    main()
