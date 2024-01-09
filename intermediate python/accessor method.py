class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model


Mustang =Car("ford",2022)

print(f"The Maker of Mustang Car is {Mustang.get_make()}")

print(f"The Manufacture year of Mustang is {Mustang.get_model()}")


#-------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self,name,address,field):
        self.name = name
        self.address = address
        self.field = field

    def get_name(self):
        return  self.name 

    def get_address(self):
        return self.address 

    def get_field(self):
        return self.field

info = Student("Nishant","Navi-Mumbai","IT")

print(info.get_name())
print(info.get_address())
print(info.get_field())

print(f"Name of student is {info.get_name()} Current address of student is {info.get_address()} and field of student is {info.get_field()}")


