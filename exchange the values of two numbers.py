
#by using temporary variable
x=100
y=200
temp=0
temp=x
x=y
y=temp

print(x)
print(y)

# without using temporary variable

a=100
b=200
a=a+b #300
b=a-b #100
a=a-b #200  
print(a)
print(b)


str=input("Enter your name:")
print(str)