numbers = [1,2,3,4,5]

def is_even(n):
    return n%2==0
    
even = filter(is_even,numbers)
list =list(even)

print(list)

#-----------------------------------------------------------------
