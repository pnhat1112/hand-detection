import cv2
import numpy as np
import tkinter as tk
import math
import mediapipe as mp
import pydirectinput


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

# Mở cửa sổ video
cap = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_text = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

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
        
        height, width, _ = image.shape
        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        # Kiểm tra sự kiện đóng cửa sổ giao diện
        window.update()
        if not tk.Toplevel.winfo_exists(window):
            break

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
        # Kiểm tra các điều kiện đã chọn và thực hiện các hành động tương ứng
                if "Cat Runner" in selected_conditions:
                    # Thực hiện các hành động cho Condition 1
                    print("Cat Runner")
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
                if "Dinosaur" in selected_conditions:
                    # Thực hiện các hành động cho Condition 2
                    print("Dinosaur Runner")

                if "Car" in selected_conditions:
                    # Thực hiện các hành động cho Condition 3
                    print("Car Runner")
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, 
            mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
            mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
            )

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
