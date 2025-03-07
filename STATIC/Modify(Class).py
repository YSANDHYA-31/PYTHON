# Modify Static Variable within the Class

class MyClass:
    static_var = 50  

    @classmethod
    def change_static_var(cls, new_value):
        cls.static_var = new_value  

print(MyClass.static_var) 

MyClass.change_static_var(100)

print(MyClass.static_var)  
