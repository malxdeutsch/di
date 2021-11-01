class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
cat_list = [Cat("Greg", 14), Cat("Ford", 11), Cat("Hetty", 3)]


def oldest_cat():
    cat = sorted(cat_list, key = lambda cats:cats.age)[-1]
    print(f"The oldest cat is {cat.name}, and is {cat.age} years old.")
    return cat

oldest_cat()


class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        new_height = int(self.height)*2
        print(f"{self.name} jumps {new_height} cm high!")

davids_dog = Dog("Rex", 50)
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog= Dog("Teacup", 20)
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

def bigger_dog(dog1, dog2):
    if dog1.height > dog2.height:
        print(f"{dog1.name} is bigger")
    else:
        print(f"{dog2.name} is bigger")

bigger_dog(davids_dog, sarahs_dog)

class Song():
    def __init__(self, lyrics=[]):
        self.new_lyric = lyrics
    def sing_me_a_song(self):
        print(*self.new_lyric, sep =" \n")

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


class Zoo():
    groups={}
    def __init__(self, zoo_name):
       self.animals = []
       self.name = zoo_name
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal) 
    def get_animals(self):
        print(self.animals)
    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        for word in sorted(self.animals):
            groups.setdefault(word[0],[]).append(word)
    def get_groups(self):
        print(groups.value())

ramat_gan_safari = Zoo("Atlanta_Zoo")




        
