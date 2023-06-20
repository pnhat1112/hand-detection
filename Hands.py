import math
import cv2
import numpy as np
import tkinter as tk
import mediapipe as mp
import pydirectinput
import time


# Hàm xử lý khi người dùng chọn một vòng if
def select_if_condition(condition):
    print(f"Selected condition: {condition}")
    # Thực hiện các hành động tương ứng với vòng if đã chọn

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Select If Condition")

# Tạo danh sách các điều kiện cho vòng if
conditions = [
    "Cat Runner",
    "Dinosaur",
    "Car",
]

# Lưu trữ các điều kiện đã chọn
selected_conditions = []

# Hàm xử lý khi người dùng chọn hoặc hủy chọn một điều kiện
def toggle_condition(condition):
    if condition in selected_conditions:
        selected_conditions.remove(condition)
    else:
        selected_conditions.append(condition)

# Tạo nút cho mỗi điều kiện
for condition in conditions:
    button = tk.Button(window, text=condition, command=lambda cond=condition: toggle_condition(cond))
    button.pack()

# Initializing the drawing utils for drawing the facial landmarks on image
mp_drawing = mp.solutions.drawing_utils
mp_drawing_text = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()
        
        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip on horizontal
        image = cv2.flip(image, 1)
        
        # Set flag
        image.flags.writeable = False
        
        # Detections
        results = hands.process(image)
        
        # Set flag to true
        image.flags.writeable = True
        
        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        window.update()
        if not tk.Toplevel.winfo_exists(window):
            break

        height, width, _ = image.shape
        # Rendering results
        if results.multi_hand_landmarks:
            hand_centers = []
            for hand_landmarks in results.multi_hand_landmarks:

                hand_centers.append([int(hand_landmarks.landmark[9].x *width), int(hand_landmarks.landmark[9].y *height)])

                if "Cat Runner" in selected_conditions:
                    if hand_landmarks.landmark[8].y > hand_landmarks.landmark[7].y and \
                            hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y and \
                            hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y and \
                            hand_landmarks.landmark[20].y > hand_landmarks.landmark[19].y and \
                            hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                                print("Nothing")
                                # print(hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y)
                                # print(hand_landmarks.landmark[4].x, hand_landmarks.landmark[3].x)
                                # print(hand_landmarks.landmark[4].y, hand_landmarks.landmark[3].y)

                    elif hand_landmarks.landmark[8].y > hand_landmarks.landmark[7].y and \
                            hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y and \
                            hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y and \
                            hand_landmarks.landmark[20].y > hand_landmarks.landmark[19].y and \
                            hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x: 
                        pydirectinput.keyDown('right')
                        pydirectinput.keyUp('right')
                        print("Right")
                    elif hand_landmarks.landmark[8].y > hand_landmarks.landmark[7].y and \
                        hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y and \
                        hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y and \
                        hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y and \
                        hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x: 
                        pydirectinput.keyDown('left')
                        pydirectinput.keyUp('left')
                        print("Left")
                    elif hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y and \
                        hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y and \
                        hand_landmarks.landmark[16].y < hand_landmarks.landmark[15].y and \
                        hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y:  
                        pydirectinput.keyDown('up') 
                        pydirectinput.keyUp('up')
                        # pydirectinput.click()
                        print("Upp")
                    elif hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y and \
                        hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y and \
                        hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y and \
                        hand_landmarks.landmark[20].y > hand_landmarks.landmark[19].y : 
                        pydirectinput.keyDown('down')
                        pydirectinput.keyUp('down')
                        print("Down")
                    pass
                if "Dinosaur" in selected_conditions:
                    if hand_landmarks.landmark[8].y > hand_landmarks.landmark[7].y and \
                            hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y and \
                            hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y and \
                            hand_landmarks.landmark[20].y > hand_landmarks.landmark[19].y and \
                            hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                                print("Nothing")
                    elif hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y and \
                        hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y and \
                        hand_landmarks.landmark[16].y < hand_landmarks.landmark[15].y and \
                        hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y:  
                        pydirectinput.keyDown('up') 
                        pydirectinput.keyUp('up')
                        # pydirectinput.click()
                        print("Up")
                    elif hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y and \
                        hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y and \
                        hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y and \
                        hand_landmarks.landmark[20].y > hand_landmarks.landmark[19].y : 
                        pydirectinput.keyDown('down')
                        pydirectinput.keyUp('down')
                    pass
                if "Car" in selected_conditions:
                    if len(hand_centers) == 2:
                        cv2.line(image, (hand_centers[0][0], hand_centers[0][1]), (hand_centers[1][0], hand_centers[1][1]), (0, 255, 0), 5)
                        
                        center_x = (hand_centers[0][0] + hand_centers[1][0]) // 2
                        center_y = (hand_centers[0][1] + hand_centers[1][1]) // 2

                        radius = int(math.sqrt((hand_centers[0][0] - hand_centers[1][0]) ** 2 + (hand_centers[0][1] - hand_centers[1][1]) ** 2) / 2)
                        cv2.circle(image, (center_x, center_y), radius, (0, 255, 0), 5)
                        
                        # pydirectinput.keyDown('up')
                        # pydirectinput.keyUp('up')
                        if hand_centers[0][1] - hand_centers[1][1] > 50:
                            print("Left")
                            pydirectinput.keyDown('left')
                            pydirectinput.keyUp('left')
                            print(hand_centers[0][1], hand_centers[1][1])
                        elif hand_centers[1][1] - hand_centers[0][1] > 50:
                            print(hand_centers[0][1], hand_centers[1][1])
                            pydirectinput.keyDown('right')
                            pydirectinput.keyUp('right')
                            print("Right")
                        else:
                            print("Nothing")

                    
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, 
                mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                )
             
            # cv2.putText(image, text, (10, 70), cv2.FONT_HERSHEY_COMPLEX, cor, (0,255,0), 2)   
           
        
        
        cv2.imshow('Hand Tracking', image)

 

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


