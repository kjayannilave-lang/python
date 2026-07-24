from abc import ABC, abstractmethod

# Abstract class
class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    # Concrete method
    def account_age(self):
        return 2025 - self.account_year

    # Abstract method
    @abstractmethod
    def get_role(self):
        pass


# Admin class
class Admin(User):
    def get_role(self):
        return "Admin"

    # Magic method
    def __str__(self):
        return f"{self.name} is an Admin user."


# Guest class
class Guest(User):
    def get_role(self):
        return "Guest"

    # Magic method
    def __str__(self):
        return f"{self.name} is a Guest user."


# Creating objects
admin = Admin("Alice", 2020)
guest = Guest("Bob", 2023)

# Display details
print("Admin Details")
print("Role:", admin.get_role())
print("Account Age:", admin.account_age(), "years")
print(admin)

print()

print("Guest Details")
print("Role:", guest.get_role())
print("Account Age:", guest.account_age(), "years")
print(guest)