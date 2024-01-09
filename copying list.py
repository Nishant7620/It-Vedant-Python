list = [1,2,3,4,5,6,7,8]

copy = list.copy()

print(copy)

#----------------------------------------------------------------------------------------------------------------------------------

original_list = [1,2,3,4,5,6]

shallow_list = original_list.copy()

print(shallow_list)

shallow_list[1]="A"

print(shallow_list)
print(original_list)

original_list[2]="C"

print(original_list)
print(shallow_list)

#---------------------------------------------------------------------------------------------------------------------------------------
# in nested list if you update or modify any item of nested list it will affect copy list 
list =[1,2,3,[4,5],6]

shallow_list =list.copy()

print(shallow_list)

list[3][0]="a"
print(list)
print(shallow_list)


shallow_list[3][1]="c"
print(shallow_list)
print(list)

#---------------------------------------------------------------------------------------------------------------------------------
#copying list using slicing method

list = [1,2,3,[4,5],6]

my_list =list[:]
print(my_list)

#modifying nested list affect on both original as well as copy list

list[3][0]="x"
print(list)
print(my_list)

my_list[3][1]="y"
print(my_list)
print(list)

#modifying list will not affect copy list or original list

list[1]="hello"
print(list)
print(my_list)

my_list[0]="A"
print(my_list)
print(list)

#--------------------------------------------------------------------------------------------------------------------------------
#copying list using deepcopy method
import copy
list = [1,2,3,[4,5],6]

deep_copy = copy.deepcopy(list)

print(deep_copy)

list[3][0]="A"
print(list)
print(deep_copy)