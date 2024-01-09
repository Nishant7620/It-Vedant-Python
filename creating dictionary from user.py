di = {}

length = int(input("enter length of dictionary: "))

for i in range(length):
    key = input("enter a key: ")
    value = input("enter a value: ")
    di.update({key:value})

print(di)
