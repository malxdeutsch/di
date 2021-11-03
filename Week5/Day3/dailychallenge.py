class Circle():
    def __init__(self, r =0 , d = 0):
        self.radius = r
        self.diameter = d
        self.diameter = self.radius * 2

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14
    
    def __repr__(self):
        return f"radius is {self.radius} " 
    
    def __add__(self, other):
        total = self.radius + other.radius
        return total
    
    def __gt__(self, other):
        if type(other) == int or float:
            return self.radius > other.radius
    
    def __eq__(self, other):
        if type(other) == int or float:
            return self.radius == other.radius

new_circle = Circle(8)
other_circle = Circle(4)
my_list = [new_circle, other_circle]

print(new_circle)
print(new_circle.area())
print(new_circle.perimeter())
print(new_circle + other_circle)
print(new_circle > other_circle)
print(new_circle == other_circle)
print(sorted(my_list))