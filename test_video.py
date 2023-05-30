from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import  Slot, QFile
import numpy as np
from PySide6.QtUiTools import QUiLoader
from Modern_GUI_PyDracula_PySide6_or_PyQt6.video_thread import VideoThread
from Modern_GUI_PyDracula_PySide6_or_PyQt6.web_cam_thread import WebCamThread

class App(QMainWindow):
    def __init__(self):
        super().__init__()




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
