# Various File Operations
"""
pystatx - Requires "python3 -m pip install pystatx" and/or activating Virtual Environment First.
Command: source practice_env/bin/activate
"""
import statx
import time

from datetime import datetime
from os import listdir, path
from os.path import isfile, join

print('--------------------------------------------------')
# Show Current Filename
print("Show Current Filename and Path of Script that is running.")

print("Current Filename and Path:", path.realpath(__file__))

print('--------------------------------------------------')
# Check if a File Exists, E.g. Math.py (Files in Current Directory)
print("Does File Exist?")

check_file = input("Enter the Filename: ")

print(f"Does The File {check_file} Exist:", path.isfile(check_file))

print('--------------------------------------------------')
# List all files found in a directory, with their file extensions on a separate line.
# E.g.Directory = /home/mike Python_Practice
print("List all Files in a Directory.")
directory = input("Please enter the directory you would like to list: ")

files_list = [f for f in listdir(directory) if isfile(join(directory, f))]

for file in files_list:
    print('***********************************************')
    print("Filename:", file)

    file_extension = file.split('.')
    stx = statx.statx(file).btime
    dt_object = datetime.fromtimestamp(stx)
    formatted_date = dt_object.strftime("%a %b %d %H:%M:%S %Y")

    print('File Extension: ".' + file_extension[-1] + '"')
    print('File Last Accessed Time:', time.ctime(path.getatime(file)))
    print(f"File Created Time: {formatted_date}")
    print('File Changed Time:', time.ctime(path.getctime(file)))
    print('File Last Modified Time:', time.ctime(path.getmtime(file)))

print('--------------------------------------------------')
