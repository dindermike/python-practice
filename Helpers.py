# Various Helper Functions
import copy
import math
import struct

from subprocess import call

print("Print Doc String of Built-in Function...")
print("Docstring of math.pi() ...")
print(math.pi.__class__)
print(math.pi.__doc__)

print('--------------------------------------------------')

print("Docstring of math.pow() ...")
print(math.pow.__class__)
print(math.pow.__doc__)

print('--------------------------------------------------')

print("Docstring of reversed() ...")
print(reversed.__class__)
print(reversed.__doc__)

print('--------------------------------------------------')

print("Docstring of abs() ...")
print(abs.__class__)
print(abs.__doc__)

print('--------------------------------------------------')

print("Docstring of set.difference() ...")
print(set.difference.__class__)
print(set.difference.__doc__)

print('--------------------------------------------------')

print("Docstring of copy.copy() ...")
print(copy.copy.__class__)
print(copy.copy.__doc__)

print('--------------------------------------------------')

print("Docstring of list.remove() ...")
print(list.remove.__class__)
print(list.remove.__doc__)

print('--------------------------------------------------')

print("Docstring of list.pop() ...")
print(list.pop.__class__)
print(list.pop.__doc__)

print('--------------------------------------------------')
# Is Python Version 32bit or 64bit?
"""
The struct.calcsize("P") function returns the size of a C pointer in bytes, which is 4 on a 32-bit system and 8 on a 64-bit system. Multiplying by 8 converts this to bits where 32 = 32-bit and 64 = 64-bit
"""
print("Is Python Version 32-bit or 64-bit Architecture?")

if struct.calcsize("P") * 8 == 64:
    print("You Are Using: 64-bit Python")
elif struct.calcsize("P") * 8 == 32:
    print("You Are Using: 32-bit Python")
else:
    print("Your Python is of Unknown Architecture")

print('--------------------------------------------------')
# Execute an External Python Command
print("Execute an External Python Command")

call(['dir'])
call(['ls', '-li'])

print('\n\n\n----- Now Executing Variables.py Script -----\n\n\n')
call(['python3', 'Variables.py'])

print('--------------------------------------------------')