'''days_in_month.py
The purpose of exercise is to create a similar script to that of the cattreats -script.
The user can define what month he/ she is interested in and find out how many days
there is in that particular month. 
Limitations:

Usage: ./days_in_month.py
Mira Kajo - 20.12.2016
'''

# create two lists: one having the months as values, and the other the number of days in each month:
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
daysMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# set a SelectedMonth variable where the user can define which month they want to check out: 
SelectedMonth = months[4]

# assign the choosen months index to another variable:

MonthIndex = months.index(SelectedMonth)

# print out the MonthIndex to check out it worked:
print(MonthIndex)

# print out a sentence telling the month the user chose and how many days is in that month:
print("The number of days in", SelectedMonth, "is ", daysMonth[MonthIndex])