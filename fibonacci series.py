num = int(input("enter a number"))

n1 =0
n2 =1
n3=0
print(n1,n2,end=" ")
for i in range(0,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")