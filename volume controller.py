import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize MediaPipe hands module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Get audio devices and initialize volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get minimum and maximum volume range
volMin, volMax = volume.GetVolumeRange()[:2]

while True:
    # Capture frame-by-frame
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Process hand landmarks
    results = hands.process(imgRGB)
    lmList = []
    
    if results.multi_hand_landmarks:
        for handLandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handLandmark, mpHands.HAND_CONNECTIONS)
    
    if lmList:
        # Get coordinates of two specific hand landmarks
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        
        # Draw circles at landmark points and a line between them
        cv2.circle(img, (x1, y1), 4, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 4, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        
        # Calculate distance between landmarks
        length = hypot(x2 - x1, y2 - y1)
        
        # Map distance to volume range
        vol = np.interp(length, [15, 220], [volMin, volMax])
        print(vol, length)
        
        # Set system volume based on hand distance
        volume.SetMasterVolumeLevel(vol, None)
        
        # Hand range: 15 - 220
        # Volume range: -63.5 - 0.0
        
    # Display the processed image with landmarks
    cv2.imshow('Image', img)
    
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
