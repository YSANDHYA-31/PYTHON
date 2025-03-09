# accessing private fields and methods


class Parent:
    def __init__(self, name, age):
        self.__name = name  # Private Field
        self.__age = age  # Private Field

    # Private Method
    def __display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    # Public Method to Access Private Method
    def access_private_method(self):
        self.__display_info()  # Calling private method inside the class

    # Public Method to Access Private Fields
    def get_private_fields(self):
        return f"Name: {self.__name}, Age: {self.__age}"

    # Main Method to Test Private Access
    @staticmethod
    def main():
        obj = Parent("Alice", 25)

        # Accessing Private Fields using Public Method
        print(obj.get_private_fields())

        # Calling Private Method using a Public Method
        obj.access_private_method()

# Calling the main method
Parent.main()

# Subclass Attempting to Access Private Fields & Methods
class Child(Parent):
    def access_private_from_child(self):
        try:
            print(self.__name)  # Trying to access private field (This will fail)
        except AttributeError:
            print("Cannot access private field directly in subclass")

        try:
            self.__display_info()  # Trying to access private method (This will fail)
        except AttributeError:
            print("Cannot access private method directly in subclass")

# Creating an instance of Child class
child_obj = Child("Bob", 20)
child_obj.access_private_from_child()
