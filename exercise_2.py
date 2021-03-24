# Create a program that helps as waiter with his menu and his orders.

#Tasks
#User stories
# As a User I want to be able to see the menu in a formated way, so that I can order my meal.
# As a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten.
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# Let's create a dictionary to save the menu with name and the cost of each item

menu = {
    "Pizza": 5.0,
    "Burger": 3.0,
    "Fries": 1.5,
    "Chicken wings": 2.0,
    "Chicken and chips": 3.5
}

# Let's print the menu and the cost to the customer through a function

def print_menu():
    print("Item -------> Cost")
    print("-------------------")
    for item in menu:
        print(f"{item} -------> £{menu[item]}")

print_menu()

# Function to check if the item that the customer have ordered is in the menu

def check_item(name):
    is_available = False
    for key in menu:
        if key==name:
            is_available=True
            break
    return is_available

# We will use a list to save the items that the customer wants to order
order = []

# Let's ask the customer what items he wants to order
making_order = True
while making_order:
    item = input("Please enter the name of the item you wish to add in your order or END to finish the order: ")
    if item=="END":
        making_order=False
    else:
        if check_item(item)==True:
            print("Adding the item...")
            order.append(item)
        else:
            print("This item is not available in the menu, try again.")
