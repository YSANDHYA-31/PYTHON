# abstract and non-abstract methods

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    # Abstract Method (Must be implemented in subclass)
    @abstractmethod
    def sound(self):
        pass  # No implementation here

    # Non-Abstract Method (Common functionality)
    def sleep(self):
        print("Sleeping...")

# Concrete Subclass
class Dog(Animal):
    # Implementing the abstract method
    def sound(self):
        print("Dog barks: Woof! Woof!")

# Concrete Subclass
class Cat(Animal):
    # Implementing the abstract method
    def sound(self):
        print("Cat meows: Meow! Meow!")

# Creating objects
dog = Dog()
cat = Cat()

# Calling abstract method (Implemented in subclass)
dog.sound()  # Output: Dog barks: Woof! Woof!
cat.sound()  # Output: Cat meows: Meow! Meow!

# Calling non-abstract method (Inherited from parent)
dog.sleep()  # Output: Sleeping...
cat.sleep()  # Output: Sleeping...
