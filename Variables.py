# Access and get system variables, including the current username of the user logged into the operating system (Ubuntu
# etc...) (two different ways to get username)
import getpass
import multiprocessing
import os
import platform
import site
import socket
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
# Get the current version of Python and OS information
print("Current Version of Python and OS Info is...")

print(sys.version)
print(sys.version_info)
print(os.name)
print(platform.system())
print(platform.release())
print(site.getsitepackages())
print(site.getusersitepackages())

print("Number of CPU's Is:", multiprocessing.cpu_count())

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
# Get the current Hostname of your system (A.k.a. The Computer Name)
# mikedinder.com = 15.197.225.128
print("System Hostname...")

ip_address = '15.197.225.128'
host_name = socket.gethostname()
host_by_name = socket.gethostbyname(host_name)
host_by_addr = socket.gethostbyaddr(ip_address)
addr_info = socket.getaddrinfo(ip_address, 80)

print('Host Name:', host_name)
print('Host By Name:', host_by_name)
print('Host By Address:', host_by_addr)
print('Address Info:', addr_info)

print('--------------------------------------------------')

print("The list of all Variables is...")
for key, value in os.environ.items():
    print(f"{key}: {value}")
