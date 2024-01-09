list = [1,2,3,4,5,6]

def my_list (l):
    for i in l:
        print(i)

my_list(list)

#---------------------------------------------------------------------------------------------------------------------------------


def even_number_list (even):
        result = []
        for i in range(2,even+1,2):
            result.append(i)
        return result

even_list = even_number_list(10)

print(even_list)

