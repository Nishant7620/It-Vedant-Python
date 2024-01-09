class Car:
    def __init__(self,maker,model,year,color,is_alloted=True):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
        self.is_alloted = is_alloted
    
    def branch(self):
        if self.year ==2020: 
            print(f"The {self.maker} {self.model} {self.color} is from Mumbai branch")
        else:
            print(f"{self. model} belongs to another branch")

    def alloted(self):
        if self.is_alloted:
            print("Car is alloted")

    def display_info(self):
        print("Car Information\n"
            f"Maker: {self.maker}\n"
            f"Model: {self.model}\n"
            f"year: {self.year}\n"
            f"Color: {self.color}\n"
            f"alloted: {self.is_alloted}\n")

#creating intance of class car
toyota = Car(maker ="toyota",model ="supra",year="2021",color="green")
endivor = Car(maker ="ford",model ="endivor",year=2020,color="green")

# method to interact with class car
toyota.display_info()
toyota.branch()
toyota.alloted()

endivor.display_info()
endivor.branch()
endivor.alloted()

