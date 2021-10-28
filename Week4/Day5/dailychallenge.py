new_input = input("List some words seperated by commas")

new_list = [word+word.join(",") for word in sorted(new_input.split(","))]

print(new_list) 