#Built-in Python Exceptions
""" 1 ZeroDivisionError """
def divi_error():
    x = 1/0

try:
    # divi_error()
    x = int("abc")
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
except ValueError as er:
    print("Wrong value Error:", er)


""" 2 ValueError """
# try:
#     x = int("abc")
# except ValueError as er:
#     print("Wrong value Error:", er)
    
    
""" 3 try else finally - Clean up actions """
# try:
#     num = int(input("Enter a number: "))  # User input
#     result = 10 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Invalid input! Please enter a number.")
# else:
#     print("Operation successful:", result)
# finally:
#     print("Execution finished.")  # Always executes


""" 4 Raising Exceptions """
# try:
#     raise NameError('Error Hi_There')
# except NameError as e:
#     print('An exception:', e)
#     # raise #to re-raise the error
    
    
""" 5 Catching Any Exception """
""" Catching all exceptions blindly can hide real bugs. Better Approach: Catch Specific Errors """
# try:
#     value = int("abc")  # Causes ValueError
#     result = 10 / value  # If value is 0, causes ZeroDivisionError
# except Exception as er:
#     print(f"Something went wrong: {er}")