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