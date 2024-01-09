s = input("Enter a string")
x=s.lower()
if (x[0::]==x[::-1]):
    print("true")
else:
    print("false")    