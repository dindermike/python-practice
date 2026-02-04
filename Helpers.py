# Various Helper Functions
import copy
import math
import socket
import struct
import sys
import textwrap

from inspect import getmodule
from subprocess import call


print('Print Doc String of Built-in Function...')
print('Docstring of math.pi() ...')
print(math.pi.__class__)
print(math.pi.__doc__)
print(getmodule(math.pi))

print('--------------------------------------------------')

print('Docstring of math.pow() ...')
print(math.pow.__class__)
print(math.pow.__doc__)
print(getmodule(math.pow))

print('--------------------------------------------------')

print('Docstring of reversed() ...')
print(reversed.__class__)
print(reversed.__doc__)
print(getmodule(reversed))

print('--------------------------------------------------')

print('Docstring of abs() ...')
print(abs.__class__)
print(abs.__doc__)
print(getmodule(abs))

print('--------------------------------------------------')

print('Docstring of set.difference() ...')
print(set.difference.__class__)
print(set.difference.__doc__)
print(getmodule(set.difference))

print('--------------------------------------------------')

print('Docstring of copy.copy() ...')
print(copy.copy.__class__)
print(copy.copy.__doc__)
print(getmodule(copy.copy))

print('--------------------------------------------------')

print('Docstring of list.remove() ...')
print(list.remove.__class__)
print(list.remove.__doc__)
print(getmodule(list.remove))

print('--------------------------------------------------')

print('Docstring of list.pop() ...')
print(list.pop.__class__)
print(list.pop.__doc__)
print(getmodule(list.pop))

print('--------------------------------------------------')

print('Docstring of sys.stderr() ...')
print(sys.stderr.__class__)
print(sys.stderr.__doc__)
print(getmodule(sys.stderr))

print('--------------------------------------------------')
# Is Python Version 32bit or 64bit?
"""
The struct.calcsize('P') function returns the size of a C pointer in bytes, which is 4 on a 32-bit system and 8 on a
64-bit system. Multiplying by 8 converts this to bits where 32 = 32-bit and 64 = 64-bit
"""
print('Is Python Version 32-bit or 64-bit Architecture?')

if struct.calcsize('P') * 8 == 64:
    print('You Are Using: 64-bit Python')
elif struct.calcsize('P') * 8 == 32:
    print('You Are Using: 32-bit Python')
else:
    print('Your Python is of Unknown Architecture')

print('--------------------------------------------------')
# Standard Error Message (Command Line)
print('Output a Standard Error via Command Line Interface')

print('ERROR A: Something went wrong.', file=sys.stderr)
sys.stderr.write('ERROR A: Another way to write to stderr.\n')
sys.stderr.flush()

# Write to Log File
sys.stderr = open('standard_error_log.txt', 'a', buffering=1)
print('ERROR B: Something went wrong.', file=sys.stderr)
sys.stderr.write('ERROR B: Another way to write to stderr.\n')
sys.stderr.flush()

print('--------------------------------------------------')
# Get ASCII Character Codes
print('Get ASCII Character Codes')

print(ord('D'))
print(ord('I'))
print(ord('N'))
print(ord('D'))
print(ord('E'))
print(ord('R'))
print(ord('!'))
print(ord('@'))
print(ord('#'))
print(ord('$'))
print(ord('%'))
print(ord('€'))

print('--------------------------------------------------')
# List of Built-In Modules
print('Built-In Modules')

modules = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(modules, width=100))

print('--------------------------------------------------')
# Execute an External Python Command
print('Execute an External Python Command')

call(['dir'])
call(['ls', '-li'])

print('\n\n\n----- Now Executing Variables.py Script -----\n\n\n')
call(['python3', 'Variables.py'])

print('--------------------------------------------------')
# Show System Copyright Information
print('Get System Copyright')

print(sys.copyright)

print('--------------------------------------------------')
# Show the size of a variable or object in Bytes
print('Get Size of a Variable in Bytes')

var1 = 'Hello'
var2 = 'Hello World'
var3 = 'Hello Dinder World'

print(f'The memory size of {var1} is:', str(sys.getsizeof(var1)))
print(f'The memory size of {var2} is:', str(sys.getsizeof(var2)))
print(f'The memory size of {var3} is:', str(sys.getsizeof(var3)))
print('The memory size of sys.copyright is:', str(sys.getsizeof(sys.copyright)))

print('--------------------------------------------------')
# Show the Identity of an Object, a Memory Address
print('Get the Identity of an Object')

print(id(var1))
print(id(var2))
print(id(var3))
print(id(sys.copyright))

print('--------------------------------------------------')
# Validate an IP Address
print('Validate an IP Address')


def is_valid_ip(address=None) -> bool:
    """
    Check if a String is a Valid IP Address.

    :param address: String, IP Address to Check.
    :returns: True/False.
    :rtype: boolean
    """
    value = False

    try:
        socket.inet_aton(address)
    except socket.error:
        print(f'The IP Address "{address}" is NOT Valid!')
    else:
        print(f'The IP Address "{address}" IS Valid!')
        value = True

    return value


is_valid_ip('127.0.0.2561')
is_valid_ip('127.0.0.256')
is_valid_ip('127.0.0.25')
is_valid_ip('8.8.8.8')

print('--------------------------------------------------')
