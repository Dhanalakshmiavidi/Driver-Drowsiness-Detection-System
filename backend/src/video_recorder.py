import cv2
import collections

class SmartRecorder:
    def __init__(self):
        self.buffer = collections.deque(maxlen=100)
        self.recording = False
        self.out = None

    def update(self, frame):
        self.buffer.append(frame)

    def start(self, filename):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))

        for f in self.buffer:
            self.out.write(f)

        self.recording = True

    def write(self, frame):
        if self.recording:
            self.out.write(frame)

    def stop(self):
        if self.out:
            self.out.release()
        self.recording = False