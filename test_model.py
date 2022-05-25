
import cv2
from keras.models import load_model
import numpy as np
import time


class CameraInput:
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype = np.float32)
        self.choices = ['rock', 'paper', 'scissors', 'nothing']

    def get_user_input(self,prediction):
        """
            Gives the predicted output on the input camera images based on the list of probabilities
        """
        user_move = np.argmax(prediction)

        user_cat = self.choices[user_move]

        return(user_cat)

    def countdown(self):
        """
            Displats the countdown to zero to indicate to get ready to play game
        """
        print("User Move")
        for i in range(3, 0 ,-1):
            #time.sleep(1)
            time.time()
            print(i)

        return(None)

    def get_prediction(self):
        """
            Open the camera and gets the prediction for the move made
        """
        while True:
            self.countdown()
            ret,frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)

            choice = self.get_user_input(prediction[0])
            if choice != 'nothing':
                break

            if cv2.waitKey(1) & 0XFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

        return(choice)

  


        
        
        
        
        
        
        
        
        
        
    