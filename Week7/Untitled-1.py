def subsetsum(numbers , target):
    checkedNumbers = {}
    for num in numbers:
        if (target - num) in checkedNumbers: # 1 action :)
            print(f"True {num} + {(target - num)} = {target}")
            return True
        else:
            checkedNumbers[num] = True
    
    print(f"False {target}")
    return False


numbers = [3,8,6,-1,-4,10]
subsetsum(numbers,5)
subsetsum(numbers,89)
subsetsum(numbers,1)
subsetsum(numbers,11)