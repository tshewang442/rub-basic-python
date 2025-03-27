class Example:
    class_variable = 0  # Class state
    
    @classmethod
    def modify_class_state(cls, value):
        cls.class_variable = value  # Modifies the class state
    
    @staticmethod
    def static_method():
        print("Static method called. Can't access or modify class state.")

# Using class method to modify class state
Example.modify_class_state(10)
print(Example.class_variable)  # Output: 10

# Using static method
Example.static_method()
