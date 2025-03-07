# Defining Local and Global variables with the same name

# Global Variable

X=50
def Function():
    X=55 # Local Variable with same name
    print("Local Variable inside a function:",X) # Prints Local varible i.e., 55    
Function()
print("Global Variable outside the fucntion:",X) # Prints Global Variable i.e., 50