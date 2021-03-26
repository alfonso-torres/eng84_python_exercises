# EXERCISE 3

# Create a list of xmas gifts using cool control flow

# Tasks
# User stories
# As a user, I want to be able to add items to the list, so I can read it later.
# As a user, I want to be able to keep adding things to the list until I use exit
# As as user, I should be able to use the word exit in a sentence and still have the program terminate, so that anyone can use it
# As a user, when the program exits, I want to see the complete list in caps lock and numbered, so that I know what to buy. Example: <br/>
#  1 - RC car <br/>
#  2 - PS2 <br/>
#  3 - GTA Vice City
# Hint: while loops and break conditions, use list and append, iterate to print

#Function to create the list of gifts we want for Christmas
def create_lists_gifts():
    list_gifts = [] # List where we will add the gifts
    list_xmas = True
    while list_xmas: # Loop to ask to the customer from the input about what he want
        item = input("Please enter the name of the gift you want for Christmas (EXIT to finish): ")
        if item == "EXIT": # In the case of the user doesn't want to add anything else
            list_xmas = False
        else:
            print(f"Adding the gift {item} ...... ")
            list_gifts.append(item) # Adding in the list

    return list_gifts # Return the list of gifts

# Call the function to generate the list
user_xmas_list = create_lists_gifts()

# Check if the user added items into the list
if len(user_xmas_list) == 0:
    print("You didn't add anything in the Christmas list...")
else:
    print("Here is your Christmas list:") # Let's print the list of Christmas
    for item in user_xmas_list: # Loop to iterate into the Christmas list
        print(f"- {item}")
