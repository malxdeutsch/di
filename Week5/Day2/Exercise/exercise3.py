from exercise import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        self.bark()
        self.trained = True
    def play(self,*args):
        print(f"{args}all play together")
    def do_a_trick(self):
        if self.trained == True:
            random_number = random.choice(range(1,5))
            if random_number == 1:
                print(f"{self.name} does a barrel roll")
            elif random_number == 2:
                print(f"{self.name} stands on his back legs")
            elif random_number == 3:
                print(f"{self.name} shakes your hand")
            else:
                print(f"{self.name} plays dead")

pet= PetDog("Gloria", 10, 20)
pet.train()
pet.play("Harry", "Charles", "Louis")
pet.do_a_trick()