import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import Qt


class SignInWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ui/sign_in.ui', self)  # 로드된 UI 파일을 현재 윈도우에 적용



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignInWindow()
    window.show()
    sys.exit(app.exec_())
