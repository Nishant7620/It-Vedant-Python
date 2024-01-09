import string
s = input("Enter a string: ")

x =set(s.lower())
y=x.remove(" ")



print(x==set(string.ascii_lowercase))

print(string.ascii_lowercase)

print(set(string.ascii_lowercase))
