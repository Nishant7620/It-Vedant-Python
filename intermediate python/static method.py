class MathOperation:
    @staticmethod
    def add(x,y):
        return x+y


    @staticmethod
    def mul(x,y):
        return x*y

sum = MathOperation()
multi = MathOperation()
print(multi.mul(8,2))
print(sum.add(5,3))

print(f"sum of numbers: {MathOperation.add(5,3)}")
print(f"Multiplication of numbers: {MathOperation.mul(8,2)}")
