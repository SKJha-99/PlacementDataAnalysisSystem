# Placement Data Analysis System - Version 1.0
# Feature: Add and display student placement data

students = []

def add_student(name, branch, package):
    student = {
        "name": name,
        "branch": branch,
        "package": package
    }
    students.append(student)
    print("Student data added successfully.")

def display_students():
    print("\nPlacement Data:")
    for student in students:
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Package: Rs.", student["package"], "LPA")
        print()

add_student("Rahul", "Computer", 6.5)
add_student("Aman", "IT", 8.0)

display_students()
