'''
2 player 🪨📄✂️
Are you ready for your first BIG project?!!

So far you have learned

input and output,
if/elif/else statements,
basic mathematics,
and casting as float and int.
WOW! That's alot in just 13 days.

Today, you are going to build a rock, paper, scissors game.

Start with this code below to ensure that whenever you use input, each player cannot see what the other player typed in 😉:

from getpass import getpass as input
For this version, you have two players. Player 1 and Player 2.
You will need to create if statements (and probably nesting) to decide who has won, lost or if the game is a tie.
Make it fun and add emojis or epic comments as your players battle it out.
Keep it simple for you. Don't expect the user to type in the words rock, paper, scissors. Instead, encourage them to use R, P, or S. (Can you ensure the user can still input an option even if it is typed in wrong?)
'''
from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

player1Move = input("Player 1 > ")
print()
player2Move = input("Player 2 > ")
print()

if player1Move=="R":
  if player2Move=="R":
    print("You both picked Rock, draw!")
  elif player2Move=="S":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
  elif player2Move=="P":
    print("Player1's Rock is smothered by Player2's Paper!")
  else:
    print("Invalid Move Player 2!")
elif player1Move=="P":
  if player2Move=="R":
    print("Player2's Rock is smothered by Player1's Paper!")
  elif player2Move=="S":
    print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
  elif player2Move=="P":
    print("Two bits of paper flap at each other. Dissapointing. Draw.")
  else:
    print("Invalid Move Player 2!")
elif player1Move=="S":
  if player2Move=="R":
    print("Player 2's Rock makes metal-dust out of Player1's Scissors")
  elif player2Move=="S":
    print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
  elif player2Move=="P":
    print("Player1's Scissors make confetti out of Player2's paper!")
  else:
    print("Invalid Move Player 2!")
else:
  print("Invalid Move Player 1!")