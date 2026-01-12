# Find the sum of the positive integers of a number that is entered. E.g. 5 = (1 + 2 + 3 + 4 + 5)
# Uses a basic math formula and not an iterative loop

number = int(input("Enter your number: "))

sum = (number * (number + 1)) / 2

print("Your sum equals ", sum)