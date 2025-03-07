# Palindrome Or Not

N=int(input("Enter the Number:"))
temp=N
rev=0

while N > 0:
    rem=N % 10
    N=N // 10
    rev=rev * 10 + rem

if temp==rev:
    print(f"{temp} is a Palindrome Number.")
else:
    print(f"{temp} is Not a Palindrome Number.")
