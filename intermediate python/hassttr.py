class Animal:
    pass

class Dog:
    def speak(self):
        return "woof!"

class Cat:
    def speak(self):
        return "Meow"

class Duck:
    def run(self):
        return "run"

def make_sound(animal):
    
    animal.speak()

    if hasattr(animal,"speak"):
            print(animal.speak())


dog = Dog()
cat = Cat()
duck = Duck()

make_sound(dog)
make_sound(cat)
make_sound(duck)