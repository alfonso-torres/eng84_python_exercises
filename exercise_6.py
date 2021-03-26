# EXERCISE 5

# Let's loop over some lists

# Tasks:
# Make a loop with a range that says hello 10 times.
# Create another loop with a range that asks for names and appends to list_names.
# Make a loop that iterates over each name in list_names and format's so that each name is lowercase,
# then add these names to a new list called list_names_lower
# Iterate over the list of values to find if they are even or not

list_names = []
list_names_lower = []

# Let's print "Hello" 10 times
i = 1
while i <=10:
    print("Hello")
    i +=1

# Function to get 10 names from the input
def get_names():
    #list_names_user = []
    x = 1
    while x <= 10:
        name = input("Please enter a name: ")
        list_names.append(name)
        x += 1

# Function to convert the names in lower case and append in a new list
def names_lower():
    for name in list_names:
        list_names_lower.append(name.lower())

# Function to print both list to see the difference between the names
def print_lists():
    y = 1
    for name_x in list_names:
        print(f"{y}. list_names : {name_x}")
        y += 1

    z = 1
    for name_y in list_names_lower:
        print(f"{z}. list_names_lower : {name_y}")
        z += 1

get_names()
names_lower()
print_lists()

# For loop to check what numbers of the list are even or not
list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for value in list_values:
    if value % 2 == 0: # Check if is even
        print(f"The number {value} is even.")
    else:
        print(f"The number {value} is not even.")

