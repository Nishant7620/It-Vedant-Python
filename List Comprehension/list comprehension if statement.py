#even numbers using for loop

for i in range(11):
    if i%2==0:
        print(i)


#------------------------------------------------------------------
#even numbers using list comprehension

even_numbers = [i for i in range(10) if i%2==0]
print(even_numbers)

#-----------------------------------------------------------------
#square of a number using loop

for x in range(10):
    if x%2==0:
        print(x**2)

#--------------------------------------------------------------------
# square of a number using list comprehension

square = [x**2 for x in range(10) if x%2==0]
print(square)        