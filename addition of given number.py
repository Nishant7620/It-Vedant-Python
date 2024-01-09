num = int(input("enter a number"))

def addition (num):
        if num <=1:
            return 1
        else :
            x = num%10
            y = num//10
            z = y//10
            sum = x+y+z
            print(sum)
addition(num)            

            