class Person:
    def __init__(self, name, age):
        self.name = name
        self. age = age
    def __abs__ (self):
        return abs(self.age)
    def __int__ (self):
        return int(self.age)
    def __input__ (self):
        return input(self.name)
    def __repr__ (self):
        return f"{(self.name)} {(self.age)}"
    
person1= Person("Henry", 44)
print(person1)

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__ (self):
        return str(f"{self.amount} {self.currency}")

    def __int__ (self):
        return int(self.amount)

    def __repr__ (self):
        return repr(f"{self.amount} {self.currency}")

    def __add__ (self, other):
        self.check(other)
        if type(other) == int:
            total = self.amount + other
            return total
        else:
            total = self.amount + other.amount
            return total
    
    def __iadd__ (self, other):
        if type(other) == int:
            self.amount += other
            return Currency(self.currency, self.amount)
        else:
            
            self.amount += other.amount
            return Currency(self.currency, self.amount)

    def check(self,other):
        if type(other)== Currency:
            if not self.currency == other.currency:
                raise TypeError 
                print(f"Cannot add between Currency type {self.currency} and {other.currency}")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1+=5
print(c1)
c1+=c2
print(c1)
print(c1 + c3)