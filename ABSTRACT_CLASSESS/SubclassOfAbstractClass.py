# subclass of an abstract class

from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    # Abstract Method (Must be implemented in subclass)
    @abstractmethod
    def area(self):
        pass  # No implementation

    # Non-Abstract Method
    def display(self):
        print("This is a shape.")

# Subclass Implementing the Abstract Method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementing the abstract method
    def area(self):
        return 3.14 * self.radius * self.radius

# Creating an object of the subclass
circle = Circle(5)

# Calling the non-abstract method using the subclass object
circle.display()  # Output: This is a shape.

# Calling the implemented abstract method
print("Area of Circle:", circle.area())  # Output: Area of Circle: 78.5
