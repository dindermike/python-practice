# List all files in a specific directory.
from os import listdir
from os.path import isfile, join

# E.g. /home/mike/Python_Practice
print("List all Files in a Directory.")
directory = input("Please enter the directory you would like to list: ")

files_list = [f for f in listdir(directory) if isfile(join(directory, f))]

for file in files_list:
    print("Filename =", file)

    file_extension = file.split('.')

    print('File Extension = ".' + file_extension[-1] + '"')

print('--------------------------------------------------')