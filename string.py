"""
str1 = "silent"
str2 ="listen"

if(len(str1)==len(str2)):
    print("true")

else :
    print("false")
"""
#---------------------------------------------------------------------------------------------------------------------------------
"""

str1 = "silent"
str2 ="listen"

for char in str1:
    if char in str2:
        print("true")

    else:
        print("false")
"""
#---------------------------------------------------------------------------------------------------------------------------------
"""
str1 = "silent"
str2 ="listen"

str3 =""

for char in str1:
    if char in str2:
        str3 = char    
        if str3 in str1:   
            print("true")

        else :
            print("false")    
        
"""
#-----------------------------------------------------------------------------------------------------------------------------------

str1 = "silent"
str2 ="listen"

all_prensent = True

for char in str1:
    if char not in str2:
         all_prensent = False
    else:
         True    


if all_prensent:
    print ("true")
else:
    print("false")

