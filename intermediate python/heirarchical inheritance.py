class Parent:
    def __init__(self):
        print("this is parent constructor")

    def parent_property(self):
        print("this is parent's property") 

class Brother(Parent):
    def __init__(self):
        print("this is brother constructor")

    def Brother_property(self):
        print("this is brother property")

class Sister(Parent):
    def __init__(self):
        print("this is sister's constructor")

    def sister_property(self):
        print("this is sister property")

# creating instace of brother class

b = Brother()

b.Brother_property()

#b.sister_property()

b.parent_property()

# creating an instace of sister class

s = Sister()

#s.Brother_property()

s.parent_property()

#creating instance of parent class

p = Parent()

p.parent_property()

#p.Brother_property()

