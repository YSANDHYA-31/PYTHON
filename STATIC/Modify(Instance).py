# Modify Static Variable within an Instance

class MyClass:
    static_var = 50 

obj1 = MyClass()
obj2 = MyClass()

print(obj1.static_var)  
print(obj2.static_var)  

obj1.static_var = 200  

print(obj1.static_var)  
print(obj2.static_var) 
print(MyClass.static_var)  
