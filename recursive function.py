
"""
def display ():
    print("this is display function")
    display()

display()

"""
#-----------------------------------------------------------------------------------------------------------------------------------
"""
i = 0
def display():
    global i
    print(i)
    i+=1
    display()
display()           
"""
#----------------------------------------------------------------------------------------------------------------------------------
# set limit to recursive break 

import sys
sys.setrecursionlimit(10)
print(sys.getrecursionlimit())

i = 0

def  display ():
    global i
    print(i)
    i +=1
    display()
display()    

#---------------------------------------------------------------------------------------------------------------------------------