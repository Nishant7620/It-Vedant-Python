
def main():
    def child():
        print("child function")
    print("main function")
    child()
main()        

#---------------------------------------------------------------------------------------------------------------------------------------
def outer_fun():
    def inner_fun():
        print("Inner Function")
    print("outer Function")
    inner_fun()
outer_fun()    

#----------------------------------------------------------------------------------------------------------------------------------------
#Nested function with return statement

def outer_fun ():
    def inner_fun():
        return "inner function"
    return inner_fun() +" " + "Outer function"
print(outer_fun())        



#---------------------------------------------------------------------------------------------------------------------------------------

def outer_fun():
    def inner_fun():
        return "Inner function"
    result= inner_fun() + " "+ "Outer function"
    return result
print(outer_fun())        