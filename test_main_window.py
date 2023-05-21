import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ui/main_window.ui', self)  # 로드된 UI 파일을 현재 윈도우에 적용

        self.icon_btn.setStyleSheet('border-image: url(ui/img/ESL_logo_small2.png);')
        self.user_icon_btn.setStyleSheet('border-image: url(ui/img/user3.png);')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
