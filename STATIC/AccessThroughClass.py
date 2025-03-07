# Static Variable and access through a Class

class MyClass:
    #Static Variable
    static = 50

print(MyClass.static) 

# Creating Instances
obj1 = MyClass()
obj2 = MyClass()

print(obj1.static)  
print(obj2.static)  

# Modifying Static Variable
MyClass.static = 100

print(obj1.static) 
print(obj2.static) 
