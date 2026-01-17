# Various Collections and/or Sets Operations
from collections import Counter

print("Comparing Lists/Sets")

numbered_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
comparing_list = [3, 9, 12, 15, 20, 25, 33, 56, 99, 100]

print("Your Standard List Is:", numbered_list)
print("Your Comparable List Is:", comparing_list)

set_list_1 = set(numbered_list)
set_list_2 = set(comparing_list)
print("A) The Difference in the Two Lists is:", set_list_1.difference(set_list_2))
print("B) The Difference in the Two Lists is:", set_list_2.difference(set_list_1))

print('--------------------------------------------------')
# Counter function of collections library
print("Using collections.Counter() function.")

fruit = Counter(['Apple', 'Pineapple', 'Peach', 'Apple', 'Peach', 'Blueberry', 'Grape', 'Orange', 'Apple', 'Banana'])
animals = Counter({'Dogs': 12, 'Cats': 3, 'Cows': 44, 'Horses': 25, 'Pigs': 8, 'Chickens': 87, 'Ducks': 1})

print('Fruit Counter:', fruit)
print('Most Common Fruit:', fruit.most_common())
print(f'Access Element in Fruit, Pineapple = {fruit['Peach']}')
print('Animals Counter:', animals)
print('Most Common Animals:', animals.most_common())
print(f'Access Element in Animals, Dogs = {animals['Dogs']}')
