class Animal:
    pass

class Lion:
    
   def feed(self):
    return "eats meat"

class Parrot:
    def feed(self):
        return "eats seeds"

class Cat:
    def feed(self):
        return "drink milk"

#creating instance of classes
lion = Lion()
parrot = Parrot()
cat = Cat()

print(lion.feed())
print(parrot.feed())
print(cat.feed())


