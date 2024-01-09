list = [1,2,3,[4,5],6]

print(list)
print(list[3][1])

#----------------------------------------------------------------------------------------------------------------------------------
#modifying nested list

list = [1,2,3,[4,5],"hello",[6,7,8]]

list[3] = 4
print(list)



#adding element to inner list

list[5].append(9)
print(list)

#replacing entire list
list[5] =[10,11,12,13]
print(list)