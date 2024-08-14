'''
👉 Day 6 Challenge
Make your own login program.
Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting.
Write a specific personalized greeting for 3 different people.
Don't forget an else statement for everyone else who shouldn't be logging in.
'''

print("Login Page")
print()

username = input("Please enter your username : ")
password = input("Please enter your password : ")

if username == "Akshay" and password == "admin" :
  print("Welcome Akshay")
elif username == "Aditi" and password == "admin":
  print("Welcome Aditi")
elif username == "admin" and password == "admin1":
  print("Welcome Admin")
else:
  print("You are not registered user..!")