"""
def prime ():  
    if (num<=1) :
        return False 
    for i in range (2,num) :
        if(num%i==0):
            return False
    return True  
num = int(input("enter a number")) 
if prime(num):
    print("is a prime number")   
else :
    print("not a prime number")                    
    


def is_prime(number):
    if number <= 1:
        return False  # 1 and any number less than 1 are not prime

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Number is divisible by some other number

    return True  # Number is prime

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is prime and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime num)")


  

num = int(input("Enter a number: "))   
def primenumber(num):
        
    if (num<=1):
        return False
    else :
        for i in range (2,num):
            if (num%i==0):
                return False
            else :
                return True

if primenumber(num):
    print("prime number")
else:
    print("Not a prime number")    
                   
                     """

num = int(input("Enter a number: "))   
def primenumber(num):
        
    if (num>1):
        for i in range (2,num):
            if (num%i==0):
                return False
            else :
                return True

if primenumber(num):
    print("prime number")
else:
    print("Not a prime number") 