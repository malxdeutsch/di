import random


class Gene:
    def __init__(self):
        self.gene = random.choice([0,1])

    def flip(self):
        self.gene = -1*(self.gene-1)

    def __str__(self):
        return str(self.gene)


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for i in range (10)]

    def flip(self):
        probablity = 50
        for gene in self.genes:
            rand_num = random.randint(0,100)
            if rand_num>probablity:
                gene.flip()
            else:
                continue

    def check_if_all_1(self):
        return all(gene.gene for gene in self.genes)                

    def __str__(self):
        output = []
        for gene in self.genes:
            output += str(gene) 
        return ','.join(output)
        

class Dna:
    def __init__(self):
        self.chromosome = [Chromosome() for i in range (10)]

    def flip(self, probablity = 50):
        for chromo in self.chromosome:
            rand_num = random.randint(0,100)
            if rand_num>probablity:
                chromo.flip()

    def check_if_all_1(self):
        for chromo in self.chromosome:
            if not chromo.check_if_all_1():
                return False
        return True

    def __str__(self):
        output = []
        for chromo in self.chromosome:
            output += str(chromo)+"\n"
        return ''.join(output)


class Organism:
    def __init__(self, DNA, probability):
        self.DNA = DNA
        self.probability = probability
    
    def gens_till_1(self):
        generation = 0
        while not self.DNA.check_if_all_1():
            generation += 1
            self.DNA.flip()
        return generation
        
    
organism1 = Organism(Dna(),70)
organism2 = Organism(Dna(),50)
organism3 = Organism(Dna(),45)
organism4 = Organism(Dna(),65)


my_list = [organism1, organism2, organism3, organism4]

for organism in my_list:
    generations_taken = organism.gens_till_1()
    print(f"{organism.probability} took {generations_taken}")

