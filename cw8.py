# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Employee class inherits from Person
class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)
        self.employee_id = employee_id

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)


# PartTime class inherits from Person
class PartTime(Person):
    def __init__(self, name, age, working_hours):
        Person.__init__(self, name, age)
        self.working_hours = working_hours

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Working Hours:", self.working_hours)


# Consultant class inherits from Employee and PartTime
class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Working Hours:", self.working_hours)
        print("Project Name:", self.project_name)


# Creating objects
person = Person("Rahul", 30)
employee = Employee("Anita", 28, "EMP101")
parttime = PartTime("Kiran", 22, 5.5)
consultant = Consultant("Meera", 35, "CON201", 6.0, "Website Development")

# Displaying details
print("Person Details")
person.show_details()

print("\nEmployee Details")
employee.show_details()

print("\nPart-Time Worker Details")
parttime.show_details()

print("\nConsultant Details")
consultant.show_details()