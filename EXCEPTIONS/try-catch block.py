# try-catch block

try:
    Num1 = 5
    Num2 = 0
    result = Num1 / Num2 
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
