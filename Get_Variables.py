# Access and get system variables, including the current username of the user logged into the operating system (Ubuntu etc...) (two different ways to get username)
import getpass
import os

print("The current Username is... ", getpass.getuser())

print('--------------------------------------------------')

print(os.environ['HOME'])
print(os.environ['USER'])
print(os.environ['LANG'])
print(os.environ['NAME'])
print(os.environ['SHELL'])

print('--------------------------------------------------')

print("The list of all Variables is...")
for key, value in os.environ.items():
    print(f"{key}: {value}")