'''
👉 Day 5 Challenge
"Which character are you?" Generator
You will need to:

Ask your users a series of questions that identify if they're one of the characters in the world you have created.
Add multiple if statements to check the result of each question.
Make sure to have a final print if they haven't selected any of the characters so far.
Example
Marvel Movie Character Creator
--

Example>
Do you like 'hanging around'?: No
Then you're not Spider-man
Do you have a 'gravelly' voice?: No
Aww, then you're not Korg
Do you often feel 'Marvelous'?: Yes
Aha! You're Captain Marvel! Hi!


'''
print("Which character are you from 'Avengers?'")
print()
print("Answer these questions and let's find out.")
print()
print("Please use Y or N for yes and no.")
print()

spiderman =  input("Do you like 'hanging around'? : ")
if spiderman == "yes":
  print("You are spiderman..!")
else:
  print("No Then you're not Spider-man")

voice = input("Do you have a 'gravelly' voice? : ")
if voice == "yes":
  print("You are a Korg")
else:
  print("Aww, then you are not Korg")

marvel = input("Do you oftern feel 'Marvelous'? : ")
if marvel== "yes":
  print("Aha! You are Captain Marvel! Hi!")
else:
  print("You are not captain marvel..!")
  