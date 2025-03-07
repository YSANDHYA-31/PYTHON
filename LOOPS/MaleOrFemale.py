# M/F using dictionary(Switch-case style)

gender=input("Enter gender (M/F):").strip().upper()

switch={
    "M" :"Male",
    "F":"Female"
}

print(switch.get(gender,"Invalid input! Please enter M or F."))

