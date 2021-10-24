string = input("Give me a string that is 10")
if len(string) < 10:
    print("string not long enough")
elif len(string) > 10:
    print("string too long")
else:
    first = string[0]
    print(first)
    last = string[-1]
    print(last)
broken = list(string)
empty_string = ""
for i in broken:
   empty_string += i
   print(empty_string)

import random
random.shuffle(broken)  
new_one = "".join(broken)
print(new_one)

    
