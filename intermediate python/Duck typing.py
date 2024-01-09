class Animal:
    pass

class Dog:
    def speak(self):
        return "woof!"

class Cat:
    def speak(self):
        return "Meow"

class Duck:
    def speak(self):
        return "Quack"

def make_sound(animal):
    return animal.speak()


dog = Dog()
cat = Cat()
duck = Duck()

print(make_sound(dog))
print(make_sound(cat))
print(make_sound(duck))