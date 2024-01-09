"""
import string

s = input("Enter a string: ")

x=set(s.lower())
y=x.remove(" ")

print(x==set(string.ascii_lowercase))
"""
"""
s="Hello"
x=input("Enter a char that you want to replace")
new_char=input("Enter a new char that you want to replace with ")

curr_char=x.lower()

print(s.replace(curr_char,new_char))
"""
"""
s = input("enter a string")
if (s.isdigit()):
    print("true")
else:
    print("false")    
    """
"""
str = input("Enter a string: ")
print(str.replace(",","."))
"""
"""

str = input("enter a string")
for char in str.replace(" ",""):
    print(char, end="")
"""
#----------------------------------------------------------------------------------------------------------------------------------
x = lambda a: print(a)
x(5)

#----------------------------------------------------------------------------------------------------------------------------------
x= lambda a,b : print(a+b)
x(5,3)

#----------------------------------------------------------------------------------------------------------------------------------

x = lambda a,b : a+b
print(x(5,3))

#---------------------------------------------------------------------------------------------------------------------------------

x = lambda a,b : a+b

z=x(5,3)
print(z)

#---------------------------------------------------------------------------------------------------------------------------------

x = lambda a,b : (a+b,a*b,a-b)

print(x(5,3))

#---------------------------------------------------------------------------------------------------------------------------------

x= lambda a,b : (a+b,a-b,a*b)

result1,result2,result3= x(5,3)
print(result1)
print(result2)
print(result3)

#--------------------------------------------------------------------------------------------------------------------------------

x = lambda a,b=20 : (a+b)

print(x(5))


#-----------------------------------------------------------------------------------------------------------------------------------
# nested lambda

x = lambda a:(lambda b: a+b)
p=x(5)
q =p(4)
print(q)

#-----------------------------------------------------------------------------------------------------------------------------------
print()
x = lambda a:(lambda b:(lambda c: (a+b+c,a*b*c)))

p=x(5)
q=p(4)
r=q(2)

print(r)


#-------------------------------------------------------------------------------------------------------------------------------------


multi = lambda a:a*10
add = lambda b: b+10

def cal (func,val):
    return func(val)

result = cal(multi,5)
result3= cal(add,2)

print(result)
print(result3)

#-------------------------------------------------------------------------------------------------------------------------------------

def add (num):
    print("this is add function")
    def wrap():
        a=10
        return a+num()       
    return wrap


def mul (num):
    print("this is mul  function")
    def wrap():
        b=2
        return b*num()
    return wrap  
def num():
    return 20


result = add(num)
print(result())


#-------------------------------------------------------------------------------------------------------------------------------------

# pattern using nested for loop



for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()    


for i in range(1,6,):
    for j in range(i):     
        print(i,end="")
    print()



#--------------------------------------------------------------------------------------------------------------------------------------
#decorator

def add (a):
    print("this is add function")
    def wrap(fun):
        a = 20
        return a+b
        return fun()
    return wrap

def mul ():
    print("this is mul function ")
    def wrap(fun):
        a = 10
        return a*b
        return fun()
    return mul        

def fun ():
    b = 10
    return fun


result = fun(add())
print(result)
