def function ():
    return "This is function"
print(function())    

#---------------------------------------------------------------------------------------------------------------------------------------

def name ():
    str = "Nishant"
    return str
print(name())


#-------------------------------------------------------------------------------------------------------------------------------------

def add():
    x=20
    y=10
    return x+y  # result is store in add/ 30 is store in add()
print(add())    

#--------------------------------------------------------------------------------------------------------------------------------------

def sub():
    x=10
    y=5
    result = x - y
    return result
print(sub())    

#-------------------------------------------------------------------------------------------------------------------------------------

def mul ():
    x=2
    y=8
    result = x * y
    return result
print(mul())    


#-----------------------------------parameterised-------------------------------------------------------------------------------------

def add (x,y):
    result= x+y
    return result
print(add(5,10))

def name (str):
    return "My name is",str
a = name("Nishant")
print(a)

#--------------------------------------------------------------------------------------------------------------------------------------

def add_numbers (x,y):
    add = x+y
    sub = x-y
    return add,sub
x,y = add_numbers(5,10)
print(x,y)  