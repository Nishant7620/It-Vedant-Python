nested_list = [[1,2,3],[4,5,6],[8,9,10]]

for i in nested_list:
    for j in i:
        print(j,end=" ")
    print()

#------------------------------------------------------------------------------------------------------------------------------------
#accessing nested list with different element in the list

print('---- Accessing Nested list with different element in the List ----- ')
nested_list = [1, [2, 3, 4], 'hello', [5, 6], 7]

for i in range(len(nested_list)):
    if type(nested_list[i]) is list:
        if len(nested_list[i])>1:
            x=len(nested_list[i])
            for j in range(x):
                print(f"Index [{i}] [{j}] :",nested_list[i][j])
            
    else:
        print(f"Index [{i}] :",nested_list[i])

print()


