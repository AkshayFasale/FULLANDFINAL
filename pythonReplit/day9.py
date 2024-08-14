'''
 Day 9 Challenge
Generation Generator
What generation are you a part of?

Use this list to guide you.

Generation Name	Starting Birth Year	Ending Birth Year
Traditionalists	1925	1946
Baby Boomers	1947	1964
Generation X	1965	1981
Millenials	1982	1995
Generation Z	1996	2015
Have a user type in the year they were born.
Use their answer to tell them the generation they are a part of.
Add emojis or a fun statement to go along with the answers if you like.
'''
print("Generation Generator..!")
print()

print("Please enter your birth year to find out which generation you belong to.")
print()

year = int(input("What year were you born? = "))
print()

if year >= 1925 and year <= 1946:
  print("You are a Traditionalists")
elif year >= 1947 and year <= 1964:
  print("You are a Baby Boomers")
elif year >= 1965 and year <= 1981:
  print("You are a Generation X")
elif year >= 1982 and year <= 1995:
  print("You are a Millenials")
elif year >= 1996 and year <= 2015:
  print("You are a Generation Z")
else:
  print("You have entered wrong year..!")