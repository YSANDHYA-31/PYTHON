# Method Overriding

# Superclass X
class X:
    def __init__(self):
        self.value = "Class X Variable"

    def method_X1(self):
        print("Method X1 from Class X")

    def method_X2(self):
        print("Method X2 from Class X")

    def show(self): 
        print("Show method in Class X")

# Subclass Y (Inheriting X)
class Y(X):
    def __init__(self):
        super().__init__()
        self.value = "Class Y Variable"

    def method_Y1(self):
        print("Method Y1 from Class Y")

    def method_Y2(self):
        print("Method Y2 from Class Y")

    def show(self):  
        print("Show method in Class Y")

# Subclass Z (Inheriting Y)
class Z(Y):
    def __init__(self):
        super().__init__()
        self.value = "Class Z Variable"

    def method_Z1(self):
        print("Method Z1 from Class Z")

    def method_Z2(self):
        print("Method Z2 from Class Z")

    def show(self):  
        print("Show method in Class Z")

# Main class
class Main:
    def main(self):
        # Creating objects
        obj_X = X()
        obj_Y = Y()
        obj_Z = Z()

        print("\n--- Methods from Class X ---")
        obj_X.method_X1()
        obj_X.method_X2()
        obj_X.show()

        print("\n--- Methods from Class Y ---")
        obj_Y.method_Y1()
        obj_Y.method_Y2()
        obj_Y.show()

        print("\n--- Methods from Class Z ---")
        obj_Z.method_Z1()
        obj_Z.method_Z2()
        obj_Z.show()

        print("\n--- Runtime Polymorphism ---")
        ref = X()  
        ref.show()

        ref = obj_Y 
        ref.show() 

        ref = obj_Z 
        ref.show()  

# Running the main class
if __name__ == "__main__":
    Main().main()
