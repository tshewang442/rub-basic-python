# Base class
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        """Display employee details."""
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")

# Subclass 1: Manager
class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)  # Call the parent class constructor
        self.team_size = team_size

    def display_info(self):
        """Override the method to include team size."""
        super().display_info()
        print(f"Team Size: {self.team_size}")

# Subclass 2: Developer
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        """Override the method to include programming language."""
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

# Creating instances
emp1 = Manager("Alice", 101, 75000, 10)
emp2 = Developer("Bob", 102, 65000, "Python")

# Displaying details
print("Manager Details:")
emp1.display_info()

print("\nDeveloper Details:")
emp2.display_info()
