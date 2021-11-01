class Farm():
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, number = 1):
        if animal in self.animals:
            self.animals[animal] += number
        else:
            self.animals[animal] = number
        return number
    def get_info(self):
        for animal,number in self.animals.items():
            print(f"{animal} : {number}")
        return "E-I-E-I-0!"

    def get_animal_types(self):
       return (sorted(self.animals))
    
    def get_short_info(self):
        string = ", ".join(self.get_animal_types())
        print(f"{self.name} has {string}")



macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()


