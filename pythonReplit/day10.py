'''
Day 10 Challenge
Extend your bill calculator
Add a tip function that adds the total tip to the bill before splitting it equally between the people.

Ask the user for the total bill amount.
Ask what % of tip they will leave to be added to the bill total.
Figure out how to get the total bill with tip then add that to original amount.
Ask the user how many people are splitting the bill and divide by the total.
You can use the same code to get started:

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)
'''
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))

answer = myBill / numberOfPeople
answer =  round(answer, 2)

print("Total bill is", myBill)
print()
print("You owe", answer)
print()
tip = int(input("What percentage of tip would you like to give? "))
tip = (tip/100) * myBill
totalbill = myBill + tip
print()
print("total bill is now ", totalbill)

finalBillperHead = totalbill / numberOfPeople
finalBillperHead = round(finalBillperHead, 2)
print()
print("You all owe per head", finalBillperHead)

'''
Better code 
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent? "))


bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)


print("You all owe", final_amount)
'''