import random

from test_model import CameraInput

class RPS:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        """
           Using random module will return the choice made by the computer 
        """

        computer_choice = random.choice(self.choices)

        return computer_choice

    def get_user_choice(self):
        """
            Gets the input from the camera, the move made by the user
        """
         
        user_move = CameraInput()

        user_choice = user_move.get_prediction()

        return(user_choice)

    def get_winner(self, computer_choice, user_choice):
        """
            Determines the winner using the game logic
        """
        if user_choice==computer_choice:
            print("It's a Tie!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                self.computer_score += 1
                print("Paper cover Rock! COMPUTER WINS !")
            else:
                self.user_score +=1
                print("Rock Smashes Scissors! YOU WIN!")
        elif user_choice == "paper":
            if computer_choice == "rock":
                self.user_score +=1
                print("Paper cover Rock! YOU WIN !")
            else:
                self.computer_score += 1
                print("Scissors cut Paper! COMPUTER WINS!")
        elif user_choice == "scissors":
            if computer_choice == "rock":
                self.computer_score += 1
                print("Rock Smashes Scissor! COMPUTER WINS!")
            else:
                self.user_score +=1
                print("Scissor cut Paper! YOU WIN!")


    def game(self,rounds=3):
        """
            Run the game using the input from the camera, calling the function to get choices and determine the winner
        """

        # print the rule of the Game
        print("Winning Rules of Rock Paper Scissors game as follows: \n"
                + "Rock v/s Paper --> Paper Wins as paper covers rock \n"
                + "Rock v/s Scissors --> Rock Wins as rock smashes scissors \n"
                + "Paper v/s Scissors --> Scissor Wins as Scissors cuts paper \n")
        while True:

            computer_choice = self.get_computer_choice() 
            user_choice = self.get_user_choice()
            print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
            winner = self.get_winner(computer_choice, user_choice)
            print(f"{winner} \nUser Score: {self.user_score} \nComputer Score: {self.computer_score}")

            if self.computer_score == rounds or self.user_score == rounds:
                break

            while True:
                next = input("Press enter to play next round.")
                if next == '':
                    break

        if self.user_score > self.computer_score:
            winner = "You Win!!!"
        else:
            winner = "Computer Win!!"

        print(f"Game Over. {winner}")

        return(None)


rps_camera = RPS()
rps_camera.game()