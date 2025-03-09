# attributes of a constructor

class Student:
    def __init__(self, name, age, course):
        # Constructor Attributes
        self.name = name  # Public Attribute
        self.age = age    # Public Attribute
        self._course = course  # Protected Attribute (Convention: single underscore)
        self.__id = 1001  # Private Attribute (Convention: double underscore)

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self._course}")

    def get_id(self):
        return self.__id  # Accessing private attribute inside the class

# Creating an object and passing values to constructor attributes
student1 = Student("Alice", 20, "Computer Science")

# Accessing public attributes
print(f"Student Name: {student1.name}")
print(f"Student Age: {student1.age}")

# Accessing protected attribute (Allowed but not recommended)
print(f"Student Course: {student1._course}")

# Trying to access private attribute directly (This will raise an AttributeError)
try:
    print(f"Student ID: {student1.__id}")
except AttributeError:
    print("Cannot access private attribute directly")

# Accessing private attribute using a public method
print(f"Student ID (via method): {student1.get_id()}")

# Displaying all details using a method
student1.display_details()
