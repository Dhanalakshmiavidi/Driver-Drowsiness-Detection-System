"""import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Mouth landmarks
UPPER_LIP = 13
LOWER_LIP = 14

# Head movement landmarks
NOSE = 1
LEFT_FACE = 234
RIGHT_FACE = 454

def calculate_ear(landmarks, eye):
    p1 = np.array(landmarks[eye[0]])
    p2 = np.array(landmarks[eye[1]])
    p3 = np.array(landmarks[eye[2]])
    p4 = np.array(landmarks[eye[3]])
    p5 = np.array(landmarks[eye[4]])
    p6 = np.array(landmarks[eye[5]])

    vertical = np.linalg.norm(p2 - p6) + np.linalg.norm(p3 - p5)
    horizontal = np.linalg.norm(p1 - p4)

    return vertical / (2.0 * horizontal)

def detect(frame):
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    status = "Looking Center"
    drowsy = False

    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]
        landmarks = []

        for lm in face.landmark:
            landmarks.append((int(lm.x * w), int(lm.y * h)))

        # ---------------- EYE DETECTION ----------------
        left_ear = calculate_ear(landmarks, LEFT_EYE)
        right_ear = calculate_ear(landmarks, RIGHT_EYE)
        ear = (left_ear + right_ear) / 2

        # Adjusted for glasses
        eye_closed = ear < 0.20   # lowered threshold

        # ---------------- YAWNING ----------------
        top_lip = np.array(landmarks[UPPER_LIP])
        bottom_lip = np.array(landmarks[LOWER_LIP])

        mouth_dist = np.linalg.norm(top_lip - bottom_lip)
        yawning = mouth_dist > 25

        # ---------------- HEAD MOVEMENT ----------------
        nose = landmarks[NOSE]
        left_face = landmarks[LEFT_FACE]
        right_face = landmarks[RIGHT_FACE]

        face_center_x = (left_face[0] + right_face[0]) // 2

        if nose[0] < face_center_x - 40:
            status = "Looking Left"
        elif nose[0] > face_center_x + 40:
            status = "Looking Right"
        else:
            status = "Looking Center"

        if nose[1] > landmarks[LEFT_FACE][1] + 40:
            status = "Looking Down"

        # ---------------- FINAL LOGIC ----------------
        if eye_closed or yawning or status != "Looking Center":
            drowsy = True

        # ---------------- DISPLAY ----------------
        cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        cv2.putText(frame, f"Mouth: {mouth_dist:.1f}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)

        cv2.putText(frame, status, (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    return drowsy, frame"""

import cv2
import numpy as np
import mediapipe as mp
from scipy.spatial import distance
import winsound
import os
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH = [13, 14]

EYE_AR_THRESHOLD = 0.30
YAWN_THRESHOLD = 15

COUNTER = 0

# 🔊 Sound path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(BASE_DIR, "mixkit-alert-alarm-1005.wav")

# 🔥 Smart alert variables
direction_start_time = None
alert_level = 0


def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)


def detect(frame):
    global COUNTER, direction_start_time, alert_level

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return False

    for face in results.multi_face_landmarks:
        landmarks = face.landmark

        # 👀 Eye detection
        leftEye = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in LEFT_EYE]
        rightEye = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in RIGHT_EYE]

        ear = (eye_aspect_ratio(leftEye) + eye_aspect_ratio(rightEye)) / 2.0

        # 😴 Drowsiness Detection
        if ear < EYE_AR_THRESHOLD:
            COUNTER += 1

            if COUNTER > 20:
                cv2.putText(frame, "DROWSY!", (180, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                # 🚨 Strong alert for drowsiness
                winsound.PlaySound(sound_path,
                                   winsound.SND_FILENAME | winsound.SND_ASYNC)

                return True
        else:
            COUNTER = 0

        # 😮 Yawning Detection
        top = landmarks[MOUTH[0]]
        bottom = landmarks[MOUTH[1]]
        mouth_dist = abs(int(top.y * h) - int(bottom.y * h))

        if mouth_dist > YAWN_THRESHOLD:
            cv2.putText(frame, "YAWNING", (180, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

        # 👤 Face Direction Detection
        nose = landmarks[1]

        if nose.x < 0.35:
            direction = "LEFT"
        elif nose.x > 0.65:
            direction = "RIGHT"
        elif nose.y < 0.35:
            direction = "UP"
        elif nose.y > 0.65:
            direction = "DOWN"
        else:
            direction = "CENTER"

        cv2.putText(frame, f"LOOKING {direction}", (120, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)

        # 🔥 SMART GRADUAL ALERT SYSTEM (5s / 10s / 30s)
        current_time = time.time()

        if direction != "CENTER":
            if direction_start_time is None:
                direction_start_time = current_time

            duration = current_time - direction_start_time

            # ⏳ 5 sec → soft alert
            if duration > 5 and alert_level == 0:
                winsound.Beep(500, 200)
                alert_level = 1

            # ⏳ 10 sec → medium alert
            elif duration > 10 and alert_level == 1:
                winsound.Beep(800, 400)
                alert_level = 2

            # ⏳ 30 sec → strong alert
            elif duration > 30 and alert_level == 2:
                winsound.PlaySound(sound_path,
                                   winsound.SND_FILENAME | winsound.SND_ASYNC)
                alert_level = 3

        else:
            # ✅ Reset when looking center
            direction_start_time = None
            alert_level = 0

    return False