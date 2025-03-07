# Average element of an array

def average(arr):
    if len(arr)==0:
        return 0
    return sum(arr) // len(arr)

Num=list(map(int,input("Enter the elements of array:").split()))
print("Average of Array:",average(Num))