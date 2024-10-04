#imports
import csv

#reading student data
def read_students(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        students = list(reader)
    return students

#calculating average grade for all students
def calculate_average_grade(students):
    total_grade = 0
    for student in students:
        total_grade += float(student['grade'])
    average_grade = total_grade / len(students)
    return average_grade

#finding the student with the higest grade
def find_highest_grade_student(students):
    highest_grade = -1
    top_student = None
    for student in students:
        if float(student['grade']) > highest_grade:
            highest_grade = float(student['grade'])
            top_student = student
    return top_student

def main():
    filename = 'students.csv'
    students = read_students(filename)
    
    average_grade = calculate_average_grade(students)
    top_student = find_highest_grade_student(students)
    
    print(f"Average Grade: {average_grade:.2f}")
    if top_student:
        print(f"Top Student: {top_student['name']} with a grade of {top_student['grade']}")

if __name__ == "__main__":
    main()
