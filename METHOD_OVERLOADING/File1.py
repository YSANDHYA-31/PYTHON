# two methods with same name but different no.of parameters

class Example:
    def display(self, *args):
        print("Arguments:", args)

obj = Example()

obj.display(10)
obj.display(10, 20)
obj.display(10, 20, 30)
