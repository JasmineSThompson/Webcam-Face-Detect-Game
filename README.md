# Webcam-Face-Detect-Game
A game made using OpenCV where the aim is to have your face tracked/recognised at the end of a timer.

Instructions for use:
1. Download the haarcascade_frontalface_default.xml from here: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
2. Place the above file in the same folder as the Python program
3. Run the Python program

The aim of the game is to have your face framed by the red box at the end of the 30 second period the game is played. Other faces will be framed by a black frame. In order to take the red frame from another face you should move your face close to or in front of theirs so it registers your face as the successive closest detectable face. Otherwise, the frame will follow a particular face until "stolen".
