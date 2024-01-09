"""

#Arithmetic operators in python:

"""
"""
#  +
a=10
b=20

print(a+b)
"""
"""
# -

print(40-20)
"""

# *
"""
x=20
y=40

print(x*y)
"""
"""
# /

x=20
y=60

print(y/x)
"""
"""
# %
num1=40
num2=50
print(num2%num1)

"""
"""
# //
x=40
y=50
print(y//x)
"""
"""
# **
x=4**2
print(x)
"""

""" Assignment operaters in python """
"""
# =

a=20
print(a)
"""
"""

# += 
x=1
x+=5
print(x)

"""
"""

# -=

x=10
x-=5
print(x)
"""

"""

# *=
x=20
x*=5

print(x)
"""
"""

# /=
x=5
x/=10
print(x)

"""
"""
# %=

x=2
x%=20
print(x)
"""

"""
# //=
x=5

x//=5
print(x)
"""
"""
**=
x=2
x**=5
print(x)

"""

"""    Comparision operators    """
""" 
#==

x=20
y=20

print(x==y)
""" 

"""
#!==

x=40
y=40

print(x!=y)

"""

"""  Identity Operators  """
"""
x=5
y=5

print(x is y)
"""
"""
x=5
y=5

print(x is not y)

"""

""" membership operator """
"""
x="Hello"

print("el" in x)

"""
"""
x="Hello"

print("h" in x)         # python is case sensitve 

"""
"""
city=["Panvel","Kharghar","Belapur"]

print("Panvel" in city)

"""

"""
city=["Panvel","Kharghar","Belapur"]
print("Panvel" not in city)

"""

""" Bitwise operator """
"""
# &
x=7
y=5
store=(x&y)
print("store",bin(store))
"""
"""
# |

x=7
y=5
z=(x|y)
print("z=",bin(z))

"""
"""

# ^

x= 5
y= 7

z=(x^y)
print("z",bin(z))


"""
"""
#example

x=7
y=8
store=x+y
print("store",bin(store))
"""

"""
"""

"""------------------------------------------Conditinal statements or branching statements--------------------------------------"""

#if statement
"""
age=int(input("Enter your age:"))
if(age>18):
    print("you are eligible")
"""

#if else statement
"""
age=int(input("Enter your age"))
if(age>18):
    print("you are eligible to drive")
else:
    print("you are not eligible to drive")

"""
"""
#Nested if statement
age=int(input("Enter your age"))
marks=int(input("enter your marks"))
if(age>=18):
    if(marks>=60 and marks<=100):
        print("you are eligible for admission")
    else:
        print("please try next time ")    
else:
    print("please try next time ")
    
"""

