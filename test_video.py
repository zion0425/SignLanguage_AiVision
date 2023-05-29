from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import  Slot, QFile
import numpy as np
from PySide6.QtUiTools import QUiLoader
from video_thread import VideoThread
from web_cam_thread import WebCamThread

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create QLabel widgets for video and webcam
        # self.sign_video = QLabel(self)
        self.webcam = QLabel(self)

        # Set window title
        self.setWindowTitle("권투 학습하기")

        # Create the video capture thread
        # self.vid_thread = VideoThread()
        # # Connect its signal to the update_vid_image slot
        # self.vid_thread.change_pixmap_signal.connect(self.update_vid_image)
        # # Start the thread
        # self.vid_thread.start()
        # load the UI file
        loader = QUiLoader()
        file = QFile("ui/prac_sign.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file)
        file.close()

        self.icon_btn = self.ui.findChild(QPushButton, 'icon_btn')
        self.user_icon_btn = self.ui.findChild(QPushButton, 'user_icon_btn')
        self.sign_video = self.ui.findChild(QLabel, 'sign_video')
        self.webcam = self.ui.findChild(QLabel, 'webcam')

        self.icon_btn.setStyleSheet('border-image: url(ui/img/ESL_logo_small2.png);')
        self.user_icon_btn.setStyleSheet('border-image: url(ui/img/user3.png);')

        self.setWindowTitle("권투 학습하기")

        # create the video capture thread
        self.vid_thread = VideoThread()
        # connect its signal to the update_vid_image slot
        self.vid_thread.change_pixmap_signal.connect(self.update_vid_image)
        # start the thread
        self.vid_thread.start()

        self.webcam_thread = WebCamThread()
        self.webcam_thread.change_pixmap_signal.connect(self.update_webcam_image)
        self.webcam_thread.start()

        self.setCentralWidget(QWidget(self))
        self.show()

        # Adjust QLabel sizes
        # self.sign_video.setScaledContents(True)

        self.webcam.setScaledContents(True)

    def closeEvent(self, event):
        # self.vid_thread.stop()
        self.webcam_thread.stop()
        event.accept()

    # @Slot(np.ndarray)
    # def update_vid_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        # qt_img = self.convert_cv_qt(cv_img)
        # self.sign_video.setPixmap(qt_img)

        self.setCentralWidget(self.ui)
        self.show()

        # Adjust QLabel sizes
        self.sign_video.setScaledContents(True)
        self.webcam.setScaledContents(True)
    def closeEvent(self, event):
        self.vid_thread.stop()
        self.webcam_thread.stop()
        event.accept()

    @Slot(np.ndarray)
    def update_vid_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.sign_video.setPixmap(qt_img)

    @Slot(np.ndarray)
    def update_webcam_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.webcam.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = QPixmap.fromImage(convert_to_Qt_format)
        return p


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    sys.exit(app.exec())
