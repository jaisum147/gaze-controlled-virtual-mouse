import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Safety feature ON (recommended)
pyautogui.FAILSAFE = True

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

# Eye landmarks (left eye)
LEFT_EYE = [33, 160, 158, 133, 153, 144]
IRIS_ID = 468

blink_count = 0
last_blink_time = time.time()
gaze_hold_start = None

def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        face = result.multi_face_landmarks[0]

        # Eye landmarks
        eye = np.array([
            (int(face.landmark[i].x * w), int(face.landmark[i].y * h))
            for i in LEFT_EYE
        ])

        ear = eye_aspect_ratio(eye)

        # ---------- BLINK DETECTION ----------
        if ear < 0.2:
            if time.time() - last_blink_time > 0.3:
                blink_count += 1
                last_blink_time = time.time()

        if time.time() - last_blink_time > 1:
            if blink_count == 2:
                pyautogui.click()          # Double blink → Left click
            elif blink_count == 3:
                pyautogui.rightClick()     # Triple blink → Right click
            blink_count = 0

        # ---------- GAZE DIRECTION ----------
        iris = face.landmark[IRIS_ID]
        dx = iris.x - 0.5
        dy = iris.y - 0.5

        move_x = 0
        move_y = 0

        if dx < -0.03:
            move_x = -20      # LEFT
        elif dx > 0.03:
            move_x = 20       # RIGHT

        if dy < -0.03:
            move_y = -20      # UP
        elif dy > 0.03:
            move_y = 20       # DOWN

        # ---------- SAFE CURSOR MOVEMENT ----------
        current_x, current_y = pyautogui.position()

        if move_x == 0 and move_y == 0:
            # CENTER gaze → hold
            if gaze_hold_start is None:
                gaze_hold_start = time.time()
            elif time.time() - gaze_hold_start > 3:
                pyautogui.click()          # Gaze hold 3 sec → Select
                gaze_hold_start = None
        else:
            gaze_hold_start = None

            # Keep cursor away from screen corners (prevents fail-safe)
            new_x = min(max(10, current_x + move_x), screen_w - 10)
            new_y = min(max(10, current_y + move_y), screen_h - 10)

            pyautogui.moveTo(new_x, new_y, duration=0.1)

    cv2.imshow("Gaze Controlled Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
