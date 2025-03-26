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
