from wormhole.video import AbstractVideo
from wormhole.utils import FrameController

import cv2
from time import sleep
from threading import Thread
from typing import Optional

# Creates a video object from a video file
class FileVideo(AbstractVideo):
    def __init__(
            self, filename: str, 
            max_fps: int = 30, 
            height: Optional[int] = None, 
            width: Optional[int] = None,
            repeat: bool = True,
        ):
        # Basic Video Properties
        self.filename: str = filename        
        # Optional Video Properties
        self.repeat: bool = repeat
        # Open Video File
        self.cap = cv2.VideoCapture(self.filename)
        # Set height and width
        height = height or int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = width or int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # Initialize Video Object
        super().__init__(height, width, max_fps)
        # Check if Video File Opened
        if not self.cap.isOpened():
            raise ValueError("Video File Not Opened!")
        # Set up Frame Controller
        self.frame_controller = FrameController(self.max_fps)
        # Start Video Thread
        self.video_thread = Thread(target=self.video_loop)
        self.video_thread.daemon = True
        self.video_thread.start()
        
    def video_loop(self):
        # Start Video Loop
        while True:
            # Read Frame
            ret, frame = self.cap.read()
            # Check if Frame is Valid
            if not ret:
                if self.repeat:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                else:
                    self.set_blank_frame()
                continue
            # Set Frame
            self.set_frame(frame)
            self.frame_controller.next_frame()