# parent class with public members

class Person:
    def __init__(self, name, age):
        self.name = name  # Public Field
        self.age = age  # Public Field

    def display_info(self):  # Public Method
        print(f"Name: {self.name}, Age: {self.age}")

# Accessing Public Members in the Same Package
class SamePackageClass:
    def access_public(self):
        obj = Person("Alice", 30)
        print(f"Accessing public field: {obj.name}")  # Allowed
        obj.display_info()  # Allowed

# Running the access from the same package
if __name__ == "__main__":
    other = SamePackageClass()
    other.access_public()
