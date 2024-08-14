'''
 Day 11 Challenge
How many seconds are in a year?
Use the power of breaking a program down into its parts. We could Google this, but why not make a program for this instead.

You can multiply a bunch of numbers to figure out how many seconds are in a year.
Use input and if statements to add the extra day for leap year.
Make the computer do all the hard work and math for you. You do the thinking beforehand.
'''

year = int(input("Enter how many days are in this year?"))
daysInYear = 365
daysInLeapYear = 366
hoursInDay = 24
secondsInMinute = 60
minutesInHours = 60

result = daysInYear * hoursInDay * secondsInMinute * minutesInHours

leapYear_Result = daysInLeapYear * hoursInDay * secondsInMinute * minutesInHours

if year == 366:
  print("Number of seconds in a leap year are", leapYear_Result)
else:
  print("Number of seconds in a year are", result)