num_1 = int(input("Enter the first number"))
num_2 = int(input("Enter the second number"))
num_3 = int (input("Enter the third number"))
"""
x = lambda a,b,c:max(a,b,c)

result=x(num_1,num_2,num_3)

print(result)

"""
y = lambda a:(lambda b:(lambda c:(max(a,b,c))))

p = y(num_1)

q =p(num_2)

r =q(num_3)

print(r)