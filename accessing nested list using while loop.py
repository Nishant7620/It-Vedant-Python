my_list = [[1,2,3],[4,5,6],[7,8,9]]

index = 0
while index < len(my_list):

    j = 0
    while j < len(my_list[index]):
        print (f"Index [{index}] [{j}]:",my_list[index][j],end=" ")

    j+=1          
    print()
    index = index+1




