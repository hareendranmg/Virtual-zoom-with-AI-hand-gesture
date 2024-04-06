import time
import cv2
import pyautogui
from HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.7)
startDist = None
scale = 0
cx, cy = 500,500
while True:
    # success, img = cap.read()
    img = cv2.imread("sample.jpg")
    hands, img = detector.findHands(img)

    if len(hands) == 2:
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and \
                detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            if startDist is None:
                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                startDist = length

            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((length - startDist) // 2)
            cx, cy = info[4:]
            print(scale)
            if scale > 0:
                    pyautogui.hotkey('ctrl', '+')
                    time.sleep(0.1) # Replace with actual command
            elif scale < 0:
                    pyautogui.hotkey('ctrl', '-')
                    time.sleep(0.1)  # Replace with actual command
        else:
            startDist = None



    cv2.imshow("Image", img)
    cv2.waitKey(1)
