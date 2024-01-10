class Vehicle:

    def __init__(self,color,wheels):
        self._color = color
        self._wheels = wheels

class Car(Vehicle):

    def __init__(self,color,wheels,doors):
        super().__init__(color,wheels)
        self._doors = doors  

    def car_details(self):
        print(f"color of car {self._color}, No. of {self._wheels}, No.of doors {self._doors}")          

car = Car("black",4,4)
car.car_details()

#Accessing protected variable using object
print(f"Before changing protected variable of wheel: {car._wheels}")
car._wheels = 10
print(f"After changing protected variable of wheel: {car._wheels}")

print(car._color)
