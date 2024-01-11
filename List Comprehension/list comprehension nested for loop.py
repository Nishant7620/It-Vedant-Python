#nested for loop 
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

for i in list1:
    for  j in list2:
        print(i,j)

#-----------------------------------------------------------------------------
#nested for loop using comprehension list
list1 = [1,2,3,4]
list2 = [5,6]
pairs =  [(i,j) for i in list1 for j in list2]
print(pairs)

#-----------------------------------------------------------------------------
#nest listed

l = [[1,2,3],[4,5,6],[7,8,9]]

for i in l:
    for j in i:
        if j%2==0:
            print(j)

#--------------------------------------------------------------------------
# nested list using list comprehension

l = [[1,2,3],[4,5,6],[7,8,9]]            

result = [j for i in l for j in i if j%2==0]

print(result)