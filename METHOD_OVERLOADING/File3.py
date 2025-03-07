# two methods with same name and same no.of parameters of same type

class Example:
    def display(self, X):
        print(f"Method 1: {X}")

    def display(self, X): 
        print(f"Method 2: {X}")

obj = Example()
obj.display(10) 