
x = lambda a:(lambda b:a+b)
y=x(5)
z=y(10)
print(z)

#---------------------------------------------------------------------------------------------------------------------------------------

a = lambda x:(lambda y:x*y)
b=a(5)(2)
print(b)

#---------------------------------------------------------------------------------------------------------------------------------------

sum_all = lambda a:(lambda b:(a+b,a-b,a*b))
x=sum_all(5)
p,q,r=x(3)
print(p)
print(q)
print(r)

#---------------------------------------------------------------------------------------------------------------------------------------

increment = lambda x:x + 10
square = lambda y: y*y

def apply_function(fun,number):
    return fun(number)

result1=apply_function(increment,5)
result2=apply_function(square,3)    

print(result1)
print(result2)

#--------------------------------------------------------------------------------------------------------------------------------------

def lamb (x):
    print (f"result is{x(5)} ")
z=(lamb(lambda y:y*y))
print(z)




