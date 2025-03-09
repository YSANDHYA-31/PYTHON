# child class in different package

from person import Person  # Importing Person from another package

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  # Calling Parent Constructor

    def access_public_in_subclass(self):
        print(f"Accessing public field in subclass: {self.name}")  # Allowed
        self.display_info()  # Allowed

# Running the access from the subclass
if __name__ == "__main__":
    child_obj = Child("Bob", 25)
    child_obj.access_public_in_subclass()
