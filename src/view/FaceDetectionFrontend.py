"""src/view: the frontend for the face detection program"""

"""Import the necessary modules"""
import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton 
from PyQt5.QtGui import QImage, QPixmap
sys.path.append("C:/Users/jerem/everything_python/face_detector_program/Model/")
from face_detection_backend import Backend


class Program():
    """Main class for the Face Detection App."""

    def __init__(self):
        """Initialize the application."""
        self.app = QApplication(sys.argv) 
        self.backend = Backend()
        
        self.setup_ui()
        self.flag_init()
        self.connect_events()
    
    def setup_ui(self):
        """Set up the user interface."""
        self.window = QWidget()
        self.window.setWindowTitle('Face Detection App')
        self.window.setGeometry(700, 250, 700, 700) 

        self.FaceCor = QLabel("<h1>Face Coordinates</h1>", parent=self.window)
        self.FaceCor.move(50, 50)

        self.DisplayCor = QLabel("<h3>coordinates of detected faces will appear here...</h3>", parent=self.window)
        self.DisplayCor.move(50, 150)

        self.FeedLabel = QLabel("<h1>Face Detection Feed</h1>", parent=self.window)
        self.FeedLabel.move(1000, 50)

        self.Face_Detection = QLabel('<h3>feed will appear here...</h3>', parent = self.window)
        self.Face_Detection.move(1000, 200)

        self.start_button = QPushButton("Start Feed", parent=self.window)
        self.start_button.move(1000, 950)

        self.pause_button = QPushButton("Pause Feed", parent=self.window)
        self.pause_button.move(1100, 950)

        self.end_button = QPushButton("End Feed", parent=self.window)
        self.end_button.move(1200, 950)

    def connect_events(self):
        """Connect the click events to functions."""
        self.start_button.clicked.connect(self.start_feed)
        self.pause_button.clicked.connect(self.pause_feed)
        self.end_button.clicked.connect(self.end_feed)

    def update_face_detection(self, q_image, start_flag):
        """Update the face detection display."""
        self.Face_Detection.setPixmap(QPixmap())
        if start_flag:
            pixmap = QPixmap(q_image)
            self.Face_Detection.setPixmap(pixmap)
            self.Face_Detection.resize(pixmap.width(), pixmap.height())
        else:
            self.Face_Detection.setText('<h3>feed stopped. feed will reappear here...</h3>')

    def update_face_cor(self, faces):
        """Update the face coordinates display."""
        coordinates_text = ""
        for index, (x, y, w, h) in enumerate(faces):
            coordinates_text = f"<h3>Face {index+1}: x: {x} y: {y} w: {w} h: {h}</h3>"
        self.DisplayCor.setText(coordinates_text)  

    def update_gui(self, frame, faces, start_flag):
        """Update GUI with frames and faces.""" 
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        self.q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.update_face_detection(self.q_image, start_flag)
        self.update_face_cor(faces)

    def flag_init(self):
        """Initialize flags."""
        self.pause_flag = False
        self.end_flag = False
        self.start_flag = False


    def start_feed(self):
        """Start the feed."""
        self.start_flag = True

        while self.start_flag:
            self.pause_flag = False
            self.end_flag = False 
            
            result, frame = self.backend.video.read()
            if not result:
                break
            faces = self.backend.face_detector(frame)

            self.update_gui(frame, faces, self.start_flag)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            if self.pause_flag:
                break
            
            elif self.end_flag:
                self.start_flag = False
            
            if self.start_flag == False:
                self.update_face_detection(self.q_image, self.start_flag)

    def pause_feed(self):
        """Pause the feed."""
        self.pause_flag = True

    def end_feed(self):
        """End the feed."""
        self.end_flag = True


if __name__ == "__main__":
    program = Program()
    program.window.show()
    sys.exit(program.app.exec())
