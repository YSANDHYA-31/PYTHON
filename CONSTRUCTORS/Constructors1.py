# call all the constraints of the class

class ConstructorDemo:
    def __init__(self, num1=0, num2=None):
        if num2 is None and num1 == 0:
            print("Default Constructor Called")
        elif num2 is None:
            self.num1 = num1
            print(f"One-Argument Constructor Called: num1 = {self.num1}")
        else:
            self.num1 = num1
            self.num2 = num2
            print(f"Two-Argument Constructor Called: num1 = {self.num1}, num2 = {self.num2}")

# Main function to test constructors
if __name__ == "__main__":
    # Calling Default Constructor
    obj1 = ConstructorDemo()

    # Calling One-Argument Constructor
    obj2 = ConstructorDemo(10)

    # Calling Two-Argument Constructor
    obj3 = ConstructorDemo(20, 30)
