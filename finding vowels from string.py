s = input("enter a string")
x=s.lower()
y=0
for i in x:
    if i in "aeiou":
        y+=1
print(y)