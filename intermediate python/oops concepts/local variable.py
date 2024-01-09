class Myclass:
    def __init__(self):
        self.intance_variable = "this is intance variable"

    def my_method(self):
        local_variable = "this is local varible"
        print(local_variable)
        print(self.intance_variable)

x = Myclass()

x.my_method()

print(x.intance_variable)
