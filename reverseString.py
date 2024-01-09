""".Write a Python Program that prints the reversed version of a string.
The program must preserve uppercase and lowercase letters.
If the string is empty, print it intact."""

str=input("Enter a string")
z=len(str)
if(z==0):
    print("empty string")
else:
    print(str[::-1])