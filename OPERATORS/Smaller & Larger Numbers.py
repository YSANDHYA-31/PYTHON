# Smaller and Larger Numbers

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

if a < b:
    print(f"{a} is smaller and {b} is larger.")
elif a > b:
    print(f"{a} is larger and {b} is smaller.")
else:
    print(f"Both values are equal: {a} and {b}.")
