#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Dipali Kadam
"""

# logic for the Rock Paper Scissor game in python 
# Usage: python input() function , random module, while loop, if-else ladder, print() function

import random

# print the rule of the Game
print("Winning Rules of Rock Paper Scissor game as follows: \n"
      + "Rock v/s Paper --> Paper Wins as paper covers rock \n"
      + "Rock v/s Scissor --> Rock Wins as rock smashes scissor \n"
      + "Paper v/s Scissor --> Scissor Wins as Scissor cuts paper \n")

# Taking input from user
user_choice= input("Enter the choice(rock,paper,scissor) : ")


# Computer choice shall be random 
choices = ["rock","paper","scissor"]
computer_choice = random.choice(choices)
print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

# Validate the winning conditions
# To play multiple times use while loop
while True: 
    if user_choice==computer_choice:
        print("It's a Tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("Paper cover Rock! COMPUTER WINS !")
        else:
            print("Rock Smashes Scissor! YOU WIN!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper cover Rock! YOU WIN !")
        else:
            print("Scissors cut Paper! COMPUTER WINS!")
    elif user_choice == "scissor":
        if computer_choice == "rock":
            print("Rock Smashes Scissor! COMPUTER WINS!")
        else:
            print("Scissors cut Paper! YOU WIN!")
                    
    break

