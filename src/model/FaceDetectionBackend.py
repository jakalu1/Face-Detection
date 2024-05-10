"""src/model: the backend for the face detection program"""

import cv2

class Backend():
    """Class for backend operations."""
    
    def __init__(self):
        """Initializes backend objects"""
        self.RED_COLOR = (0, 0, 255) 
        self.LINE_THICKNESS = 4 
        self.video = cv2.VideoCapture(0) 
        self.face_classifier = cv2.CascadeClassifier('C:/Users/jerem/everything_python/face_detector_program/Bin/haarcascade_frontalface_default.xml')

    def draw_face_rectangle(self, video, x, y, w, h):
        """Draws a rectangle around the detected face."""
        cv2.rectangle(video, (x, y), (x+w, y+h), self.RED_COLOR, self.LINE_THICKNESS)

    def draw_face_lines(self, video, x, y, w, h):
        """Draws croshair lines on the detected face."""
        top_edge_midpoint = (int(x+(w/2)), y)
        bottom_edge_midpoint = (int(x+(w/2)), int(y+h))
        left_edge_midpoint = (x, int(y+(h/2))) 
        right_edge_midpoint = (int(x+w), int(y+(h/2)))

        cv2.line(video, top_edge_midpoint, bottom_edge_midpoint, self.RED_COLOR, self.LINE_THICKNESS) 
        cv2.line(video, right_edge_midpoint, left_edge_midpoint, self.RED_COLOR, self.LINE_THICKNESS)

    def display_coordinates(self, index, x, y, w, h):
        """Displays the coordinates of the detected faces."""
        print(f"\rFace {index+1}: x: {x} y: {y} w: {w} h: {h}", end="", flush=True)

    def face_detector(self, video):
        """Detects faces in the provided video frame."""
        gray_image = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
        
        for index, (x, y, w, h) in enumerate(faces):
            self.draw_face_rectangle(video, x, y, w, h)
            self.draw_face_lines(video, x, y, w, h)
            self.display_coordinates(index, x, y, w, h)
        return faces
