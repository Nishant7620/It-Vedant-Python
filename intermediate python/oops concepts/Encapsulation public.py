class Car:
    def __init__(self,make,model,year):
        self.make = make                                    #Instance Attribute
        self.model = model
        self.year = year

    def start(self):                                            #Instance method
        print(f"{self.make} {self.year} {self.model} is started")

car = Car("toyota","camry",2022)                                #class Instance

car.start()                                             #using instance method


print(car.model)                            #public Variable

