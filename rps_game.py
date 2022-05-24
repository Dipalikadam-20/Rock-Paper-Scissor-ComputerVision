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
player= input("Enter the choice(rock,paper,scissor) : ")


# Computer choice shall be random 
choices = ["rock","paper","scissor"]
computer_choices = random.choice(choices)
print(f"\nYou chose {player}, computer chose {computer_choices}.\n")

# Validate the winning conditions
# To play multiple times use while loop
while True: 
    if player==computer_choices:
        print("It's a Tie!")
    elif player == "rock":
        if computer_choices == "paper":
            print("Paper cover Rock! YOU LOSE !")
        else:
            print("Rock Smashes Scissor! YOU WIN!")
    elif player == "paper":
        if computer_choices == "rock":
            print("Paper cover Rock! YOU WIN !")
        else:
            print("Scissors cut Paper! YOU LOSE!")
    elif player == "scissor":
        if computer_choices == "rock":
            print("Rock Smashes Scissor! YOU LOSE!")
        else:
            print("Scissors cut Paper! YOU WIN!")
                    
    break

