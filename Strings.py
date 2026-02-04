# Various String operations and functions

# Reverse a string
print('Reverse a String')
print('    * First Method')
entered_string = input('Enter the string you wish to reverse: ')
reversed_1 = ''.join(reversed(entered_string))

print(f'The reverse of {entered_string} is... {reversed_1}')

print('    * Second Method')
reversed_2 = entered_string[::-1]
print(f'The reverse of {entered_string} is... {reversed_2}')

print('    * Third Method')
reversed_3 = ''
for char in entered_string:
    reversed_3 = char + reversed_3
print(f'The reverse of {entered_string} is... {reversed_3}')

print('The Length of Your String is:', len(entered_string))

print('--------------------------------------------------')
# Reverse a Number
print('Reverse a Number')

number = int(input('Enter your positive number:'))

reversed = int(str(number)[::-1])

print('The reversed number is:', reversed)
print(type(reversed))

print('--------------------------------------------------')
# Line Breaks in Strings and Removing Line Breaks
print('String Line Breaks')

var1 = '\nHello World\n\nHello Dinder\n'
var2 = var1.rstrip()
var3 = var1.lstrip()
var4 = var1.strip()
var5 = var1.replace('\n', '')

print(var1)
print('*****')
print(var2)
print('*****')
print(var3)
print('*****')
print(var4)
print('*****')
print(var5)
print('*****')

print('--------------------------------------------------')
# Convert a String to a List
print('String to List')

this_string = str(input('Enter a Random Sentence: '))

print('Your List is...')
print(this_string.split(' '))

print('--------------------------------------------------')

print('Multi-Line String 1')

print("""
      This is a Mult-Line String in a Print Statement.
      This is how you can write without having to do special stuff to a string.
      This is the third line of the statement.
""")

print('--------------------------------------------------')

print('Replace characters in a string.')

var = 'This,is,my,string.'
print('Original String =', var)

modified_var = var.replace(',', ' ')
print('Repaced all "," with a " " =', modified_var)

print('--------------------------------------------------')

print('Add Leading Characters to a String')

str1 = 'Hello'
str2 = 'Hello Wo'
str3 = 'Hello World'
str4 = 'Hello Dinder World'

print(str1)
print(str2)
print(str3)
print(str4)

str1_new = str1.ljust(18, '.')
str2_new = str2.ljust(18, '.')
str3_new = str3.ljust(18, '.')
str4_new = str4.ljust(18, '.')

print(str1_new)
print(str2_new)
print(str3_new)
print(str4_new)

str1_new = str1.ljust(18, '_')
str2_new = str2.ljust(18, '_')
str3_new = str3.ljust(18, '_')
str4_new = str4.ljust(18, '_')

print(str1_new)
print(str2_new)
print(str3_new)
print(str4_new)

str1_new = str1.ljust(18, '*')
str2_new = str2.ljust(18, '*')
str3_new = str3.ljust(18, '*')
str4_new = str4.ljust(18, '*')

print(str1_new)
print(str2_new)
print(str3_new)
print(str4_new)
