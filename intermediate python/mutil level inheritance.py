class Parent:
    def __init__(self):
        print("Parent Constructor")

    def parent_property(self):
        print("parent's property")

class Child(Parent):
    def __init__(self):
        print("Child constructor")

    def child_property(self):
        print("child's property")


class GrandChild(Child):
    def __init__(self):
        super().__init__()
        print("Grand Child constructor")

    def Grand_property(self):
        print("Grand Child's property")

gc = GrandChild()

gc.child_property()

gc.parent_property()



