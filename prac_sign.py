import sys
import cv2
from PyQt5 import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.uic import loadUi


class VideoViewer(QMainWindow):
    def __init__(self):
        super(VideoViewer, self).__init__()

        loadUi('ui/prac_sign.ui', self)  # UI 파일의 경로로 변경해야 합니다.

        self.icon_btn.setStyleSheet('border-image: url(ui/img/ESL_logo_small2.png);')
        self.user_icon_btn.setStyleSheet('border-image: url(ui/img/user3.png);')

        self.video = cv2.VideoCapture('videos/권투.mp4')  # 비디오 파일의 경로로 변경해야 합니다.

        while True:
            ret, cv_img = self.video.read()
            if ret:
                # convert the image to Qt format
                qt_img = self.convert_cv_qt(cv_img)
                # display it
                self.sign_video.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.sign_video.width(), self.sign_video.height(), Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = VideoViewer()
    viewer.show()
    sys.exit(app.exec_())
