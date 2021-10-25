my_set ={1, 2, 4, 10}
my_fav_numbers= my_set
my_fav_numbers.add(12)
my_fav_numbers.add(18)
my_fav_numbers.remove(18)
print(my_fav_numbers)
new_set = {"CML", "Hindel", "Bazel"}
friend_fav_numbers = new_set
set_3 = friend_fav_numbers | my_fav_numbers
our_fav_numbers= set_3
print(our_fav_numbers)

# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# No


for number in range(1,21):
    print(number)

# Recap – What is a float? What is the difference between an integer and a float?
 # It is a decimal, and an integer is a whole number.
# Can you think of another way to generate a sequence of floats?
 # In a list
 #Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
  # list =["1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5"]
  #print([float(x) for x in a])

basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana") 
basket.remove("Blueberries")
basket.append("kiwi")
basket.insert(0,"Apples")
count = basket.count("Apples")
print(count)
basket.clear()
print(basket)

active = True
while active:
    user_input = input("what is your name")
    if user_input == "Malka":
        active = False

my_list = list(range(1,50))
for obj in my_list:
   index = my_list.index(obj)
   if index%2==0:
       print(obj)

for digit in range(1500, 2501):
    if digit%5==0 and digit%7==0:
        print(digit)

user_fruits= input("List one or more of your favorite fruits with a space in between")
list2 = user_fruits.split(" ")
user_again = input("Name any fruit")
if user_again in list2:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")


list3 =[]
while True:
    pizza_username = input("Enter a series of pizza toppings")
    if "quit" == pizza_username:
        break
    toppings = pizza_username.split()
    print("I'll add", toppings, "to the pizza")
    list3 += toppings
    
print(list3)
total = len(list3)
print((total*2.5)+10)

list4 = []
total = 0
ages = input("List each person's age").split(",")
for age in ages:
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
print(total)

list5 = []
teen = ["Greg", "Ashley", "Luna"]
for ten in teen:
    restricted= (input("How old are you?"))
    restricted= int(restricted)
    if restricted >= 16 and restricted <= 21:
      list5.append(ten)
print(list5)

list6 = ["Tom", "Harry", "John"]
for new_name in list6:
    new_remove = (input("How old are you?"))
    new_remove= int(new_remove)
    if new_remove < 16:
        list6.remove(new_name)
print(list6)

sandwich_orders= ["deli","pastrami","pbj","pastrami","tuna","pastrami"]
finished_sandwiches = []
print("The deli has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
for idx in range(len(sandwich_orders)):
    finished_sandwiches.append(sandwich_orders[idx])
    print("I have made your", sandwich_orders[idx],"sandwich")
for sandwich in finished_sandwiches:
    if sandwich in sandwich_orders:
        sandwich_orders.remove(sandwich)
print(sandwich_orders)
print(finished_sandwiches)




        

    
