# EXERCISE 1

# Create a program that calculates the year of birth!

# Tasks:
# Define the variables `name` and `age`.
# Calculate the year they were born.
# Print out `"OMG <person>, you are <age> years old so you were born in <year>"` with the correct values.

# Second part:

# Prompt the user for input and re-assign the variable `name` and `age`.
# Find out if the person's birthday has already happened this year or not.

import datetime

name = input("Please enter your name: ") # Get the user name
age = ""
user_prompt = True
while user_prompt: # Get the user age
    age = input(" Please enter your age: ")
    if age.isdigit(): # isdigit() is ensures to the user input is in digits
        user_prompt = False
    else:
        print("Please enter your age in Digits. ")

# Check if the persons birthday has already happened or not
birthday_info = input("Has your birthday already happened this year or not? (Y/N): ")

while birthday_info!="Y" and birthday_info!="N":
    birthday_info = input("Please select a correct answer, (Y/N): ")

current_date = datetime.datetime.now()
current_year = current_date.year # Getting the current year
age = int(age) # Casting to int to be able to operate
year = current_year-age
# Get the year they were born
if birthday_info=="N":
    year-=1

print(f"OMG {name}, you are {age} years old so you were born in {year}")

# One year is 8760 hours
age_in_hours = age*8760

print(f"You have lived about {age_in_hours} hours.")
