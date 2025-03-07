# Sum of values of an array

def array(a):
    return sum(a)

# Input as seperated with spaces
Num=list(map(int,input("Enter the elements of Array:").split()))
print("Sum of Array:",array(Num))