
for i in range (10):
    if i%2==0:
        if i%3==0:
            print(i)
        
#-----------------------------------------------------------------------------------------
#list comprehension nested if statement

divisible = [i for i in range(10) if i%2==0 if i%3==0]

print(divisible)

#----------------------------------------------------------------------------------------
#squaring of number

square = [i**2 for i in range(10) if i%2==0 if i%3==0]

print(square)

#------------------------------------------------------------------------------------------
#square of even numbers 

square_of_even_numbers = [i**2 if i%2==0 else "odd" for i in range(1,10) ]

print(square_of_even_numbers)

#-----------------------------------------------------------------------------------------

div = [{f"{x} is divisile by 2" if x%2==0 else f"{x} is divisible by 3" if x%3==0 else "x" for x in range(10) }]

print(div)