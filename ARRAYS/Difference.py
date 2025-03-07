# Difference between Smallest and largest elements

def difference(Arr):
    return max(Arr)-min(Arr)

Arr=list(map(int,input("Enter Array elements:").split()))
print(f"The Difference between Smallest and Largest is:",difference(Arr))