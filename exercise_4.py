# EXERCISE 4

# Super simple game that will substitute multiples of 3 and 5 for Fizz and
# Buzz respectively, or Fizzbuzz for multiples of the both.

# Tasks
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number.
# For the multiples of five print "Buzz" instead of the number.
# For numbers which are multiples of both three and five print "FizzBuzz".

for number in range(1,101,1): # For loop from 1 to 100
    if number % 3 == 0 and number % 5 == 0: # Check if is multiple of 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0: # Check if is multiple of 3
        print("Fizz")
    elif number % 5 == 0: # Check if is multiple of 5
        print("Buzz")
    else:
        print(number) # Not multiple of 3 and 5
