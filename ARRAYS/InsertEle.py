# Insert elements at specific position

def insert_ele(Arr,New_element,Position):
    Arr.insert(Position,New_element)
    return Arr

Arr=list(map(int,input("Enter the elements of Array:").split()))
New_element=int(input("Enter the New Element:"))
Position=int(input("Enter the index position:"))
Updated_arr=insert_ele(Arr,New_element,Position)
print("Updated Array:",Updated_arr)