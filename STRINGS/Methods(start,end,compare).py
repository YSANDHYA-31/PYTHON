# startswith() , endswith() , compareTo()

txt1=input("Enter the string:")
start=input("Enter the starting string:")
end=input("Enter the ending string:")

print(txt1.startswith(start))
print(txt1.endswith(end))

txt2=input("Enter the second string to compare:")
print(f"txt1 and txt2 are equal:",txt1 == txt2)
print(f"txt1 and txt2 are not equal:",txt1 != txt2)
print(f"txt1 is less than txt2:",txt1 < txt2)
print(f"txt1 ais greater than txt2:",txt1 > txt2)
