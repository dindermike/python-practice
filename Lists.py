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

# Show the First and Last elements of a list of names
print("Show the first and last names of a list of names.")

names = [name for name in input("Enter your names separated by spaces: ").split()]

print("Your List of Names =", names)
print("The First Name/Element is...", names[0])
print("The Last Name/Element is...", names[-1])

print('--------------------------------------------------')
# Number of items in a list

print("The number of items in a list.")

print("The Length of the names you entered is =", len(names))

find_name = input("Enter the name you wish to find: ")
count = 0

for name in names:
    if name == find_name:
        count += 1

print(f"The name {find_name} was found {count} times.")

print('--------------------------------------------------')
# Find all Even and Odd indexes of a list
print("Find Even and Odd Indexes and Reverse the List.")

numbered_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

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
