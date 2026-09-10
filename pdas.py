# Placement Data Analysis System - Version 2.0
# Features: Student data, average package, branch-wise analysis

students = []

def add_student(name, branch, package):
    students.append({
        "name": name,
        "branch": branch,
        "package": package
    })

def display_students():
    print("\n--- Placement Data ---")
    for student in students:
        print(
            "Name:", student["name"],
            "| Branch:", student["branch"],
            "| Package:", student["package"], "LPA"
        )

def calculate_average_package():
    if not students:
        print("No placement data available.")
        return

    total = sum(student["package"] for student in students)
    average = total / len(students)

    print("\nOverall Average Package:", round(average, 2), "LPA")

def branch_analysis():
    branches = {}

    for student in students:
        branch = student["branch"]

        if branch not in branches:
            branches[branch] = []

        branches[branch].append(student["package"])

    print("\n--- Branch-wise Analysis ---")

    for branch, packages in branches.items():
        average = sum(packages) / len(packages)
        highest = max(packages)

        print("Branch:", branch)
        print("Students Placed:", len(packages))
        print("Average Package:", round(average, 2), "LPA")
        print("Highest Package:", highest, "LPA")
        print()

# Sample data
add_student("Rahul", "Computer", 6.5)
add_student("Aman", "IT", 8.0)
add_student("Sameer", "Computer", 10.0)
add_student("Zaid", "Mechanical", 5.5)
add_student("Rohan", "IT", 7.0)

display_students()
calculate_average_package()
branch_analysis()
