# two methods with same name but different no.of parameters os different datatypes

class Example:
    def display(self, *args):
        if len(args) == 1:
            print(f"One parameter of type {type(args[0]).__name__}: {args[0]}")
        elif len(args) == 2:
            print(f"Two parameters: {args[0]} ({type(args[0]).__name__}), {args[1]} ({type(args[1]).__name__})")
        else:
            print("Invalid number of arguments")

obj = Example()
obj.display(10)            
obj.display("Overloading")       
obj.display(10, "Overloading")  
obj.display(3.145, True)     
