import os
import random

#raw_input in newer python versions
inp = input("hi: ")
if inp=="hi":
    print("hallo")

# sequence: 
# - player one enters a number, between 1 and 1000
# - number should not be visible anymore
# repeat: 
# - player two enters a number
# - numbers are compared to each other
#   - if player two's number is higher, output to high
#   - if player two's number is lower, output to low
#   - if player two's number is equal, output succcess
# variables of player numbers: player_one, player_two


player_one = int(input("Player one, please enter a number between 1 and 1000: "))

if player_one < 1 or player_one > 1000:
    print("Nö du mieser Schummler! Verloren!!!!! Ätschibätsch!")
    exit()
# Hide the number from player two

os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
print("Player one has entered a number. Player two, please guess the number.")
player_two = None
while player_two != player_one:
    player_two = int(input("Player two, please enter your guess: "))
    if player_two > player_one:
        print("Too high!")
    elif player_two < player_one:
        print("Too low!")
    else:
        print("Success! You guessed the number.")                           
# The code above is a simple number guessing game where player one enters a number and player two tries to guess it.
# The game provides feedback on whether the guess is too high or too low until the correct number is guessed.   