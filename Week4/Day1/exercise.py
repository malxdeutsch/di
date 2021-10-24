print(("Hello" + " " + "World" + " ")*4)

print((99^3) * 8)

5 < 3
#False
3 == 3
#True
3 == "3"
#False
#"3" > 3
#TypeError: '>' not supported between instances of 'str' and 'int'
#"Hello" == "hello"
#TypeError: '>' not supported between instances of 'str' and 'int'

computer_brand = "mac"
print(f"I have a {computer_brand} computer")

name = "Malka"
age = "24"
shoe_size = "7.5"
info = f" My name is {name}, I am {age} years old, and my shoes are a size {shoe_size}"
print(info)

a = 10
b = 20
if a > b:
    print("Hello World")

question = int(input("Pick a number"))
if question%2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")


prompt = input("What is your name?")
if prompt == "Malka":
    print(" You have the prettiest name in the world")
else:
    print("Your name is pretty, but not as pretty as mine")


height = int(input("What is your height in inches?"))
if height > 145:
    print("You are tall enough to ride")
else:
    print("You need to grow more in order to ride")






