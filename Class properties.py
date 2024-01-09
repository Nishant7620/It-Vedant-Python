
class Car:
    def __init__(self,make,model,year,color,fuel_type,is_running=True,speed =0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color                          #instance Attribute of class
        self.fuel_type = fuel_type
        self.is_running = is_running
        self.speed = speed

    def start(self):                                #instace Method of class        
        if self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model} is starting")
        else:
            print("press Start button to start the car")
    def stop (self):
        if self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model} is stopping")
        else:
            print("the car is already stopped")
    def accelerate(self,speed_increase):
        if self.is_running:
            self.speed+=speed_increase 
            print(f"The car accelerating. Current speed: {self.speed} mph")
        else:
            print("Start the car before accelerating")
    def display_info(self):
        print(f"\nCar Information:\n"
                f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Year: {self.year}\n"
                f"Color: {self.color}\n"
                f"Fuel Type: {self.fuel_type}\n"
                f"Is Running: {self.is_running}\n"
                f"Current speed: {self.speed} mph \n")                                    
    


#creating instance of a class

Mustang = Car(make="ford",model="top",year="2020",color="green",fuel_type="petrol")

#using method to interact with the class(car)

Mustang.display_info()
Mustang.start()
Mustang.accelerate(30)
Mustang.stop()

#----------------------------------------------------------------------------------
