
"""
string methods
"""
#uppercase
"""
str="Nishant"
print(str.upper())
"""
#lowercase
"""
str="Hello"
print(str.lower())
"""
#endswith() method
"""
str="we are learning string methods"
print(str.endswith("methods"))
"""
"""
str="we are learning string "
print(str.endswith("methods"))
"""
#string split() method
"""
str="we are learing string method"
print(str.split()) 
"""
"""
str1="Nishant"
print(str1.split())
"""
#string find() method
"""
str="we are learning string method"
tofind="learning"
print(str.find(tofind))
"""
"""
str1="always work hard"
print(str1.find("hard"))

print(str1.index("work"))
"""

#strip() method 
"""
str="    Always work hard   "
print(str.strip())


str1="Always work hard "
print(str1.lstrip())

str2="Always work hard"
print(str.rstrip())
"""
#count() method
"""
str="we are learning string methods"
print(str.count("string"))

str1=" My name is Nishant and full name is Nishant Ganesh Karanjavkar"
string="Nishant"
print(str1.count(string))
"""

#alphanumberic   ----isalnum() method
str="we are learning string methods"
print(str.isalnum())

str1="we are learning string methods 123"
print(str.isalnum())

# isdigit() method
string="12334343434344"
print(string.isdigit())

#isalnum() method

string2="afddsafdf12334"
print(string2.isalnum())

#repace() method

string3="We are learning string methods in python"
print(Replace("python","Python"))

