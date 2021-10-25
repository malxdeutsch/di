birthday = input("What is your birthday? Answer in DD/MM/YYYY format.")
day = birthday[:birthday.find("/")]
month = birthday[birthday.find("/")+1:birthday.rfind("/")]
year = int(birthday[birthday.rfind("/")+1:])
age = 2021 - year
last_digit = age % 10.
dashes = (11-last_digit)/2
new_dash = ""
new_i=""
for number in range(1,12):
    if number <= dashes:
        new_dash += ("-")
    elif number <= dashes+last_digit:
        new_i += ("i")
print("   ",new_dash,new_i,new_dash,"  ")  
print("  ","|",":H:a:p:p:y:","|","  ")
print( "__","|","___________","|","__")
print( "|","^^^^^^^^^^^^^^^^^","|")
print("|",":B:i:r:t:h:d:a:y:","|")
print("|","                 ","|")
print(" ~~~~~~~~~~~~~~~~~~~")


