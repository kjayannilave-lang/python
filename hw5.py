# Step 1: Create two sets
frontend_students = {"Asha", "Rahul", "Priya"}
backend_students = {"Priya", "Kiran", "Arun"}

# Step 2: Add a new student to the Backend course
backend_students.add("Meera")

# Step 3: Remove a student from the Frontend course
frontend_students.remove("Rahul")

# Step 4: Display students enrolled in both courses
common_students = frontend_students.intersection(backend_students)
print("Students enrolled in both courses:", common_students)

# Step 5: Display students enrolled only in Backend
backend_only = backend_students.difference(frontend_students)
print("Students only in Backend:", backend_only)

# Step 6: Display the total number of unique students
all_students = frontend_students.union(backend_students)
print("Total unique students:", len(all_students))

# Step 7: Create a dictionary with course names and student counts
courses = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

# Step 8: Print each course name and number of students
for course, count in courses.items():
    print("Course: {}, Students: {}".format(course, count))

# Step 9: Create a new dictionary using dictionary comprehension
updated_courses = {
    key: value for key, value in courses.items()
}

updated_courses["Fullstack"] = (
    courses["Frontend"] + courses["Backend"]
)

print("Updated Course Dictionary:", updated_courses)