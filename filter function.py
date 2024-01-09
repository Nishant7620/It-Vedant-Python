numbers = [1,2,3,4,5,6]

def even (n):
        return n%2==0

even_numbers = list(filter(even,numbers)) 

print(even_numbers)

#---------------------------------------------------------------------------------------------
#applying filter () in lambda function()

number = [1,2,3,4,5,6]

x = filter(lambda a: a%2==0,number)

result =list(x)
print(result)

#------------------------------------------------------------------------------------------
# checking string empty or not

string = ["","hello","","World"]

check_string = filter(lambda x: len(x)>0,string)

result = list(check_string)
print(result)

#-------------------------------------------------------------------------------------------
#using null in filter

#num = [1,2,3,4,5,6,7,8,10]
num = [True,False,True,False]

even_num = list(filter(None,num))

print(even_num)
