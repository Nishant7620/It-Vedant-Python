di = {"a":1,"b":2,"c":3,"d":4}

k = input("enter a key")
v = input("enter a value")

if k not in  di:
    di[k] = v
    print(di)

else: 
    print("already exists")    


