dict = {"a":1,"b":2,"c":3,"d":4}

print(dict)
#-----------------------------------------------------------------------------------------------------------
#accessing value of dictiontary by using key
dict1 = {"a":1,"b":2,"c":3,"d":4}
print(dict["a"])


#-----------------------------------------------------------------------------------------------------------
# empty dictionary
dict  = {}
print(dict)

#---------------------------------------------------------------------------------------------------------
#clear method
dict = {"a":1,"b":2,"c":3,"d":4}

dict.clear()
print(dict)

#----------------------------------------------------------------------------------------------------
#copy() method

dict = {"a":1,"b":2,"c":3,"d":4}

copy_dict =dict.copy()

print(copy_dict)

dict["a"]=99
print(dict)
print(copy_dict)
copy_dict["a"]=100
print(dict)
print(copy_dict)
#-------------------------------------------------------------------------------------------------------------------
#shallow copy


original_dict = {"a":1,"b":[1,2],"c":3,"d":4}

print(original_dict["b"])
print(f"original dictionary",original_dict["b"][1])

copied_dict =original_dict.copy()

print(copied_dict)

copied_dict["b"][1] =99

print("copied dictionary",copied_dict)
print("original dictionary",original_dict)

original_dict["b"][0] =100
print("original dictionary",original_dict)
print("copied dictionary",copied_dict)

#---------------------------------------------------------------------------------------------------------------
#deep copy method

import copy 


original_dictionary = {"a":1,"b":[3,4],"c":3,"d":4}

copied_dictionary =copy.deepcopy(original_dictionary)


original_dictionary["b"][0]=5
print("original dictionary",original_dictionary)
print("copied_dictionary",copied_dictionary)

#------------------------------------------------------------------------------------------------------------
#from key method 

keys =["a","b","c","c"]
default_values = 100

my_dict =dict.fromkeys(keys,default_values)
print(my_dict)

#-------------------------------------------------------------------------------------------------------
# with multiple values

default_values = 100,200
my_dict =dict.fromkeys(keys,default_values)
print(my_dict)

#----------------------------------------------------------------------------------------------------
k =["a","b","c","d"]

dict2 = dict.fromkeys(k)
print(dict2)

#------------------------------------------------------------------------------------------------
#get method ()

d = {"a":1,"b":2,"c":3,"d":4}

value_of_a = d.get("a")
value_of_b = d.get("b")
print(value_of_a)
print(value_of_b)

value_of_e =d.get("e",5) #key is not present in dictionary

print(value_of_e)

#--------------------------------------------------------------------------------------------------------
#item method

di = {"a":1,"b":2,"c":3,"d":4}

items = di.items()

print(items)

#-----------------------------------------------------------------------------------------------------------
#accessing key value pair usng loop

di = {"a":1,"b":2,"c":3,"d":4}

for key,value in di.items():
    print(key,value)

#-------------------------------------------------------------------------------------------------------
# keys () method
# 
di = {"a":1,"b":2,"c":3,"d":4}

key_views =di.keys()

print(key_views)

#----------------------------------------------------------------------------------------------------
#values () method


di = {"a":1,"b":2,"c":3,"d":4}

values = di.values()

print(values)

#-------------------------------------------------------------------------------------------------------
#pop method 


di = {"a":1,"b":2,"c":3,"d":4}

value =di.pop("b")
print(value)
print(di)

value2 =di.pop("x",0)

print(value2)
print(di)

#-------------------------------------------------------------------------------------------------
#pop items method


di = {"a":1,"b":2,"c":3,"d":4}

remove_items = di.popitem()   #remove last pair from dictionary
print(remove_items)
print(di)
#--------------------------------------------------------------------------------------------------
#setdefault


di = {"a":1,"b":2,"c":3,"d":4}

value_a = di.setdefault("a",100)

print(value_a)
print(di)

value_e =di.setdefault("e",200)
print(value_e)
print(di)

#-------------------------------------------------------------------------------------------------------
#update method 

my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict.update({"a":100})

print(my_dict)
#----------------------------------------------------------------------------------------------------
#merging dictionaries

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict2 = {'d': 4, 'e':5 , 'g': 6}

my_dict.update(my_dict2)

print(my_dict)

