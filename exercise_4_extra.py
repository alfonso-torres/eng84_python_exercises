# EXERCISE 4

# Super simple game that will substitute multiples of 3 and 5 for Fizz and
# Buzz respectively, or Fizzbuzz for multiples of the both.

# Tasks
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number.
# For the multiples of five print "Buzz" instead of the number.
# For numbers which are multiples of both three and five print "FizzBuzz".

# BUT MAKE IT FUNCTIONAL
# so we can decide which numbers to substitute for fizz and buzz using functions.

# Let's define the two variables to see with which is multiple or not
var_fizz = 3
var_buzz = 5

# Function to generate the correct prints
def generate_fizzbuzz(num1, num2):
    for number in range(1, 101, 1):  # For loop from 1 to 100
        if number % num1 == 0 and number % num2 == 0:  # Check if is multiple of both
            print("FizzBuzz")
        elif number % num1 == 0:  # Check if is multiple of fizz
            print("Fizz")
        elif number % num2 == 0:  # Check if is multiple of buzz
            print("Buzz")
        else:
            print(number)  # Not multiple

# Function to return the new value of Fizz in the case that user wants to change
def change_value_fizz():
    new_fizz = input("Enter new value for Buzz (Only DIGITS): ")
    while new_fizz.isdigit() == False: # Check if the input is not a digit
        new_fizz = input("Try again... (Only DIGITS): ")

    new_fizz = int(new_fizz) # Casting from String to int
    return new_fizz

# Function to return the new value of Buzz in the case that user wants to change
def change_value_buzz():
    new_buzz = input("Enter new value for Fizz (Only DIGITS): ")
    while new_buzz.isdigit() == False: # Check if the input is not a digit
        new_buzz = input("Try again... (Only DIGITS): ")

    new_buzz = int(new_buzz)
    return new_buzz

print("Welcome to the FIZZBUZZ game.")
# Ask user if the want to change the default values or not
answer = input("Would you like to change the default values of Fizz(3) and Buzz(5)? (Y/N): ")
run_program = True
while run_program:
    if answer == "N": # In the case if they want to keep the same values
        generate_fizzbuzz(var_fizz, var_buzz)
        run_program = False
    elif answer == "Y": # In the case if they want to change the values
        var_fizz = change_value_fizz()
        var_buzz = change_value_buzz()
        generate_fizzbuzz(var_fizz, var_buzz)
        run_program = False
    else:
        answer = input("Try again... (Y/N): ")
