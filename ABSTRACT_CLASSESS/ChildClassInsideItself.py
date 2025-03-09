# Instance of a child class inside itself

from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    # Abstract Method (Must be implemented in subclass)
    @abstractmethod
    def area(self):
        pass  # No implementation in abstract class

    # Abstract Method
    @abstractmethod
    def perimeter(self):
        pass

# Concrete Subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementing the abstract methods
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    # Creating an instance inside the child class itself and calling abstract methods
    @classmethod
    def test_methods(cls):
        rect = cls(10, 5)  # Creating an instance of Rectangle
        print("Area:", rect.area())  # Calling implemented abstract method
        print("Perimeter:", rect.perimeter())  # Calling another implemented abstract method

# Calling the test method inside the subclass
Rectangle.test_methods()
