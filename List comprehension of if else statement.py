my_list = [1,2,3,4,5,6,7,8]

for i in my_list :
    if i%2==0:
        print(i)


#-------------------------------------------------------------------------------------------------------
#list comprehension 

list = [1,2,3,4,5,6,7,8]

even_numbers = [i for i in list if i%2==0 ]
print(even_numbers)

#-----------------------------------------------------------------------------------------------------


even = [x for x in range(11) if x%2==0]
print(even)

#------------------------------------------------------------------------------------------------
#square of number using for loop

for i in range(10):
    if i%2==0:
        print(i**2)

square = [i**2 for i in range(10) if i%2==0]
print(square)


#---------------------------------------------------------------------------------------------------