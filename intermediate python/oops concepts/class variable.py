class Cirlce:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def calculate (self):
        return self.pi * self.radius * self.radius

Cirlce.pi = 30

c1 =Cirlce(5)
print(c1.calculate())

c2= Cirlce(10)
c2.pi =30

print(c2.calculate())

c3 = Cirlce(5)
c3.pi =10
print(c3.calculate())


#-------------------------------------------------------------------------------------------------------

class Cirlce:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def calculate(self):
         print(self.pi * self.radius * self.radius)

print("before ")
c1 = Cirlce(5)
result = c1.calculate()  

print("after")
c1.pi = 10
result = c1.calculate() 

c2 =Cirlce(6)

c2.pi = 100

result = c2.calculate()








