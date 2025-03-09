# call constrructors of super class from child class

# Superclass with multiple constructors
class SuperClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("SuperClass: Default Constructor Called")
        elif b is None:
            print(f"SuperClass: One-Argument Constructor Called: a = {a}")
        else:
            print(f"SuperClass: Two-Argument Constructor Called: a = {a}, b = {b}")

# Subclass inheriting from SuperClass
class SubClass(SuperClass):
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            super().__init__()  # Calls SuperClass Default Constructor
            print("SubClass: Default Constructor Called")
        elif y is None:
            super().__init__(x)  # Calls SuperClass One-Argument Constructor
            print(f"SubClass: One-Argument Constructor Called: x = {x}")
        else:
            super().__init__(x, y)  # Calls SuperClass Two-Argument Constructor
            print(f"SubClass: Two-Argument Constructor Called: x = {x}, y = {y}")

# Main function to test constructors
if __name__ == "__main__":
    obj1 = SubClass()       # Calls default constructor
    obj2 = SubClass(10)     # Calls one-argument constructor
    obj3 = SubClass(20, 30) # Calls two-argument constructor

