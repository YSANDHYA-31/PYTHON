# check whether the array contain elements -- 12 and 23

def elements(Arr):
    return (12 in Arr) and (23 in Arr)  

Arr = list(map(int, input("Enter Array elements: ").split()))
print("Whether the Array contain elements 12 and 23:",elements(Arr))
