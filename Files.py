# Various File Operations
from os import listdir, path
from os.path import isfile, join

print('--------------------------------------------------')
# Check if a File Exists
print("Show Current Filename and Path of Script that is running.")

print("Current Filename and Path:", path.realpath(__file__))

print('--------------------------------------------------')
# Check if a File Exists
print("Does File Exist?")

check_file = input("Enter the Filename: ")

print(f"Does The File {check_file} Exist:", path.isfile(check_file))

print('--------------------------------------------------')
# List all files found in a directory, with their file extensions on a separate line. E.g. Directory = /home/mike/Python_Practice
print("List all Files in a Directory.")
directory = input("Please enter the directory you would like to list: ")

files_list = [f for f in listdir(directory) if isfile(join(directory, f))]

for file in files_list:
    print("Filename =", file)

    file_extension = file.split('.')

    print('File Extension = ".' + file_extension[-1] + '"')

print('--------------------------------------------------')
