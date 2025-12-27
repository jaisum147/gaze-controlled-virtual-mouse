>>Gaze-Controlled Virtual Mouse

-->Introduction
This project demonstrates a "gaze-controlled virtual mouse system" that allows a user to control
the mouse cursor using only eye movements and blink gestures. The goal of this project is to provide
a hands-free interaction method using computer vision techniques and a standard webcam.The system tracks eye gaze direction and blink patterns in real time and converts them into
corresponding mouse actions.

-->Features
- Cursor movement using eye gaze:
  - Look left → Move cursor left
  - Look right → Move cursor right
  - Look up → Move cursor up
  - Look down → Move cursor down
- Center gaze stops cursor movement
- Double blink performs a left mouse click
- Triple blink performs a right mouse click
- Holding the gaze at the center for 3 seconds triggers a selection click

>> Tools and Technologies
- Python 3.11
- OpenCV for video capture and processing
- MediaPipe Face Mesh for facial landmark detection
- NumPy for mathematical operations
- PyAutoGUI for mouse control

>> Setup Instructions

-->Step 1: Clone the repository:
git clone https://github.com/your-username/gaze-controlled-virtual-mouse.git
cd gaze-controlled-virtual-mouse
-->Step 2: Install required libraries such as:
    1.OpenCV 
    2.MediaPipe 
    3.NumPy
    4. PyAutoGUI 
  
  
  
  to install use  : pip install opencv-python mediapipe numpy pyautogui

  and
  
  
  to verify wheter it is installed or not use : python -c "import cv2, mediapipe, numpy, pyautogui; print('All installed successfully')"

-->step 3 : Run the program





