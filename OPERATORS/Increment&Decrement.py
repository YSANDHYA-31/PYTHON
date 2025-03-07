# Increment & Decrement of Numbers

inc = lambda x: x + 1  
dec = lambda x: x - 1  

N = int(input("Enter a number: "))  
operation = input("Enter operation (++, --): ")  

# Performing the operation based on user input
if operation == "++":
    print("Result:", inc(N))
elif operation == "--":
    print("Result:", dec(N))
else:
    print("Invalid Operation!")