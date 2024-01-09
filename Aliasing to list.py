my_list = [0,1,3,4]

alias = my_list

my_list.append(5)
print("printing original list")

print(my_list)
print("printing alias list")
print(alias)

alias.append(6)
print("printing alias list")
print("alias list",alias)

print("printing original list")
print("original list", my_list)