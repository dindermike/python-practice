# Various Math Functions
import math

# Area of a Circle
print("Find the Area of a Circle.")
radius = float(input("Enter the Radius of the Circle: "))

# Hand Written Exponent
area = math.pi * radius**2

# Math Function Exponent
area_2 = math.pi * math.pow(radius, 2)

print(f"The Area of a circle with a radius of {radius} equals...")
print("Hand written exponent:", area)
print("Math function exponent:", area_2)

print('--------------------------------------------------')

# Find the sum of the positive integers of a number that is entered. E.g. 5 = (1 + 2 + 3 + 4 + 5)
# Uses a basic math formula and not an iterative loop

print('Find the sum of all positive numbers of the number you enter.')
number = int(input("Enter your number: "))

sum = (number * (number + 1)) / 2

print("Your sum equals ", sum)

print('--------------------------------------------------')

# Find the Average of X-amount of Numbers being input via the command line.
print("Find the Avera of X-amount of Numbers being entered.")

total_numbers = int(input("How many numbers will there be? "))
total_sum = 0

print("You will now be asked to enter each number one at a time, to be added to the sum.")

for n in range(total_numbers):
    number = float(input("Enter the next Number: "))
    total_sum += number

average = total_sum / total_numbers

print(f"Your average of all the numbers inputted is... {total_sum} / {total_numbers} =", average)

print('--------------------------------------------------')
