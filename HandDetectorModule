import cv2
import mediapipe as mp
import time
import pyautogui

cap = cv2.VideoCapture(0)


class hand_detector():
    def __init__(self, mode=False, max_hands=1,min_detection_confidence=0.7, min_tracking_confidence=0.7):
        self.mode = mode
        self.max_hands = max_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,     self.max_hands, self.min_tracking_confidence, self.min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS)

        return img


    def findPosition(self, img):

        lmList = []
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                for id, lm in enumerate(handlms.landmark):
                    height, width, channel = img.shape
                    cx = int(lm.x * width)
                    cy = int(lm.y * height)
                    lmList.append([id, cx, cy])

                    if id % 4 == 0:
                        cv2.circle(img, (cx,cy), 15, (255, 0, 0), cv2.FILLED)

        return lmList

def main():

    while True:
        success, img = cap.read()

        detector = hand_detector()
        img = detector.findHands(img)

        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:

            if lmlist[4][1] >= lmlist[8][1]:
                pyautogui.press('left')
                #print('right')

            elif lmlist[4][1] <= lmlist[8][1]:
                pyautogui.press('right')
                #print('left')

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xff == 27:
           break

if __name__ == '__main__':
    main()
