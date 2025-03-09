# Access modifiers

class SuperClass:
    # Public Constructor
    def __init__(self):
        print("SuperClass: Public Constructor Called")

    # Protected Constructor
    def _init_protected(self):
        print("SuperClass: Protected Constructor Called")

    # Private Constructor (Name-Mangling)
    def __init_private(self):
        print("SuperClass: Private Constructor Called")

class SubClass(SuperClass):
    def __init__(self):
        super().__init__()  # Calls the Public Constructor
        print("SubClass: Public Constructor Called")

        # Calling the protected constructor
        super()._init_protected()

        # Trying to call the private constructor (Will cause an AttributeError if accessed directly)
        try:
            super().__init_private()
        except AttributeError:
            print("Cannot directly access SuperClass private constructor")

# Main function to test constructors
if __name__ == "__main__":
    obj = SubClass()
    
    # Accessing protected constructor from an object (Not recommended)
    obj._init_protected()  

    # Attempt to access the private constructor (Will cause an error)
    try:
        obj.__init_private()
    except AttributeError:
        print("Cannot access private constructor from outside the class")
