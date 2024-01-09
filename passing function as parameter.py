
def display(ah):
    return "This is display function",ah()

def desp():
    return "this desp function" 
print(display(desp))    


#----------------------------------------------------------------------------------------------------------------------------------------

def add(a,b):
    return a+b

def sub (a,b):
    return a-b

def calculation(function,x,y):
    return function(x,y)

result1 = calculation(add,5,3)
print(result1)

result2 = calculation(sub,5,3)
print(result2)


