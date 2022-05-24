import random

class RPS:
    def __init__(self):
        self.choices = ['rock','paper','scissors']

    def get_computer_choice(self):
        """
            using random module to get computer choices from the list
        """
        computer_choice = random.choice(self.choices)

        return computer_choice


    def get_user_choice(self):
        # get input from user

        while True:
            user_choice = input("Enter the choice(rock,paper,scissors): ")
            user_choice = user_choice.lower()

            if user_choice in self.choices:
                return user_choice

    def get_winner(self,computer_choice, user_choice):
        """
            Determines the winner by defining the game rule
        """
        if user_choice==computer_choice:
            print("It's a Tie!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Paper cover Rock! COMPUTER WINS !")
            else:
                print("Rock Smashes Scissors! YOU WIN!")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper cover Rock! YOU WIN !")
            else:
                print("Scissors cut Paper! COMPUTER WINS!")
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Rock Smashes Scissor! COMPUTER WINS!")
            else:
                print("Scissor cut Paper! YOU WIN!")


    def game(self):
        """
            Run the game using the input from the user and determine the winner
        """

        # print the rule of the Game
        print("Winning Rules of Rock Paper Scissors game as follows: \n"
                + "Rock v/s Paper --> Paper Wins as paper covers rock \n"
                + "Rock v/s Scissors --> Rock Wins as rock smashes scissors \n"
                + "Paper v/s Scissors --> Scissor Wins as Scissors cuts paper \n")

        computer_choice = self.get_computer_choice() 
        user_choice = self.get_user_choice()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        winner = self.get_winner(computer_choice, user_choice)
        return(winner)

rps_manual =  RPS()
rps_manual.game()
