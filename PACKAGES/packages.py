# Create two class

# create first class

class ClassA:
    def __init__(self):
        print("Constructor of ClassA is called.")

    def display(self):
        print("Method of ClassA is called.")

# create second class

class ClassB:
    def __init__(self):
        print("Constructor of ClassB is called.")

    def display(self):
        print("Method of ClassB is called.")

# Creating objects of both classes
obj1 = ClassA()  # Calls ClassA constructor
obj1.display()   # Calls ClassA method

obj2 = ClassB()  # Calls ClassB constructor
obj2.display()   # Calls ClassB method


