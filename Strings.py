# Various String operations and functions

# Reverse a string
print("Reverse a String")
print("    * First Method")
entered_string = input("Enter the string you wish to reverse: ")
reversed_1 = "".join(reversed(entered_string))

print(f"The reverse of {entered_string} is... {reversed_1}")

print("    * Second Method")
reversed_2 = entered_string[::-1]
print(f"The reverse of {entered_string} is... {reversed_2}")

print("    * Third Method")
reversed_3 = ""
for char in entered_string:
    reversed_3 = char + reversed_3
print(f"The reverse of {entered_string} is... {reversed_3}")

print('--------------------------------------------------')
# Reverse a Number
print("Reverse a Number")

number = int(input("Enter your positive number:"))

reversed = int(str(number)[::-1])

print("The reversed number is:", reversed)
print(type(reversed))

print('--------------------------------------------------')

print("Multi-Line String 1")

print("""
      This is a Mult-Line String in a Print Statement.
      This is how you can write without having to do special stuff to a string.
      This is the third line of the statement.
""")

print('--------------------------------------------------')

print('Replace characters in a string.')

var = "This,is,my,string."
print("Original String =", var)

modified_var = var.replace(',', ' ')
print('Repaced all "," with a " " =', modified_var)
