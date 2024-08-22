import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

while True:  # Start an infinite loop for the game
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

    # Convert the player's choice from string to integer
    player = int(playerchoice)

    # Error handling to ensure the player enters a valid number (1, 2, or 3)
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    # Randomly select a choice for the computer (as a string)
    computerchoice = random.choice("123")

    # Convert the computer's choice from string to integer
    computer = int(computerchoice)

    print("*" * 50)
    print("")
    print("You chose: " + str(RPS(player)).replace("RPS.", "") + ".")
    print("")
    print("I chose: " + str(RPS(computer)).replace("RPS.", "") + ".")  
    print("")

    # Determine the winner based on the rules of Rock, Paper, Scissors
    if player == 1 and computer == 3:
        print("🥳 You win! 🎉".center(50, "-"))
    elif player == 2 and computer == 1:
        print("🥳 You win! 🎉".center(50, "-"))
    elif player == 3 and computer == 2:
        print("🥳 You win! 🎉".center(50, "-"))
    elif player == computer:
        print("😲 Tie game! 🤪".center(50, "-"))
    else:
        # If none of the above conditions are met, the computer wins
        print("😎 I win! 😎".center(50, "-"))

    print("")  # Print an empty line for better readability

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    # If the player types anything other than "yes", exit the loop
    if play_again != "yes":
        print("Thanks for playing!")
        break  # Exit the loop, ending the game
