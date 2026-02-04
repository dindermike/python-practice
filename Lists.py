# List and Tuple operations
import copy


# Enter numbers and split into a list and a tuple.
print("Enter a series of numbers. Your output will be a list and a separate tuple of numbers.")
numbers = [int(num) for num in input("Enter numbers separated by spaces: ").split()]
tupled = tuple(numbers)

print("List:", numbers)
print(type(numbers))
for x in numbers:
    print(type(x))

print("Tuple:", tupled)
print(type(tupled))
for x in tupled:
    print(type(x))

print('--------------------------------------------------')
# Create a Histogram using the list of numbers above.
print("Show a Histogram of the List of Numbers you Entered.")


def histogram(list_of_numbers) -> None:
    """
    Histogram: a chart that visually displays the distribution of continuous numerical data, grouping it into "bins" or
    ranges, with the height of each bar showing the frequency (how many data points) within that range. This function
    will represent this in text format using asterisks "*", where each line is each element in the list.

    :param list_of_numbers: List of Numbers Entered Via Input
    :returns: Nothing
    :rtype: None
    """
    for interval in list_of_numbers:
        output = ''

        while (interval > 0):
            output += '*'
            interval -= 1

        print(output)


histogram(numbers)

print('--------------------------------------------------')
# Find all the Even Numbers found in the list. By Value and not by index.
print("Show Even numbers by value of the list of numbers.")

for x in numbers:
    if x > 100:
        print("XXX - This Number Exceeds This Threshold! - XXX")
    elif x % 2 == 0:
        print("    (" + str(x) + ")")
    else:
        print("X")

print('--------------------------------------------------')

# Show the First and Last elements of a list of names
print("Show the first and last names of a list of names.")

names = [name for name in input("Enter your names separated by spaces: ").split()]

print("Your List of Names =", names)
print("The First Name/Element is...", names[0])
print("The Last Name/Element is...", names[-1])

print('--------------------------------------------------')
# List to String
print("List to String.")

stringed_list_1 = ' '.join(names)
stringed_list_2 = ', '.join(names)
stringed_list_3 = ' - '.join(names)
stringed_list_4 = ' : '.join(names)

print("Example 1:", stringed_list_1)
print("Example 2:", stringed_list_2)
print("Example 3:", stringed_list_3)
print("Example 4:", stringed_list_4)

print('--------------------------------------------------')
# Number of items in a list, how many times does this name appear in the list?
print("The number of items in a list.")

print("The Length of the names you entered is =", len(names))

find_name = input("Enter the name you wish to find: ")
count = 0
found = False

this_count = names.count(find_name)
print(f"A) The name {find_name} was found {this_count} times.")

# Via For Loop: Slower Memory Performacne
for name in names:
    if name == find_name:
        count += 1

print(f"B) The name {find_name} was found {count} times.")

print('--------------------------------------------------')
# Alternative, check if element is in the list
print("Check if the Name you Entered is in the List")

if find_name in names:
    print(f'A) The Name "{find_name}" is in the list of names you created.')
else:
    print(f'A) The Name "{find_name}" is NOT in the list of names you created.')

# Via a For Loop: Slower Memory Performance
for name in names:
    if name == find_name:
        found = True

if found:
    print(f'B) The Name "{find_name}" is in the list of names you created.')
else:
    print(f'B) The Name "{find_name}" is NOT in the list of names you created.')

print('--------------------------------------------------')
# Find all Even and Odd indexes of a list
print("Find Even and Odd Indexes and Reverse the List.")

numbered_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Copying for Independent Operations Further Down in this File
numbered_list_1 = copy.copy(numbered_list)
numbered_list_2 = copy.copy(numbered_list)
numbered_list_3 = copy.copy(numbered_list)
numbered_list_4 = copy.copy(numbered_list)

even_indexes = numbered_list[::2]
odd_indexes = numbered_list[1::2]

print("Your Standard List Is:", numbered_list)
print("Your Even Indexes Are:", even_indexes)
print("Your Odd Indexes Are:", odd_indexes)
print("Your Reversed List Is:", numbered_list[::-1])

print('--------------------------------------------------')
# Using a Slice Object
print("Slice Objects.")

special_slice = slice(3, 12, 2)

print("Your Slice Is:", special_slice)
print("Your Sliced List Is:", numbered_list[special_slice])
print("Your Reversed Sliced List Is:", numbered_list[::-1][special_slice])

print('--------------------------------------------------')
# Adding and Removing items from a List
print("Adding and Removing Items in a List")

print("Un-Altered")
print(numbered_list_1)
print(numbered_list_2)
print(numbered_list_3)
print(numbered_list_4)

print("Removing Index 5 by Index:", numbered_list_1.pop(5))
print(numbered_list_1)

print("Removing Index 5 by Value:", numbered_list_2.remove(7))
print(numbered_list_2)

print("Removing First Element")
del numbered_list_3[0]
print(numbered_list_3)

print("Removing Last Element")
del numbered_list_4[-1]
print(numbered_list_4)

print('--------------------------------------------------')
