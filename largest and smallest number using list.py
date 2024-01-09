list = [1,2,3,4,5,6,7,8]

if len(list)<=0:
    print("empty list")

else:
    x = max(list)
    y = min(list)

    print(x,"is largest element,",y,"is smallest element",sep=" ")
