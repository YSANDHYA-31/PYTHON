# Largest among three

A,B,C=map(int,input("Enter numbers A, B, C:").split())
if A>B and A>C:
    print(f"{A} is Largest among three.")
elif B>A and B>C:
    print(f"{B} is Largest among three.")
else:
    print(f"{C} is Largest among three.")