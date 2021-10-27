def display_message():
    print("I am learning python in this course")

display_message()

def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Pride and Prejudice")

def describe_city(city, country="USA"):
    print(f"{city} is in {country}")
describe_city("Atlanta")

import random
def our_number():
    entry = int(input("Give a number"))
    if  1 < entry < 100:
        print(entry)
    else:
        entry = int(input("Give a number"))
    new_random =random.randint(1,100)
    print(new_random)
    if entry == new_random:
       print("Success!")
    else:
        print(f"Fail, you got {entry} and {new_random}")
our_number()

def make_shirt(size = "large", text = "I love python"):
    print(f"The shirt should be size {size} and print {text} on it")
make_shirt("small","first cousin")
make_shirt()
make_shirt(size = "medium")
make_shirt(size = "small", text = "I hope this is right")

magicians = ["Houdini", "Shimon", "Copperfield"]

def show_magicians():
    for magician in magicians:
       print (magician)
show_magicians()
def make_great():  
    for i in range(len(magicians)):
       magicians[i] = magicians[i] +" "+ "the Great"
make_great()
show_magicians() 

    
