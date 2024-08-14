
'''
Fake Fan Question Generator
Wanna find out if someone else is a true superfan of the same show, movie or interest as you? Create a program that asks what someone is interested in and includes nested if statements to ask annoying follow-up questions to see if someone is the real deal!

Make sure you include multiple if/elif statements and nested if statements too!
'''


superfan = input("Are you a super fan of the Marvel?")
if superfan == "yes":
  print("Lets see what you likes and dislikes..!")
  print()
  print("Answer the questions and lets find out")
  print()
  print("Please use Y or N for yes and no")
  print()
  ironman = input("Do you like ironman?")
  if ironman == "Y":
    print("Thats great choise")
    tobi = input("Do you know tobi?")
    if tobi == "Y":
      print ("No you are not iron man FAN")
    else:
      print ("aah so u are aware of ironman very well..!")
  hulk = input("Do you like hulk?")
  if hulk == "Y":
    print("Thats great choise but i dont like hulk")
    green = input("Do you know what color us hulk having?")
    if green == "Y":
      print (" Tell me what is it?")
    else:
      print ("Good good u know it")
else:
  print("Ok no issue you are not superfan so go to hell..!")
      