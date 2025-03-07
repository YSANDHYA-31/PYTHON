# Even and Odd in Array

def even_odd(Arr):
    Even=sum(1 for Num in Arr if Num%2==0)
    Odd=len(Arr)-Even
    return Even,Odd

Arr=list(map(int,input("Enter the array elements:").split()))
X,Y=even_odd(Arr)
print(f"Even Numbers:{X}\nOdd Numbers:{Y}")
