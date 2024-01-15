"""
numbers = [1,2,3,4,5]

def is_even(n):
    return n%2==0
    
even = filter(is_even,numbers)
list =list(even)

print(list)
"""
#-----------------------------------------------------------------
#applying filter () in lambda function

numbers = [1,2,3,4,5,6,7,8]

even_number = filter(lambda x:x%2==0,numbers)

even_list = list(even_number)
print(even_list)