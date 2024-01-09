str =input("Enter a string: ")

def reversed (string):
    x =""
    for char in string:
        x=char+x
    return x

print(reversed(str))        



    