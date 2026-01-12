# Find the Average of X-amount of Numbers being input via the command line.

total_numbers = int(input("How many numbers will there be? "))
total_sum = 0

print("You will now be asked to enter each number one at a time, to be added to the sum.")

for n in range(total_numbers):
    number = float(input("Enter the next Number: "))
    total_sum += number

average = total_sum / total_numbers

print(f"Your average of all the numbers inputted is... {total_sum} / {total_numbers} =", average)
