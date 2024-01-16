"""
def make_pretty(func):
    def inner ():
        print("i got decorated")
        func()
    return inner

def ordinary():
    print("i am ordinary")

result = make_pretty(ordinary)
result()

"""
def make_pretty(func):
    def inner ():
        print("i got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("i am ordinary")

ordinary()

#-------------------------------------------------------------------------------
def add(num):
    def wrap():
        r=10
        result = num() + r
        return result
    return wrap

def mul(num):
    def wrap():
        r = 20
        result = num() * r
        return result
    return wrap    
@mul
@add
def num():
    return 5

print(num())

