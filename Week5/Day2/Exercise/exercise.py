class Pet():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}' 

cat1 = Bengal("Tom", 20)
cat2 = Persian("Ira", 5)
cat3 = Chartreux("Theresa", 11)

cat_list = [cat1, cat2, cat3]

my_pets = Pet(cat_list)

my_pets.walk()

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self. age = age
        self. weight = weight
        self.speed = self.run_speed()
    def bark(self):
        bark_string = (f"{self.name} is barking")
        print(bark_string)
        return bark_string
    def run_speed(self):
        new_weight = (self.weight/self.age)*10
        return new_weight
    def fight(self, other_dog):
        speed = int(self.speed * self.weight)
        speed1 = int(other_dog.speed * other_dog.weight)
        if speed > speed1:
            winner_string = (f"{self.name} won the fight")
            return winner_string
        else:
            winner_string = (f"{other_dog.name} won the fight")
            return winner_string
            
dog1 = Dog("Larry", 5,10)
dog2 = Dog("George", 10, 35)
dog3 = Dog("Freddy", 15, 25)

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))


