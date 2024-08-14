'''
Day 8 Challenge
Affirmations (or insults) Generator
Today's focus is using all the skills you have learned so far:

input and output
concatenation
if statements
nested if statements
Build a custom affirmations generator to give the user a customized affirmation each day of the week.

Make sure you ask the user for their name, the current day of the week, and a few of their favorite things. All of this information should be used to help you build your affirmations.
The goal is to generate a unique message for each day of the week based on the user's answers.
Use concatenation to generate the affirmation.

If affirmations are not your jam, then you could do a daily joke or insult. Please don't be mean. Keep it light and funny.

Final challenge: Can you create if statements that do not care about capital or lowercase letters of names.
'''
print ("Hello My friend, Hope you are good..! please share some information about you")
print()
name = input("Enter your name : ")
print()

if name =="Akshay" or name == "akshay":
  day =  input("Enter the day of week : ")
  if day == "Monday" or day == "monday":
    print(name,"It will be great Monday..!, and you look good BTW")
  if day == "Tuesday" or day == "tuesday":
    print(name,"it will be hectic day for you boss is angry on you")
  if day == "Wednesday" or day == "wednesday":
    print(name,"How are you, hope yesterday was not bad for you,", day, "will be good for you")
  if day == "Thursday" or day == "thursday":
    print(name,"Weekend is only 2 days away, Awesome Thursday it will be..!")
  if day == "Friday" or day == "friday":
    print(name,"Its weekend some more hours and you have those 2 loevly days..!")
  if day == "Saturday" or day == "saturday":
    print(name,"What are you doing here go get in your bed")
  if day == "Sunday" or day == "sunday":
    print(name,"Enjoy your meal and warm bed tomorrow is monday..!")
    
elif name =="Aditya" or name == "Aditya":
  day =  input("Enter the day of week : ")
  if day == "Monday" or day == "monday":
    print(name,"It will be great Monday..!")
  if day == "Tuesday" or day == "tuesday":
    print(name,"Awesome Tuesday it will be..!")
  if day == "Wednesday" or day == "wednesday":
    print(name,"Awesome Wednesday it will be..!")
  if day == "Thursday" or day == "thursday":
    print(name,"Awesome Thursday it will be..!")
  if day == "Friday" or day == "friday":
    print(name,"Awesome Friday it will be..!")
  if day == "Saturday" or day == "saturday":
    print(name,"Awesome Saturday it will be..!")
  if day == "Sunday" or day == "sunday":
    print(name,"Awesome Sunday it will be..!")

else:
  print("Sorry you name is not in the database")
  
  


