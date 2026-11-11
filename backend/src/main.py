
"""import cv2
import time
import os
import datetime

from drowsiness_detector import detect
from email_alert import send_email

# 📁 Create recordings folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
recordings_path = os.path.join(BASE_DIR, "recordings")

if not os.path.exists(recordings_path):
    os.makedirs(recordings_path)


def run_camera():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("❌ Camera not working")
        return

    filename = os.path.join(recordings_path, f"output_{int(time.time())}.mp4")

    # ✅ MP4 FIX
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    print("📁 Recording:", filename)

    last_email_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.resize(frame, (640, 480))

        # 🕒 Timestamp
        cv2.putText(frame, str(datetime.datetime.now()),
                    (10, 470),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255), 1)

        drowsy = detect(frame)

        if drowsy:
            current_time = time.time()

            if current_time - last_email_time > 10:
                print("📧 Sending Email Alert...")

                out.release()  # stop video

                send_email(filename)

                # start new recording
                filename = os.path.join(recordings_path, f"output_{int(time.time())}.mp4")
                out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

                last_email_time = current_time

        out.write(frame)

        cv2.imshow("DriveSafe AI 🚗", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()"""



import cv2
import time
import os
import datetime

from drowsiness_detector import detect
from email_alert import send_email

# 📁 Create recordings folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
recordings_path = os.path.join(BASE_DIR, "recordings")

if not os.path.exists(recordings_path):
    os.makedirs(recordings_path)


def run_camera():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("❌ Camera not working")
        return

    filename = os.path.join(recordings_path, f"output_{int(time.time())}.mp4")

    # ✅ MP4 FIX
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    print("📁 Recording:", filename)

    last_email_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.resize(frame, (640, 480))

        # 🕒 Timestamp
        cv2.putText(frame, str(datetime.datetime.now()),
                    (10, 470),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255), 1)

        drowsy = detect(frame)

        if drowsy:
            current_time = time.time()

            if current_time - last_email_time > 10:
                print("📧 Sending Email Alert...")

                out.release()  # stop video

                send_email(filename)

                # start new recording
                filename = os.path.join(recordings_path, f"output_{int(time.time())}.mp4")
                out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

                last_email_time = current_time

        out.write(frame)

        cv2.imshow("DriveSafe AI 🚗", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_camera()