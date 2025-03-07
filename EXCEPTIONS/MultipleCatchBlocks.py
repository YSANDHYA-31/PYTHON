# multiple catch blocks

try:
    num1 = int(input("Enter numerator: ")) 
    num2 = int(input("Enter denominator: ")) 
    result = num1 / num2  
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except Exception as e: 
    print("An unexpected error occurred:", e)


