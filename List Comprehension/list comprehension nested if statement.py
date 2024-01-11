#number is divisible by 3 and 7 using for loop

for i in range(100):
    if i%3==0:
        if i%7==0:
            print(i)

#--------------------------------------------------------------------
# number is divisible by 3 and 7 using list comprehension

result = [i for i in range(100) if i%3==0 if i%7==0]
print(result) 

#---------------------------------------------------------------------
#square of number using loop

for i in range(100):
    if i%3==0:
        if i%7==0:
            print(i**2)

#---------------------------------------------------------------------
#square of a number using list comprehension

square = [x**2 for x in range(100) if x%3==0 if x%7==0]
print(square)
