class Car:
    def __init__(self,make,model):
        self.__make = make          #private attribute
        self.__model = model        #private attribute    
        self.__speed = 0            #private attribute

    def get_make(self,):
        return self.__make

    def set_make(self,make):
         self.__make = make


    def get_model(self):
       return self.__model

    def set_model(self,model):
        self.__model = model

car = Car(make="toyota",model="camry")

print(f"make:{car.get_make()}")
car.set_make = ("Honda")
print(f"Updated make:{car.get_make()}")


print(f"model:{car.get_model()}")
car.set_model = ("Endevour")
print(f"updated model:{car.get_model()}")
