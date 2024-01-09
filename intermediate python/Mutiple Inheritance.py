class Dad:
    def __init__(self):
        super().__init__()
        print("this is Dad Constructor")

class Mom:
    def __init__(self):
        super().__init__()
        print("this is Mom Constructor")

class Child(Dad,Mom):
    def __init__(self):
        super().__init__()
        print("this is Child Constructor")

c = Child()
