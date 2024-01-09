"""
def parent ():
    def child():
        return ("This is child function")
    print("This is parent")
    return child

result =parent()
print(result())
"""
#--------------------------------------------------------------------------------------------------------------------------------------
"""
def create_machine():
    def machine():
        print("this is machine function")
        return ("When machine is created it is store here")
    print("Machine will create here")
    return machine
result = create_machine() 

print(result())
"""
#--------------------------------------------------------------------------------------------------------------------------------------
# returning with parameter
"""
def create_machine(mach):
    print("Machine will create here")
    return mach

def machine():
    print("machine will store here")
    return ("this is machine function")

result =create_machine(machine)     
print(result())
#---------------------------------------------------------------------------------------------------------------------------------------
"""
"""

def create_machine(mach):
    def machine():
        print("this is machine function")
        return mach()
    print("this is create machine function")
    return machine

def another_machine():
    print("this is another machine")

result = create_machine(another_machine)

print(result())
"""

#--------------------------------------------------------------------------------------------------------------------------------
def create_multiplier (factor):
    def multiplier(x):
        return factor*x
    return multiplier    

multiply_by_2 =create_multiplier(2)
multiply_by_3 = create_multiplier(3)
result1 =multiply_by_2(5)
result2 =multiply_by_3(7)
print(result1)
print(result2)
        