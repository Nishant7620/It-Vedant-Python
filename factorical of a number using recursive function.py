num = int(input("enter a number"))

def factorial(n):
    fact = 1
    if n>=1:
        fact = fact * n
        n = factorial(n-1)
        return fact

    else:
        return 1

        
result=factorial(num)

print(result)