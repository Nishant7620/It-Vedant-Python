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

