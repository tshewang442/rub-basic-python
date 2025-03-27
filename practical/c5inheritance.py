class Person():
  nationality = "Bhutanese"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def display(self):
    print(f"Person class; Name: {self.name} Age: {self.age}")

class Employee(Person):
  def __init__(self, name, age, emp_id, salary):
    Person.__init__(self, name, age)
    self.emp_id = emp_id
    self.salary = salary
    # Person.nationality = "BHT"

  def display(self):
    super().display()
    print(f"Employee class; Emp ID: {self.emp_id} Salary: {self.salary}")

class Manager(Employee):
  def __init__(self, name, age, emp_id, salary, dept):
    super().__init__(name, age, emp_id, salary)
    self.dept = dept

  def display(self):
    super().display()
    print(f"Manager class: Department: {self.dept.title()}")

obj = Manager("John", 30, "EMP08", "70000", "Product Service")
obj.display()

# print("**********************\n")
# name = str(input("Enter Full Name: "))
# age = int(input("Age: "))
# empid = input("Employee ID:")
# salary = float(input("Salary: "))
# dep = input("Department: ")

# print("\n*********** Display Info ***********\n")
# manager_Obj = Manager(name, age, empid, salary, dep)
# manager_Obj.display()
# print("\n")
