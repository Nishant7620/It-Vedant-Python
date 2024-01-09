class Parent:
    def __init__(self):
        print("parent property")

    def car(self):
        print("this is car")    


class Child(Parent):
    def __init__(self):
        print("Child property")

    def child_car(self):
        print("this child car")    


c = Child()
c.car()
p = Parent()
#p.child_car()


#-----------------------------------------------------------------------------------------------------

class Vehicle:
    def car_info(self):
        print("Jaguar F-type 2020 edition")

    def rtr(self):
        print("Ready to Race")

class Car(Vehicle):

    def start_engine(self):
        print("Press start button to start the car")

    def honk(self):
        print("press honk button to honks loudly")

Van = Vehicle()

Van.car_info()

Van.rtr()

Jaguar = Car()

Jaguar.start_engine()

Jaguar.honk()
