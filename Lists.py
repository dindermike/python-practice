# List and Tuple operations

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
