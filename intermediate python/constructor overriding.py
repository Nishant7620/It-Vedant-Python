class Vehicle:
    def __init__(self):
        print("This is a Vehicle constructor")

    def ca_info(self):
        print("Jaguar f-type 2020 edition")

class Car(Vehicle):

    def __init__(self):
        super().__init__()
        print("this is a car constructor")

    def start_engine(self):
        print("Press start button to start the Car")

#v = Vehicle()
#v.ca_info()

c = Car()
c.start_engine()
