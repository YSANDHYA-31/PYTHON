# another class in different package

from person import Person  # Importing Person from a different package

class ExternalClass:
    def access_public(self):
        obj = Person("Charlie", 35)
        print(f"Accessing public field: {obj.name}")  # Allowed
        obj.display_info()  # Allowed

# Running the access from a different package
if __name__ == "__main__":
    external = ExternalClass()
    external.access_public()
