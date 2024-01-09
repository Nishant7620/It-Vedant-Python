def expo (num,exponent):
    if exponent ==0:
        return 1
    elif exponent ==1:
        return num    
    else:
        return num*expo(num,exponent-1)
 
print(expo(2,3))

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

print(power(2,3)) 
