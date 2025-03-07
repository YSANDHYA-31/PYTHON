# Reverse the Elements of Array

def reverse_arr(Arr):
    Arr.reverse()
    return Arr

Arr=list(map(int,input("Enter the array elements:").split()))
print("Reversed Array:",reverse_arr(Arr))
