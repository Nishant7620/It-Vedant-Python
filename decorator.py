
def add (num):
    print("this is add function")
    def wrap():
        a=10
        return a+num()       
    return wrap


def mul (num):
    print("this is mul  function")
    def wrap():
        b=2
        return b*num()
    return wrap  
def num():
    return 20


result = add(num)
print(result())