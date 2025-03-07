# Duplicates from the array

def duplicates(Arr):
    seen=set()
    dupli=set()
    for Num in Arr:
        if Num in seen:
            dupli.add(Num)
        else:
            seen.add(Num)
    return list(dupli)
Arr=list(map(int,input("Enter the Array Elements:").split()))
dupli=duplicates(Arr)
print("Duplicates Elements of Array:",dupli or "No Duplicates Found.")
