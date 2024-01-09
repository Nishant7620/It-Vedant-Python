class Car:
    speed = 0
    def __init__(self,make,model,year):
        self.make= make
        self.model = model
        self.year = year
        print(f"before acceleration {self.speed} mph")
    @classmethod
    def accelerate(cls,speed_increase):
        cls.speed = cls.speed + speed_increase
        print(f" Speed of car is {cls.speed} mph")

    def display(self):
        print(f"{self.make} {self.model} {self.year}")    
        

mustang = Car("ford","top",2020)

mustang.accelerate(40)

mustang.display()

