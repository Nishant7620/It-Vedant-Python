from functools import reduce

numbers = [1,2,3,4,5,6]

add = reduce(lambda x,y:x+y,numbers)

print(add)
#---------------------------------------------------------------------------------------------------------------------
#larger number

number = [1,2,3,4,5,6]

max_value = reduce(lambda x,y: x if x>y else y,number)

print(max_value)

#---------------------------------------------------------------------------------------------------------------------
#factorial of a number

n=5

fact = reduce(lambda x,y:x*y,range(1,n+1))


print(fact  )