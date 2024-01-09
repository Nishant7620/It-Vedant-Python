even_list = []
odd_list = []

for i in range(10):
    integer = int(input("enter a number:  "))

    if integer%2==0:
        even_list.append(integer)
    else:
        odd_list.append(integer)

print(even_list)
print(odd_list)        