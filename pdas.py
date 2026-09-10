# Placement Data Analysis System - Version 1.1
# Features: Student data, average package calculation

students = []

def add_student(name, branch, package):
    students.append({
        "name": name,
        "branch": branch,
        "package": package
    })
    print("Student data added successfully.")

def display_students():
    print("\nPlacement Data:")
    for student in students:
        print(student["name"], "-", student["branch"],
              "-", student["package"], "LPA")

def calculate_average_package():
    if len(students) == 0:
        print("No data available.")
        return

    total = sum(student["package"] for student in students)
    average = total / len(students)

    print("Average Package =", average, "LPA")

add_student("Rahul", "Computer", 6.5)
add_student("Aman", "IT", 8.0)
add_student("Sameer", "Computer", 10.0)

display_students()
calculate_average_package()
