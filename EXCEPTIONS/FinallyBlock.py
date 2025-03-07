# finally block

try:
    Num = int(input("Enter a number: "))
    print(10 / Num) 
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Execution completed.") 
