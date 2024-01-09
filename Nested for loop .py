x = [1,2,3,4,5,6]
s =["a","b","c","d","e","f"]

for i in x:
    for j in s:
        print(i,j)

#-----------------------------------------------------------------------------------------

list1 = [0,1,2]
list2 = ["a","b","c"]

nested = [(x,y) for x in list1 for y in list2]

print(nested)

#-----------------------------------------------------------------------------------------

l = [[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    for j in i:
        if j%2==0:
            print(j)

even_number = [j for i in l for j in i if j%2==0] 

print(even_number)