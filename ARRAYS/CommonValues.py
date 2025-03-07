# To print common values in two arrays

Arr1=list(map(int,input("Enter elements of Arr1:").split()))
Arr2=list(map(int,input("Enter elements of Arr2:").split()))
common=list(set(Arr1) & set(Arr2))
if common:
    print("Common Values:",common)
else:
    print("No Common Values.")