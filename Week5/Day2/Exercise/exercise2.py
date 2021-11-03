class Family:
    def __init__(self, members, last_name):
        self. members = members
        self.last_name= last_name
    def born(self, **kwargs):
        print(kwargs)
        self.members.append(kwargs)
        print("Congrats on the kid")

    def is_18(self, name, returndict = False):
        for person_dict in self.members:
            if name == person_dict["name"]:
                if int(person_dict["age"]) > 18:
                    if returndict == True:
                        return True, person_dict
                    return True
                else:
                    return False
    def try_print(self):
        for person_dict in self.members:
            print(person_dict["name"])

family1 = Family ([
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}], "Banks")

family1.born(name='Brody',age= 0, gender='Male', is_child =True)
family1.is_18("Sarah")
family1.try_print()

class TheIncredibles(Family):
    def __init__(self, members, last_name):
        super().__init__(members, last_name)
        for new_dict in self.members:
            new_dict["power"]= None
            new_dict["incredible_name"]= None

    def use_power(self, name):
        if self.is_18(name, True)[0]:
            print(f"{self.is_18(name, True)[1][power]}")
        else:
            raise Exception 
            print("Not over 18 years old")

    def incredible_presentation(self):
        for new_list in self.members:
            print(new_list["name"],new_list["incredible_name"],new_list["power"])
            

the_incredibles= TheIncredibles([
    {"name":'Bob','age':35,'gender':'Male','is_child':False, "power": "strength","incredible_name":"Mr. Incredible"},
    {"name":'Helen','age':32,'gender':'Female','is_child':False, "power": "elasticity", "incredible_name":"Elastigirl"},
    {"name":'Violet','age':14,'gender':'Female','is_child':True,"power": "invisible", "incredible_name":"Vio-let"},
    {'name':'Dashiell','age':10,'gender':'Male','is_child':True, "power": "speed", "incredible_name":"Dash"}
    ], "Parr")

print(the_incredibles)
print(the_incredibles.incredible_presentation())

the_incredibles.born(name='John Jackson',age=1,gender= 'Male',is_child =True, power='unknown power', incredible_name='Jack-Jack')

print(the_incredibles)
print(the_incredibles.incredible_presentation())