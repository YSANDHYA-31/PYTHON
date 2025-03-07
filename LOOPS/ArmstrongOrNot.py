# Armstrong Or Not

Num=int(input("Enter the Number:"))

sum=0
temp=Num
while temp>0:
    rem=temp%10
    sum+=rem*rem*rem
    temp=temp//10

if sum==Num:
    print(f"{Num} is an Armstrong Number.")
else:
    print(f"{Num} is not an Armstrong Number.")
