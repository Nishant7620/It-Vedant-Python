num = int(input("enter a number"))

def fibonacci (num):
    if num <=1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(num))         