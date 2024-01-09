class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def set_make(self,brand):
        self.make = brand

    def set_model(self,mod):
        self.model = mod 

mustang = Car("ford","top")

print(mustang.make)
print(mustang.model)

mustang.make ="Lamborghini"
mustang.model = "Avantador"

print(f"new company in the market is {mustang.make}")
print(f"Model lauch is {mustang.model}")


#---------------------------------------------------------------------------------------------

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def set_marks (self,update):
        self.marks = update

info = Student("Nishant",60)

print(info.name)
print(info.marks)

info.marks = 80

print(f"Student name is {info.name} and upated marks are {info.marks}")



