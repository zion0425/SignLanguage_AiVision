from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QPushButton
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi('ui/prac_sign.ui', self)  # 로드된 UI 파일을 현재 윈도우에 적용

        self.icon_btn.setStyleSheet('border-image: url(ui/img/ESL_logo_small2.png);')
        self.user_icon_btn.setStyleSheet('border-image: url(ui/img/user3.png);')


    def play_video(self):
        # 비디오 재생
        self.media_player.play()

    def stop_video(self):
        # 비디오 정지
        self.media_player.stop()

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()

