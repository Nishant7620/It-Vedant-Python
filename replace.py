str=input("Enter a string")
cur_char=input("enter a char you want to replace")
new_char=input("enter a new char ")

if (new_char==""):
    print("you haven't entered any string")

else :
    print(str.replace(cur_char,new_char))

