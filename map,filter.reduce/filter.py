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

#-----------------------------------------------------------------
#checking string empty or not

string = ["hello" ,"","world"]

check_string = list(filter(lambda s: len(s)>0,string))
print(check_string)

#-----------------------------------------------------------------
#using null in filter

numbers =[1,2,3,4,4,5,6,7,8,9,10]
numbers = [True,False,True,False,True]

even_numbers = list(filter(None,numbers))
print(even_numbers)


