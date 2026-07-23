# Base class
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)


# Trainer class inherits from Employee
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        Employee.__init__(self, name, role)
        self.specialization = specialization

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)


# YogaInstructor class inherits from Employee
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        Employee.__init__(self, name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)


# MultiTrainer class inherits from Trainer and YogaInstructor
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)


# Creating objects
employee = Employee("Ravi", "Receptionist")
trainer = Trainer("Anita", "Trainer", "Strength Training")
yoga = YogaInstructor("Meera", "Yoga Instructor", "Hatha Yoga")
multi = MultiTrainer("Arjun", "Multi Trainer", "Cardio", "Vinyasa Yoga")

# Displaying details
print("Employee Details")
employee.display()

print("\nTrainer Details")
trainer.display()

print("\nYoga Instructor Details")
yoga.display()

print("\nMulti Trainer Details")
multi.display()