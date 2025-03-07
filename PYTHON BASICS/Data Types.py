# Defining variables of Various Data Types

# Input is given by the user

Value=input("Enter a Value:")
try:
    # try evaluating the input to convert it into its correct type
    # eval() automatically detects and converts the entered string
    var=eval(Value)

except:
    # if eval() fails, treat it as a string
    var=Value
    
print(type(var).__name__)