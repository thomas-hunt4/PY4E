
grocery_list = []


def add_item():
    item = input("What would you like to add to your list? ")
    grocery_list.append(item)
    print(f'This is your updated {grocery_list}')
    quit

def remove_item():
    item = input("What would you like to remove to your list? ")
    if item in grocery_list:
        grocery_list.remove(item)
        print(f'This is your updated {grocery_list}')
    else:
        print('Item not found')
    quit


def display_list():
    print(f"Here is your current grocery list: {grocery_list}")
    quit


def main():
    #   done = False
    # while not done:
        print('Grocery List')
        print('\n')
        print('1. Add item to list')
        print('2. Remove item from list')
        print('3. Display your list')
        print('4. Exit')
        print('\n')
        userselect = input("Select Option: 1-4 ")
    if int(userselect) == '1':
        # item = input('Enter item to add to list')
        add_item()
    elif int(userselect) == 2:
        remove_item() 
    elif int(userselect) == 3: 
        display_list()
    elif int(userselect) == 4:
        print('See you next time!')    
    else:
        Quit
    pass

# def main()
# while True:
#     userselect = input("What would you like to do? ")
#     if userselect == "add":
#         add_item()
#     elif userselect == "remove":
#         remove_item() 
#     elif userselect == "show list": 
#         display_list()
#     elif userselect == "quit"  

    # print(grocery_list)

# print(grocery_list)

# print(grocery_list)