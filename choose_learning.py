from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap, QIcon
import sys
from PySide6.QtCore import  Slot, QFile
from PySide6.QtUiTools import QUiLoader

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # load the UI file
        loader = QUiLoader()
        file = QFile("ui/ui_choose_learning.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file)
        file.close()

        self.logo_btn = self.ui.findChild(QPushButton, 'logo_btn')
        self.user_icon = self.ui.findChild(QPushButton, 'user_icon')

        self.hobby = self.ui.findChild(QPushButton, 'hobby')
        self.character = self.ui.findChild(QPushButton, 'character')
        self.family = self.ui.findChild(QPushButton, 'family')
        self.born = self.ui.findChild(QPushButton, 'born')
        self.age = self.ui.findChild(QPushButton, 'age')
        self.language = self.ui.findChild(QPushButton, 'language')

        self.logo_btn.setStyleSheet('border-image: url(ui/img/ESL_logo_small2.png);')
        self.user_icon.setStyleSheet('border-image: url(ui/img/user3.png);')

        self.image_path = ["ui/img/취미.png", "ui/img/성격.png", "ui/img/가족관계.png", "ui/img/출생.png", "ui/img/나이대.png", "ui/img/언어.png"]

        # 버튼의 배경 이미지 설정
        self.hobby.setStyleSheet(f"QPushButton {{ border-image: url({self.image_path[0]}); }}")
        self.character.setStyleSheet(f"QPushButton {{ border-image: url({self.image_path[1]}); }}")
        self.family.setStyleSheet(f"QPushButton {{ border-image: url({self.image_path[2]}); }}")
        self.born.setStyleSheet(f"QPushButton {{ border-image: url({self.image_path[3]}); }}")
        self.age.setStyleSheet(f"QPushButton {{ border-image: url({self.image_path[4]}); }}")
        self.language.setStyleSheet(f"QPushButton {{ border-image: url({self.image_path[5]}); }}")

        self.setWindowTitle("권투 학습하기")

        self.setCentralWidget(self.ui)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    sys.exit(app.exec())
