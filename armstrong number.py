num  = int(input("enter a number"))
n = len(str(num))
sum = 0
temp = num
while temp>0:
    digit = temp %10
    sum += digit **int(n)                        #floor =digit//10
    temp = temp//10
        
if num == sum :
    print("true")

else :
    print("false")




