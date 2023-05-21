import sys
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class VideoViewer(QMainWindow):
    def __init__(self):
        super(VideoViewer, self).__init__()

        loadUi('ui/prac_sign.ui', self)  # UI 파일의 경로로 변경해야 합니다.

        self.icon_btn.setStyleSheet('border-image: url(ui/img/ESL_logo_small2.png);')
        self.user_icon_btn.setStyleSheet('border-image: url(ui/img/user3.png);')

        self.video = cv2.VideoCapture('videos/권투.mp4')  # 비디오 파일의 경로로 변경해야 합니다.
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)  # 비디오 프레임을 업데이트할 주기(ms)를 설정합니다.

    def update_frame(self):
        ret, image = self.video.read()
        if ret:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            bytes_per_line = channel * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            pixmap = pixmap.scaled(self.sign_video.width(), self.sign_video.height(), aspectRatioMode=True)
            self.sign_video.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = VideoViewer()
    viewer.show()
    sys.exit(app.exec_())
