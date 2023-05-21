from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
from PyQt5.uic import loadUi


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        # cap = cv2.VideoCapture('videos/권투.mp4')
        cap = cv2.VideoCapture(0)

        # 영상의 FPS 정보 가져오기
        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = int(1000 / fps)  # 재생 주기(ms)

        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
            else:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 영상이 끝나면 다시 처음으로 돌아감

            # 재생 주기만큼 대기
            cv2.waitKey(delay)

        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi('ui/prac_sign.ui', self)  # UI 파일의 경로로 변경해야 합니다.

        self.icon_btn.setStyleSheet('border-image: url(ui/img/ESL_logo_small2.png);')
        self.user_icon_btn.setStyleSheet('border-image: url(ui/img/user3.png);')

        self.setWindowTitle("Qt live label demo")

        # create the label that holds the image
        self.sign_video = self.findChild(QLabel, 'sign_video')

        # create a text label
        self.textLabel = QLabel('Webcam')

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.sign_video.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())