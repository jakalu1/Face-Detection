                                                <h1>Face Detection Program</h1>

This is a Python program that uses OpenCV and PyQt5 to detect faces in real-time video feed from your webcam. The program displays the video feed with rectangles and crosshairs drawn around the detected faces, along with the coordinates of each face. The purpose of this program is for any robotics project that requires face detection capabilities.

**Getting Started**
To run this program on your computer, follow these steps:

1. Download the required files
      - Download the frontend and backend Python files from the repository.

2. Install dependencies
- Make sure you have Python and the following libraries installed: OpenCV (cv2) and PyQt5.
- You can install them using pip:

pip install opencv-python
pip install pyqt5

3. Download the Haar Cascade file
- Download the haarcascade_frontalface_default.xml file from the "dependencies" folder included in this repository.

4. Modify the backend file
- Open the backend file in a text editor or IDE (e.g., Visual Studio Code).
- Locate the line that initializes the face_classifier (around line 13).
- Replace the file path with the path to the haarcascade_frontalface_default.xml file you downloaded in step 3.

5. Modify the frontend file
- Open the frontend file in a text editor or IDE.
- Locate the line that imports the Backend class (around line 8).
- Replace the file path with the path to the backend file you downloaded in step 1.

6. Run the program
- Open the frontend file in your Python IDE or editor.
- Run the frontend file.
- The Face Detection Program window should open, and you should see the video feed from your webcam with detected faces highlighted.

Make sure to adjust the file paths in steps 4 and 5 according to the locations of the downloaded files on your system.

Note: This program requires a working webcam to capture the video feed. If you encounter any issues, ensure that your webcam is properly connected and functioning.
