from functools import reduce
numbers = [1,2,3,4,5]

addition_ofnumbers = reduce(lambda x,y:x+y,numbers)

print("sum",addition_ofnumbers)

#--------------------------------------------------------------------------------
#largest number

numbers = [1,3,4,5,6,7,8,9,10]

largest_num = reduce(lambda x,y: x if x>y else y,numbers)
print(largest_num) 


#-------------------------------------------------------------------------------------
#factorial of a number

n = 5

fact = reduce(lambda x,y:x*y,range(1,n+1))
print(fact)