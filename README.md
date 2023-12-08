# Hand Gesture Volume Control

This Python script utilizes the Mediapipe and OpenCV libraries to control system volume based on hand gestures captured through a webcam.

## Description

The script captures frames from the webcam, detects hand landmarks using the MediaPipe Hands module, and calculates the distance between specific landmarks (fingertips). It maps this distance to a predefined volume range and adjusts the system volume accordingly.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Mediapipe (`mediapipe`)
- NumPy (`numpy`)
- Pycaw (`pycaw`)
- Comtypes (`comtypes`)

## Installation and Setup

Install the required Python libraries:
```bash
   pip install opencv-python mediapipe numpy pycaw comtypes 
```

 ## Usage
 
  1. Ensure your hand is visible to the webcam.
  
  2. Move your index finger and thumb to control the volume. Bring them closer or farther apart to increase or decrease the volume, respectively.
  
  3. Press 'q' to exit the volume control.

 ## Steps
 
1. Connect a webcam to your system.

2. Run the Python script:
```bash
   python hand_gesture_volume_control.py 
```
