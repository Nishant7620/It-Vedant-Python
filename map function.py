"""
numbers = [1,2,3,4,5,6]

def square (n):
    for i in n:
        print( i**2)

square(numbers)
"""
#------------------------------------------------------------------------------------------------------
# map ()
"""
def square (n):
    return n**2

numbers = [1,2,3,4,5,6]

squared = map(square,numbers)

print(list(squared))
"""
#--------------------------------------------------------------------------------------------------
#using lambda function in map ()
numbers = [1,2,3,4,5,6]
x = map(lambda a: a*2,numbers)

result = list(x)

print(result)

#------------------------------------------------------------------------------------------------
#squaring  a number using lambda function in map () with 2 argument

number1 = [1,2,3,4]
number2 = [7,8,9,10]

double_number = map(lambda a,b:a*b,number1,number2)

result = list(double_number)
print(result)

#------------------------------------------------------------------------------------------------
number1 = [1,2,3,4]
number2 = [7,8,9,10]

double_number = map(lambda a,b:(a*2,b*2),number1,number2)

result = list(double_number)
print(result)

#--------------------------------------------------------------------------------------------