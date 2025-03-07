# Remove Duplicates

def remove_duplicates(Arr):
    unique=[]
    for num in Arr:
        if num not in unique:
            unique.append(num)
    return unique

Arr=list(map(int,input("Enter elements of Array:").split()))
print("Array after removing duplicates:",remove_duplicates(Arr))