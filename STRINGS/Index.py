#Search using Index

txt=input("Enter the string:")
i=input("Enter the string to find:")
try:
    result=txt.index(i)
    print("Result:",result)
except ValueError:
    print("String not found.")