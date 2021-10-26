keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)


total = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for name, age in family.items():
    age= int(age)
    if age < 3:
        ticket = 0
        total+= ticket
    elif age > 3 and age < 12:
        ticket = 10
        total+= ticket
    else:
        ticket = 15
        total+= ticket
    print(name,ticket)
    print(total)

brand = {
"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"], 
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color": {
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]
    }
}

brand["number_stores"]=2
print(brand["number_stores"])
print("Zara clients are", brand["type_of_clothes"])
brand["country_creation"]="Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][3])
print(brand["major_color"]["US"])
print(len(brand))
for key in brand.keys():
    print(key)
more_on_zara ={
"creation_date": 1975,
"number_stores": 10000
}

brand.update(more_on_zara)
print(brand["number_stores"])
#  it replaced the value stored there before

disney_users_a ={}
disney_users_b ={}
disney_users_c ={}
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
for index, value in enumerate(users):
    if "i" in value and value.startswith("M") or value.startswith("P"):     
        disney_users_a [value] = index     
print(disney_users_a)
for index, value in enumerate(users):
    disney_users_b [index] = value
print(disney_users_b)
new_users = sorted(users)
for value, index in enumerate(new_users):
    disney_users_c [index] = value
print(disney_users_c)