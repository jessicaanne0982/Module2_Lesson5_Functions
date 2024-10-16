 
beginning_list = [item for item in input("Let's get your list started! Enter your items : ").split()]

# Task 1
def add_item():
    beginning_list.append(input("Item to add: "))
 
# Task 2
def remove_item():
        beginning_list.remove(input("Item to remove: "))

# Task 3   
def print_list():
    print("Here is your shopping list:" "\n")
    print(*beginning_list, sep = "\n")

while True:
    choice = input("Would you like to add more, remove something, or see your final list? (Type: add, remove, or quit) ").lower()

    if choice == "quit":
        break
    elif choice == "add":
            add_item()
    elif choice == "remove":
        remove_item()
    
print_list()


