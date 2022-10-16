def main():

    import os
    import uuid

    import cv2
    import mediapipe as mp
    import mouse
    import numpy as np
    import time


    def dist(e1, e2):
        return np.sqrt((e2.x-e1.x)**2 + (e2.y-e1.y)**2)

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()

            # BGR 2 RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Flip on horizontal
            image = cv2.flip(image, 1)

            # Set Flag
            image.flags.writeable = False

            # Detections
            results = hands.process(image)

            # Set flag to true
            image.flags.writeable = True

            # RGB 2 BGR
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # # Detections
            # print(results)
            # Rendering the results
            if results.multi_hand_landmarks:

                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
                    _index_landmark = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    _middle_landmark = hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                    #1279 719
                    if dist(_index_landmark, _middle_landmark) < 0.07:
                        mouse.press('left')
                        time.sleep(1)
                        print('click')

                    else:
                        mouse.move(
                            1300*_index_landmark.x,
                            750*_index_landmark.y
                        )


            cv2.imshow('Hand Tracking', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()