
grocery_list = []

# item = grocery_list

def add_item():
    item = input("What would you like to add to your list? ")
    grocery_list.append(item)
    print(f'This is your updated {grocery_list}')
    quit

# def remove_item(item):


def display_list():
    print("Grocery list: ")
    for item in grocery_list:
        print(f"Here is your current grocery list: {grocery_list}")



while True:
    userselect = input("What would you like to do? ")
    if userselect == "add":
        # item = input("Enter an item to add to your list: ")
        add_item()
    elif userselect == "remove":
        item = input("Enter an item to remove from your list: ") 

    elif userselect == "show list": 
        print(grocery_list)  

    # print(grocery_list)

# print(grocery_list)

# print(grocery_list)