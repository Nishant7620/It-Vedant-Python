class Calculator:

    def add(self,a,b,c=None):
        if c is not None:
            return a+b+c
        else:    
            return a*b

cal = Calculator()

print(cal.add(5,3))

print(cal.add(5,3,2))