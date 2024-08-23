import sys 
import random


#set the range 
min_value = 1
max_value = 2

#assign a var to the the random number as random chooses between the set range
computerchoice = random.randint(min_value, max_value)


print("Guess a number between 1 and 2:")
#assign the input as a variable
guess = input(":> ")
#pass that var as an integer and assign a new var
playerchoice = int(guess)

# Use the set vars in conditonal logic to determine if the guess is less than greater than or equal to 
# the random number
if playerchoice > computerchoice:
    print(f"I had {computerchoice} which is lower than {playerchoice} sorry! 😎")
elif playerchoice < computerchoice:
    print(f"I had {computerchoice} which is higher than {playerchoice} sorry! 😎")
else:
    playerchoice == computerchoice
    print(f"{playerchoice} is Correct!🎉")
    

    
    
    