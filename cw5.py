# Step 1: Create two sets
python_students = {"Asha", "Rahul", "Priya"}
data_science_students = {"Priya", "Kiran", "Meera"}

# Step 2: Add a new student to the Python set
python_students.add("Arun")

# Step 3: Remove one student from the Data Science set
data_science_students.remove("Meera")

# Step 4: Find students enrolled in both courses
common_students = python_students.intersection(data_science_students)
print("Students enrolled in both courses:", common_students)

# Step 5: Find students only in Python
python_only = python_students.difference(data_science_students)
print("Students only in Python:", python_only)

# Step 6: Display all students (no duplicates)
all_students = python_students.union(data_science_students)
print("All students:", all_students)

# Step 7: Create a dictionary with course names and student counts
courses = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

# Step 8: Print course name and number of students
for course, students in courses.items():
    print("Course: {}, Students: {}".format(course, students))

# Step 9: Create a new dictionary with doubled values
expected_growth = {course: students * 2 for course, students in courses.items()}

print("Expected Growth:", expected_growth)