# Copy the elements from one to another array

def copy(arr):
    return arr[:]

Num1=list(map(int,input("Enter elements of Num1:").split()))
Num2=copy(Num1)

print("Copied Elements of Num2:",Num2)