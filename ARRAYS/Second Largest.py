# Second Largest element from the array

def second(Arr):
    unique = list(set(Arr))
    return max(unique) if len(unique) < 2 else sorted(unique)[-2]  

Arr = list(map(int, input("Enter the Array elements: ").split()))
print("The Second Largest element of the Array:", second(Arr))
