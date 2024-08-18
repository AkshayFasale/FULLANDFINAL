'''

'''
print("Grade Generator")
print()

testName = input("Please enter Test name ")
maxScore = int(input("What is the maximum score you can receive? "))
yourScore = int(input("How many points did you receive?"))

number_score = float(yourScore / maxScore)
final_number = round(number_score,2)
percentage = round(yourScore / maxScore * 100, 2)

if final_number >= 90:
  print("You got", final_number, "% which is an A+ grade..!")
elif final_number >= 80 and final_number <= 89:
  print("You got", final_number, "% which is an A grade..!")
elif final_number >= 70 and final_number <= 79:
  print("You got", final_number, "% which is an B grade..!")
elif final_number >= 60 and final_number <= 69:
  print("You got", final_number, "% which is an C grade..!")
elif final_number >= 50 and final_number <= 59:
  print("You got", final_number, "% which is an D grade..!")
else:
  print("You got under 50% which is an U grade..!")
  

        