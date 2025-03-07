# Remove element from array

def remove(arr,result):
    return [i for i in arr if i!=result]

Num=list(map(int,input("Enter array elements:").split()))
result=int(input("Enter the elements to remove:"))

print("Updated Array:",remove(Num,result))