class Addition:
    def Calculate(self,a,b):
        result = a+b
        print(f"Addition Result: {result}")

class Calculation(Addition):
    def Calculate(self,a,b):
        super().Calculate(5,3)
        result = a*b
        print(f"Multiplication Result: {result}")
calc = Addition()
calc.Calculate(10,20)



