# Throwing an exception with custom message

def check_number(N):
    if N < 0:
        raise ValueError("Invalid Input: Number cannot be negative!") 
    else:
        print("Valid number:", N)

N = int(input("Enter a number: "))
check_number(N)
