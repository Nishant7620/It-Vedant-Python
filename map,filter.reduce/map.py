#squaring a number using normal function

numbers = [1,2,3,4,5]

def square(n):
    for  i in n:
        print(i**2)

square(numbers)

#-------------------------------------------------------------------------
#squaring a number using map() function

numbers  = [1,2,3,4,5]

def square(x):
    return x**2

squared =map(square,numbers)
result = list(squared)
print(result)

#------------------------------------------------------------------------
#squaring a number using lambda function in map() function
"""
numbers = [1,2,3,4,5]
doubled_numbers = map(lambda x:x*2,numbers)
list =list(doubled_numbers)
print(list)
"""
#--------------------------------------------------------------------------
#square a number using lambda function in map() function with two argument

number1 = [1,2,3,4,5]
number2 = [10,20,30,40,50]

two_argument = map(lambda x,y:x*y,number1,number2)

result = list(two_argument)
print(result)