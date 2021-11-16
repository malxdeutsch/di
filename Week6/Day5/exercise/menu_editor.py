from menu_item import MenuItem

def show_user_menu():
    choose = input("A)Add an Item\n D) Delete an Item \n V) View the Menu \nX)Exit \n").upper()
    return choose

def add_an_item():
    new_item = input ("Add an item")
    new_price= int(input("Add price"))
    new_one= str(MenuItem(new_item, new_price))
    new_one.save()
    print(f"{new_one} was added successfully.")

def remove_item_from_menu():
    item_to_remove = input ("What item would you like to delete")
    for item in MenuItem.all():
        if item[0] == item_to_remove:
            new_delete= MenuItem.delete(new_item)
            print(f"{new_delete} was deleted successfully.")


def main():
    choice = show_user_menu()
    while choice != "X":
        if choice == "A":
            add = str(add_an_item())  
            print(add)
            return add                      
        elif choice == "D":
            remove = remove_item_from_menu()
            return remove
        elif choice == "V":
            print(MenuItem.all())
            break
    print(str(MenuItem.all()))
    return



main()
