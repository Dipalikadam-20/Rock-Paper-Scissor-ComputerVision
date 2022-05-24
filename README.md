# Rock-Paper-Scissor-ComputerVision


**AiCore Rock-Paper-Scissor-ComputerVision project -**

  1. Implementation of rock-paper-scissor game using manual input from user using **basic python**:
  
     a. Python | random | input() function | list data structure | Control flow
     
     b. To play the game with computer with manual user input, run **rps_game_basic.py**
     
  2. Implementation of rock-paper-scissor game using manual input from user using **Advanced python**:
  
     a. Python | random | functions| Classes | list data structure | Control flow
     
     b. To play the game with computer with manual user input, run **RPS_game.py**
     
   3. Implementation of rock-paper-scissor game using webcam as input and **Computer Vision**.
   
      a. Python |OpenCv | Keras | Numpy | random |
      
      b. Model trained on teachable machines building own dataset
      
      c. To play full game with camera, run **rps_play.py**
   
  

**Mileston1: Create the model **
1.	Go to https://teachablemachine.withgoogle.com to start creating the model. Each class is trained with images of yourself showing options to camera.
An image model of 4 classes(Rock,Paper,Scissor,Nothing) was created using webcam inputs.

2.	The model was downloaded and saved to the repository. The text file containing the labels as labels.txt


**Milestone 2: Install the dependencies**

Create new virtual environment and install the below requirements
 **Requirements**
    •	Python 3
    •	Keras
    •	Tensorflow
    •	OpenCV

conda create -n my_env_name python=3.9

conda activate my_env_name

conda install pip

Install the requirements:

conda install -c conda-forge opencv

pip install ipykernel


**Milestone 3: Create a Rock-Paper-Scissor game**

1.	Store user’s input and computer’s choices
2.	Determine the winner by applying the rock-paper-scissor game logic
3.	Usage of python function to determine the winner 
4.	Usage of python random module to decide computer’s choices

**Milestone 4: Using camera to play rock-paper-scissor**

1.	Use camera to get the input from the user and get the predictions of the model
2.	Add countdown to zero 
3.	Add the number of rounds to the game to decide the Winner with the update in the score.


