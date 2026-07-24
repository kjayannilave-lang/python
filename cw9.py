from abc import ABC, abstractmethod

# Abstract class
class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    # Method to calculate years on the platform
    def years_on_platform(self):
        return 2025 - self.joining_year

    # Abstract method
    @abstractmethod
    def role(self):
        pass

    # Common display method
    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role()}")
        print(f"Years on Platform: {self.years_on_platform()} years")
        print()


# Customer class
class Customer(User):
    def role(self):
        return "Customer"


# Vendor class
class Vendor(User):
    def role(self):
        return "Vendor"


# Creating objects
customer1 = Customer("Alice", 2020)
vendor1 = Vendor("Bob", 2018)

# Display details
customer1.display()
vendor1.display()