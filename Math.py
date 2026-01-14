# Various Math Functions
import math

print('--------------------------------------------------')
# Find the Greatest Common Factor 
"""
The Greatest Common Divisor (GCD), also known as the Highest Common Factor (HCF) or Greatest Common Factor (GCF), is the largest positive integer that divides two or more given integers without leaving a remainder. It's found by identifying common factors or using methods like prime factorization or Euclid's Algorithm, and is useful for simplifying fractions or dividing items into equal groups
"""
gcf_1 = math.gcd(24, 54)

print(f"A) The GCF of 24 and 54 is: {gcf_1}")

gcf_list = [12, 18, 24, 48, 54]
gcf_2 = math.gcd(*gcf_list)
gcf_nums = ', '.join(str(i) for i in gcf_list)
print(f"B) The GCF of {gcf_nums} is: {gcf_2}")

print('--------------------------------------------------')
# Area of a Circle
print("Find the Area of a Circle.")
radius = float(input("Enter the Radius of the Circle: "))

# Hand Written Exponent
area = math.pi * radius**2

# Math Function Exponent
area_2 = math.pi * math.pow(radius, 2)

print(f"The Area of a circle with a radius of {radius} equals...")
print("Hand written exponent:", round(area, 2))
print("Math function exponent:", round(area_2, 2))

print('--------------------------------------------------')
# Find the Volume of a Spere, V = 4/3 π r³

print("Find volume of a sphere.")

volume = (4/3) * math.pi * radius**3

print("The volume equals ", volume)

print('--------------------------------------------------')
# Find if a number is Even or Odd (radius input)
print('Determine if the Radius input is an Even or Odd number.')

if radius % 2 == 0:
    print("The Radius is an Even Number")
else:
    print("The Radius is an Odd Number")

print('--------------------------------------------------')
# Find the Area of a Triangle, A = 1/2 × b × h or get semi-perimeter and then area. The former, uses two inputs base and height. The latter, the semi-perimeter, uses 3 side lengths as inputs.

print("The Area of a Triange.")

num_1 = int(input("Enter the First Number: "))
num_2 = int(input("Enter the Second Number: "))
num_3 = int(input("Enter the Third Number: "))

area_triangle_1 = (num_1 * num_2) / 2

semi = (num_1 + num_2 + num_3) / 2
semi_positive = abs(semi * (semi - num_1) * (semi - num_2) * (semi - num_3))
area_triangle_2 = math.sqrt(semi_positive)

print("The Area of the Triangle, given base and height =", round(area_triangle_1, 2))
print("The Area of the Triangle, given 3 sides =", round(area_triangle_2, 2))

print('--------------------------------------------------')
# Find the sum of the positive integers of a number that is entered. E.g. 5 = (1 + 2 + 3 + 4 + 5)
# Uses a basic math formula and not an iterative loop

print('Find the sum of all positive numbers of the number you enter.')
number = int(input("Enter your number: "))

sum_total = (number * (number + 1)) / 2

print("Your sum equals ", sum_total)

print('--------------------------------------------------')
# Find the Average of X-amount of Numbers being input via the command line.

print("Find the Average of X-amount of Numbers being entered.")

total_numbers = int(input("How many numbers will there be? "))
total_sum = 0

print("You will now be asked to enter each number one at a time, to be added to the sum.")

for n in range(total_numbers):
    number = float(input("Enter the next Number: "))
    total_sum += number

average = total_sum / total_numbers

print(f"Your average of all the numbers inputted is... {total_sum} / {total_numbers} =", average)

print('--------------------------------------------------')
# Find if all or some of three input numbers are equal

print("If Three Numbers all Equal")

if num_1 == num_2 == num_3:
    print('Dinder Magic - All Numbers Are Equal to Each Other')
elif num_1 == num_2 and num_1 != num_3:
    print('Only The First and Second Numbers Match')
elif num_1 == num_3 and num_1 != num_2:
    print('Only The First and Last Numbers Match')
elif num_2 == num_3 and num_2 != num_1:
    print('Only The Second and Third Numbers Match')
elif num_1 != num_2 and num_1 != num_3:
    # Find the biggest and smallest of the three numbers entered
    print("None of the numbers match")

    nums = []

    nums.append(num_1)
    nums.append(num_2)
    nums.append(num_3)

    print(nums)

    print("The Largest Number Is:", max(nums))
    print("The Smallest Number Is:", min(nums))

    print("The sum of all numbers in the list is =", sum(nums))
else:
    # Should Never Hit
    print("Uncaught Exception")

print('--------------------------------------------------')
