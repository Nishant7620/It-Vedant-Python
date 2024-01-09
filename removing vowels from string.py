str1 = input("enter a string: ")
str_list =list(str1)

vowels = ["a","e","i","o","u"]

for i in vowels:
    if i in str_list:
        str_list.remove(i)
        string= "".join(str_list)
print(string)