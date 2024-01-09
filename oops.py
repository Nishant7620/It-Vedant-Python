class Car:
    def __init__(self,maker,model,year):
        self.maker = maker
        self.model = model
        self.year = year
        print(self.maker)
        print(self.model)
        print(self.year)
    def start(self,s,st):
        self.s = s
        self.st = st 
        print(s)
        print(st)   
ford = Car(maker="ford",model="lxi",year="2020")

ford.start(s="on",st="off")

Ferrari = Car(maker="ferrari",model="vxi",year="2021")

Ferrari.start(s="on",st="off")







