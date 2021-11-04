import random

def get_words_from_file():
    with open('word.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
    
lines = get_words_from_file()


def get_random_sentence(lines,length):
    sentence = ""
    for random_word in range(0,length):
        sentence += random.choice(lines) + " "
    return sentence.lower()

def main():
    print("This is taking words from a random list and making a sentence with it.")

main()

def new_input():
    length= input("How many words should the sentence be?")
    if length.isnumeric():
        if int(length) > 2 and int(length) < 20:
            return int(length)
        else:
            print("Error")
            return
    else:
        print("Error")
        return

length = new_input()
print(get_random_sentence(lines, length))


import json

with open('try.json', 'r') as file:
    sample_Json= json.load(file)

print(sample_Json["company"]["employee"]["payable"]["salary"])
sample_Json["company"]["employee"]["birth_date"] = "4/21/2021"

with open('try.json', 'w') as file:
   json.dump(sample_Json, file, indent =2)