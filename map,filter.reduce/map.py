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