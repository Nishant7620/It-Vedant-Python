class Car:
    def __init__(self,make,model,year):
        self.speed = 0
        self.make = make
        self.model = model
        self.year = year

    def accelerate(self,speed_increase):
        self.speed = self.speed + speed_increase

    def display(self):
        print(f"the current speed of {self.make} {self.model} of {self.year} is {self.speed}") 

Endivor =Car(make ="ford",model="top",year="2021")
Endivor.display()
Endivor.accelerate(20)
Endivor.display()