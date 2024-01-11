#square of a even number

square_of_even_number = [x**2 if x%2==0 else "odd" for x in range(10)]
print(square_of_even_number)

#number is divisible by 3 and 5

divisible = [f"{i} divisible by 3" if i%3==0 else f"{i} divisible by 5" if i%5==0 else i for i in range(50)]
print(divisible)