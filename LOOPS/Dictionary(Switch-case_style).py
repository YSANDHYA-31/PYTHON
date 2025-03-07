# check even or odd using dictionary (switch-case style)

N=int(input("Enter the Number:"))

switch={
    0:"Even",
    1:"Odd"
}

print(f"{N} is {switch[N % 2]} number.")
