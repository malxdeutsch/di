string = "7i3Tsih%xi #sM $a #t%^r!"
first_column = [string[i] for i in range(0, len(string), 3)] 
print(first_column)
second_column = [string[i] for i in range(1, len(string), 3)]
print(second_column) 
third_column = [string[i] for i in range(2, len(string), 3)] 
print(third_column)
alpha =""
for index in range(0,len(first_column)-1):
    index2 = index + 1
    if first_column[index].isalpha():
        alpha += first_column[index]
    else:
        if first_column[index2].isalpha()== False:
           alpha+=" "
        else:
            continue
    if index2 == len(first_column):
        break

for index in range(0,len(second_column)-1):
    index2 = index + 1
    if second_column[index].isalpha():
        alpha += second_column[index]
    else:
        if second_column[index2].isalpha()== False:
           alpha+=" "
        else:
            continue
    if index2 == len(second_column):
        break 

for index in range(0,len(third_column)-1):
    index2 = index + 1
    if third_column[index].isalpha():
        alpha += third_column[index]
    else:
        if third_column[index2].isalpha()== False:
           alpha+=" "
        else:
            continue
    if index2 == len(third_column):
        break
print(alpha)  