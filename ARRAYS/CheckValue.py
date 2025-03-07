# Check value of an array

def value(arr,result):
    return result in arr

Num=list(map(int,input("Enter the elements of Array:").split()))
result=int(input("Enter the value to search:"))

if value(Num,result):
    print(f"{result} is present in the Array.")
else:
    print(f"{result} is not present in the Array.")      