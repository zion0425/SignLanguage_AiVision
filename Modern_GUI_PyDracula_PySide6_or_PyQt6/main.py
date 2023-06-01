# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
from PySide6 import QtGui
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
import cv2
from PySide6.QtCore import  Slot
import numpy as np
import sys
import os
import platform
from Modern_GUI_PyDracula_PySide6_or_PyQt6.video_thread import VideoThread
from Modern_GUI_PyDracula_PySide6_or_PyQt6.web_cam_thread import WebCamThread
import dictionary


# from Modern_GUI_PyDracula_PySide6_or_PyQt6.vdi_cam import Vdi_Cam
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
# from Modern_GUI_PyDracula_PySide6_or_PyQt6.modules import *
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    prefix = '/videos/'
    suffix = '.mp4'
    videoName = ''

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

    def initVideoWebcam(self, videoName, vLable, cLable):
        self.sign_video = vLable
        self.vid_thread = VideoThread()
        self.setVideoName(videoName)
        self.vid_thread.setVideoPath(self.current_dir + self.prefix + self.videoName + self.suffix)
        self.vid_thread.change_pixmap_signal.connect(self.update_vid_image)

        self.webcam = cLable
        self.webcam_thread = WebCamThread(widgets)
        self.webcam_thread.change_pixmap_signal.connect(self.update_webcam_image)

        self.sign_video.setScaledContents(True)
        self.webcam.setScaledContents(True)

    def setVideoName(self, videoName):
        self.videoName = videoName

    def startVideo(self):
        if not (self.vid_thread.isRunning() and self.webcam_thread.isRunning()):
            self.initVideoWebcam(self.videoName, widgets.vid_label, widgets.webcam_label)
        self.vid_thread.start()
        self.webcam_thread.start()

    def stopVideo(self):
        self.vid_thread.stop()

    def stopThreadds(self):
        self.vid_thread.stop()
        self.webcam_thread.stop()
        # 필요한지 의문임.
        # del self.vid_thread
        # del self.webcam_thread

    def relodingVideo(self, videoName):
        self.stopVideo()
        self.vid_thread = VideoThread()
        self.setVideoName(videoName)
        widgets.about_video.setText(videoName)
        widgets.about_video.setStyleSheet("font-size: 25px;")

        self.vid_thread.setVideoPath(self.current_dir + self.prefix + self.videoName + self.suffix)
        self.webcam_thread.setCurrentVdiName(videoName)
        self.vid_thread.change_pixmap_signal.connect(self.update_vid_image)
        self.vid_thread.start()

    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # //////////////// 비디오 이름 세팅 ///////////////////////
        self.videoFileNames = {
            'hobby': ['노래', '특기', '물놀이', '테니스', '수영', '마라톤', '낚시', '야구', '권투', '없다'],
            'character': ['계획적', '똑똑하다', '귀엽다', '고리타분', '수다스럽다', '긍정적', '독특', '조용하다', '솔직하다', '엉뚱'],
            'family': ['친모', '친부', '여동생', '할아버지', '오빠', '할머니', '누나', '형'],
            'birth': ['한국인'],
            'age': ['노인', '어른', '청년', '청소년'],
            'language': ['한국어', '영어', '일본어']
        }
        # 카테고리별 학습할 수어의 개수를 저장하는 변수
        self.learnCnt = {"hobby": 10, "character": 10, "family": 8, "birth": 1, "age": 4, "language": 3}

        # 유저가 학습하고자 하는 카테고리의 value값을 저장하는 변수
        # 카테고리 선택할 때마다 해당 카테고리의 value값을 넣어준다.
        # 학습 완료, 학습 화면 이탈 시에는, 해당 카테고리의 value값을 0으로 초기화 한다.
        self.userLearnCnt = 0

        #   비디오 캠 세팅 #############################
        self.initVideoWebcam('권투', widgets.vid_label, widgets.webcam_label)



        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "ESL - Educate Sign Language"
        description = "ESL - Educate Sign Language"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_learn.clicked.connect(self.buttonClick)
        widgets.btn_quiz.clicked.connect(self.buttonClick)
        widgets.btn_wordList.clicked.connect(self.buttonClick)
        widgets.btn_dictionary.clicked.connect(self.buttonClick)


        # Main Contents
        widgets.hobby_btn.clicked.connect(self.buttonClick)
        widgets.character_btn.clicked.connect(self.buttonClick)
        widgets.family_btn.clicked.connect(self.buttonClick)
        widgets.age_btn.clicked.connect(self.buttonClick)
        widgets.language_btn.clicked.connect(self.buttonClick)
        widgets.birth_btn.clicked.connect(self.buttonClick)
        widgets.pushButton.clicked.connect(self.buttonClick)
        widgets.pushButton_2.clicked.connect(self.buttonClick)
        widgets.btn_start_learn.clicked.connect(self.buttonClick)
        widgets.btn_start_quiz.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.quiz)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        if btnName != "btn_learn" and btnName != "pushButton_2":
            self.stopThreadds()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.quiz)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_start_learn":
            widgets.stackedWidget.setCurrentWidget(widgets.wordList)

        if btnName == "btn_start_quiz":
            widgets.stackedWidget.setCurrentWidget(widgets.sign_quiz_game)

        # SHOW WIDGETS PAGE
        if btnName == "btn_learn":
            widgets.stackedWidget.setCurrentWidget(widgets.wordList)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_quiz":
            widgets.stackedWidget.setCurrentWidget(widgets.sign_quiz_game) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_wordList":
            widgets.stackedWidget.setCurrentWidget(widgets.dic)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_dictionary":
            widgets.stackedWidget.setCurrentWidget(widgets.dictionary)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "pushButton_2" :
            self.userLearnCnt -= 1
            if self.userLearnCnt < 0 :
                print("finished")
                widgets.stackedWidget.setCurrentWidget(widgets.wordList)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
                self.stopThreadds()
                return
            widgets.pushButton_2.setEnabled(False)
            widgets.pushButton_2.setStyleSheet("background-color: #ffffff;")
            # self.widgets.pushButton_2.setGeometry(QRect(350, 430, 411, 51))
            widgets.pushButton_2.setStyleSheet(u"font-size: 32px;")
            self.webcam_thread.setCorrectCnt(0)
            self.currentVideoName = self.videoFileNames.get(self.currentCategory)[self.userLearnCnt]
            self.webcam_thread.setCurrentVdiName(self.currentVideoName)
            self.relodingVideo(self.currentVideoName)

        if btnName == "hobby_btn" or btnName == "age_btn" or btnName == "language_btn" or btnName == "birth_btn" or btnName == "character_btn" or btnName == "family_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.learning_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            self.startVideo()

            # continue 버튼을 비활성화 상태로 둔다.
            widgets.pushButton_2.setEnabled(False)
            widgets.about_webcam.setText("")
            # 유저가 선택한 학습하고자 한 카테고리 버튼, 즉 카테고리명 저장
            self.currentCategory = btnName.split("_")[0]
            # 유저 카운트, 학습해야 할 수어개수를 저장
            self.userLearnCnt = self.learnCnt[btnName.split("_")[0]] - 1
            # 현재 학습중인 비디오 이름 저장
            self.currentVideoName = self.videoFileNames.get(self.currentCategory)[self.userLearnCnt]
            self.relodingVideo(self.currentVideoName)

        # else :

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/images/ESL_logo_small2.ico"))
    window = MainWindow()

    dictionary.dictionary(widgets)

    sys.exit(app.exec())
