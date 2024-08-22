import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

title = "Rock 🪨, Paper 📄, Scissors ✂️".upper()
choice = "Choose a number and enter below".title()
choice0 = "1) for Rock 🪨"
choice1 = "2) for Paper 📄"
choice2 = "3) for Scissors ✂️"


print("-" * 50)
print(title.center(50, "-"))
print("-" * 50)
print("")
print(choice.center(50, "-"))
print("")
print(choice0)
print(choice1)
print(choice2)
print("")
print("-" * 50)
playerchoice = input("\n:> ")
print("")

player = int(playerchoice)




# Error handling (simple)
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("*" * 50)
print("")
print("You chose: " + str(RPS(player)).replace("RPS.", "") + ".")
print("")
print("I chose: " + str(RPS(computer)).replace("RPS.", "") + ".")  
print("")

if player == 1 and computer == 3:
    print("🥳 You win! 🎉".center(50, "-"))
elif player == 2 and computer == 1:
    print("🥳 You win! 🎉".center(50, "-"))
elif player == 3 and computer == 2:
    print("🥳 You win! 🎉".center(50, "-"))
elif player == computer:
    print("😲 Tie game! 🤪".center(50, "-"))
else:
    print("😎 I win! 😎".center(50, "-"))

print("")   

    
    
