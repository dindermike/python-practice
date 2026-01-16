# Access and get system variables, including the current username of the user logged into the operating system (Ubuntu etc...) (two different ways to get username)
import getpass
import os
import platform
import pprint
import sys

print("The current Username is... ", getpass.getuser())

print('--------------------------------------------------')
# Get Environment Variables
print("Various Local Environment Variables...")

print(os.environ['HOME'])
print(os.environ['USER'])
print(os.environ['LANG'])
print(os.environ['NAME'])
print(os.environ['SHELL'])

print('--------------------------------------------------')
# Get the current version of Python
print("Current Version of Python and OS Info is...")

print(sys.version)
print(sys.version_info)
print(os.name)
print(platform.system())
print(platform.release())

print('--------------------------------------------------')
# Get the current version of Ubuntu
print("Ubuntu Information...")

# Get all the OS release data
os_release_info = platform.freedesktop_os_release()

ubuntu_version = os_release_info.get("VERSION")
ubuntu_codename = os_release_info.get("VERSION_CODENAME")
pretty_name = os_release_info.get("PRETTY_NAME")

print(f"Pretty Name: {pretty_name}")
print(f"Ubuntu Version: {ubuntu_version}")
print(f"Codename: {ubuntu_codename.title()}")

print('--------------------------------------------------')

print("The list of all Variables is...")
for key, value in os.environ.items():
    print(f"{key}: {value}")