# EXERCISE 5

# Lets make a functional calculator.

# Tasks:
# Create an `add` function.
# Create a `subtract` function.
# Crate a `multiply` function.
# Create a `divide` function.
# Create an `area of a circle` function.
# Create an `area of a square` function.
# Create an `area of a triangle` function.

# Run the function with arguments

import math # Import to use same functions of the module math

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function calculates the area of a circle
def area_circle(radius):
    return multiply(math.pi, math.pow(radius,2))

# This function calculates the area of a square
def area_square(side):
    return multiply(side, side)

# This function calculates the area of a triangle
def area_triangle(base, height):
    return divide(multiply(base, height), 2)

# Let's go to call all of them
print("Let's go to call add function with 10 and 30. We expect 40 as a result...")
print(add(10, 30) == 40)

print("Let's go to call subtract function with 30 and 10. We expect 20 as a result...")
print(subtract(30, 10) == 20)

print("Let's go to call multiply function with 3 and 5. We expect 15 as a result...")
print(multiply(3, 5) == 15)

print("Let's go to call divide function with 15 and 5. We expect 3 as a result...")
print(divide(15, 5) == 3)

print("Let's go to call area_circle function with a radius of 2. We expect 12.5663706144 as a result...")
print(round(area_circle(2)) == 13)

print("Let's go to call area_square function with a side of 4. We expect 16 as a result...")
print(area_square(4) == 16)

print("Let's go to call area_triangle function with a base of 2 and height of 4 . We expect 4 as a result...")
print(area_triangle(2, 4) == 4)
