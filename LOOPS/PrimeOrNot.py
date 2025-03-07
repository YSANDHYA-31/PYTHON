# Prime Or Not

Num=int(input("Enter a Number:"))

if Num<2:
    print(f"{Num} is not a Prime Number.")
else:
    for i in range(2,int(Num**0.5)+1):
        if Num % i==0:
            print(f"{Num} is not a Prime Number.")
            break
        else:
            print(f"{Num} is a Prime Number.")
