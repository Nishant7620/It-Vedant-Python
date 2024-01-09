num =int(input("Enter a number"))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("It is not a prime number")
            break
        else:
            print("it is a prime number")   
            break
else:
    print("It is not a prime number")             


print("----------------------------------------------------------------")

num = int(input("Please enter a number: "))


for i in range(2, num):
   if num % i == 0:
       print(num, "is not a prime number")
       break
else:
   print(num, "is a prime number")
