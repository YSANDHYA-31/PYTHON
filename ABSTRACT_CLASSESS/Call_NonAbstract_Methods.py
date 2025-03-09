# call non-abstract methods from child class

from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    # Abstract Method (Must be implemented in subclass)
    @abstractmethod
    def area(self):
        pass  

    # Non-Abstract Method
    def display_shape(self):
        print("This is a shape.")

# Concrete Subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementing the abstract method
    def area(self):
        return self.length * self.width

    # Creating an instance inside the child class and calling non-abstract method
    @classmethod
    def test_non_abstract_methods(cls):
        rect = cls(10, 5)  # Creating an instance of Rectangle inside the class
        rect.display_shape()  # Calling the non-abstract method from the abstract class

# Calling the test method inside the subclass
Rectangle.test_non_abstract_methods()
