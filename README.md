# Student Marks Management System

## Objective

Develop a Python program using **Object-Oriented Programming (OOP)** to manage student marks in three subjects: **Math, Physics, and Geography**. **Max marks on every course is 50**. The program should calculate each student's **average marks** and **percentage**, then save the data to a **CSV file**.

## Requirements

1. **Create a `Student` class** with the following:

   - Attributes:
     - `name` (Student's name)
     - `math` (Math marks)
     - `physics` (Physics marks)
     - `geography` (Geography marks)
   - Methods:
     - `calculate_average()` – Computes the average marks of the student.
     - `calculate_percentage()` – Computes the percentage.
2. **User Input:**

   - Allow the user to enter the number of students.
   - Take input for each student's name and their marks.
3. **Data Processing:**

   - Calculate and display the **average marks** and **percentage** for each student.
4. **File Handling:**

   - Save the student details (name, marks, average, and percentage) into a CSV file (`students_data.csv`).

## Expected Output

```
Enter number of students: 2  

Enter name of student 1: Alice  
Enter Math marks: 85  
Enter Physics marks: 78  
Enter Geography marks: 90  

Enter name of student 2: Bob  
Enter Math marks: 92  
Enter Physics marks: 88  
Enter Geography marks: 81  

Student Details:  
Student Name: Olga  
Math: 85, Physics: 78, Geography: 90  
Average Marks: 84.33  
Percentage: 84.33%  

Student Name: Bob  
Math: 92, Physics: 88, Geography: 81  
Average Marks: 87.00  
Percentage: 87.00%  

Student data has been saved to 'students_data.csv'.
```

## Guidelines

- Use **OOP principles** such as **encapsulation** and **methods**.
- Implement **file handling** to store student details in CSV format.
- Validate inputs (e.g., marks should be numeric and within 0-100).

📌 **Submit your completed Python script.** 🚀
