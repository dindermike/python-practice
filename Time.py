# Various Time/Date operations and functions
import calendar
import datetime

# Get the current Date and Time
now = datetime.datetime.now()

print("The Current Date and Time is...")
print(now.strftime("%B %A %m/%d/%y %I:%M%p")) # Outputs as January Monday 01/12/26 03:55PM

print('--------------------------------------------------')

print("Show a calendar for a given month and year.")

year = int(input("Enter the Year in YYYY format: "))
month = int(input("Enter the Month in MM numeric format: "))

print(calendar.month(year, month))

print('--------------------------------------------------')

print('Shows the Full Year')
print(calendar.calendar(year))

print('--------------------------------------------------')

print("Number of days between two dates.")

date_1 = input("Please enter the start date in mm/dd/yyyy format: ")
date_2 = input("Please enter the end date in mm/dd/yyyy format: ")
format_pattern = "%m/%d/%Y"

start_object = datetime.datetime.strptime(date_1, format_pattern)
end_object = datetime.datetime.strptime(date_2, format_pattern)

if start_object > end_object:
    delta = start_object - end_object
elif start_object < end_object:
    delta = end_object - start_object
else:
    delta = 0

print("The number of days between the two dates is...")
print(delta)