import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import Qt


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ui/log_in.ui', self)  # 로드된 UI 파일을 현재 윈도우에 적용

        pixmap = QPixmap("ui/img/ESL_logo.png")

        self.logo.setPixmap(pixmap.scaled(500,500,Qt.IgnoreAspectRatio))
        self.login_button.clicked.connect(self.login)
        self.find_id_pw

    def login(self):
        email = self.email_input.text()
        password = self.passwd_input.text()

        # 로그인 처리 로직
        if email == 'admin' and password == 'password':
            QMessageBox.information(self, '로그인', '로그인 성공')
        else:
            QMessageBox.warning(self, '로그인', '로그인 실패')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
