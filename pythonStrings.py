"""-----------------------------------------------Strings in python---------------------------------------------------------"""

#Unicode string
"""
str=u"मराठी"
print(str)

"""
# for giving '
"""
str="How\'s the Josh!"
print(str)

str1="\"My name is Nishant\",I live in Panvel"
print(str1)

str2="\"my name is nishant \"i live in Panvel\"\""
print(str2)
"""
#for moving next line \n
"""
str="My name is Nishant \n I live in Panvel"
print(str)
"""
# gap between or gap of 4 space 
"""
str="My name is Nishant \t I live in Panvel"
print(str)
"""
#Row string (R) (r)
"""
str=R"How\"s the Josh!"
print(str)
"""
"""----------------------------------------------string formatting-----------------------------------------------------------"""
"""
str="hello"
print("{:<20}".format(str))

str1="Hello"
print("{:>20}".format(str1))

str3="Hello"
print("{:^20}".format(str3))

print("Hello",format('-','-<10'),"world")



str4="Nishant"
print("{:>10}".format(str4))

"""

"""-----------------------------------------Basic operation of string----------------------------------------------------"""
"""
#Concatination
a="Hello"
b="World"
print(a+b)

str1="Nishant "
str2="Karanjavkar"
print(str1+str2)
"""
"""
#Append

str1="Hello"
str2="world"
str1+=str2
print(str1)
"""
#f string
"""
str1="Hello"
str2="World"
str3=f"{str1}{str2}"
print(str3)


a="Nishant "
b="Karanjavkar"
c=f"{a}{b}"
print(c)
"""
#Looping through string
"""
for i in "Hello":
    print(i)

for x in "World":
    print(x)
"""
# len() in string
"""
str="Hello"
print(len(str))    
"""
# string check
"""
str="Always work hard"
print("work" in str)
"""
"""
str1="Hello"
print("el" in str1)
"""

# srting check using if statement
"""
str="Always do hard work"
if("hard" in str):
    print("hard is present")
else:
    print("entered string is not present")   
    """

#not in
"""
str ="always do hard work"
if("hello" not in str):
    print("hello is not present")
else:
    print("hello is present")         
"""
