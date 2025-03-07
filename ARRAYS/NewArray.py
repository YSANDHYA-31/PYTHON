# remove duplicates and print new array

def duplicates(Arr):
    return list(set(Arr))

Arr=list(map(int,input("Enter Elements of Array:").split()))
print("New Array:",duplicates(Arr))