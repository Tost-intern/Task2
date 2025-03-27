
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
        total_marks = self.math + self.physics + self.geography
        max_marks = 50 * 3  # 50 marks per subject * 3 subjects
        return (total_marks / max_marks) * 100

def validate_marks(marks):
    try:
        marks = float(marks)
        if 0 <= marks <= 50:
            return True
        print("Marks should be between 0 and 50")
        return False
    except ValueError:
        print("Please enter a valid number")
        return False

def main():
    students = []
    
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students > 0:
                break
            print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
    
    for i in range(num_students):
        print(f"\nEnter details for student {i+1}:")
        name = input("Enter name: ")
        
        while True:
            math = input("Enter Math marks (0-50): ")
            if validate_marks(math):
                math = float(math)
                break
                
        while True:
            physics = input("Enter Physics marks (0-50): ")
            if validate_marks(physics):
                physics = float(physics)
                break
                
        while True:
            geography = input("Enter Geography marks (0-50): ")
            if validate_marks(geography):
                geography = float(geography)
                break
        
        students.append(Student(name, math, physics, geography))
    
    # Display student details and save to CSV
    with open('students_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Math', 'Physics', 'Geography', 'Average', 'Percentage'])
        
        print("\nStudent Details:")
        for student in students:
            average = student.calculate_average()
            percentage = student.calculate_percentage()
            
            print(f"\nStudent Name: {student.name}")
            print(f"Math: {student.math}, Physics: {student.physics}, Geography: {student.geography}")
            print(f"Average Marks: {average:.2f}")
            print(f"Percentage: {percentage:.2f}%")
            
            writer.writerow([
                student.name,
                student.math,
                student.physics,
                student.geography,
                f"{average:.2f}",
                f"{percentage:.2f}%"
            ])
    
    print("\nStudent data has been saved to 'students_data.csv'")

if __name__ == "__main__":
    main()
