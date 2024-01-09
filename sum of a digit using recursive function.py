
def sum(num):
    while num<=10:
        return num
    else :
        return  num%10 + sum(num//10)


        
print(sum(143))        
        