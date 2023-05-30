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

    def initVideoWebcam(self, videoName, vLable, cLable):
        self.sign_video = vLable
        self.vid_thread = VideoThread()
        self.setVideoName(videoName)
        self.vid_thread.setVideoPath(self.current_dir + self.prefix + self.videoName + self.suffix)
        self.vid_thread.change_pixmap_signal.connect(self.update_vid_image)

        self.webcam = cLable
        self.webcam_thread = WebCamThread()
        self.webcam_thread.change_pixmap_signal.connect(self.update_webcam_image)

        self.sign_video.setScaledContents(True)
        self.webcam.setScaledContents(True)

    def setVideoName(self, videoName):
        self.videoName = videoName

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

    def startVideo(self):
        if not (self.vid_thread.isRunning() and self.webcam_thread.isRunning()):
            self.initVideoWebcam(self.videoName, widgets.vid_label, widgets.webcam_label)
        self.vid_thread.start()
        self.webcam_thread.start()


    def stopVideo(self):
        self.vid_thread.stop()
        self.webcam_thread.stop()
        # 필요한지 의문임.
        # del self.vid_thread
        # del self.webcam_thread
    def relodingVideoCam(self, videoName, vLable, cLable):
        self.stopVideo()
        self.initVideoWebcam(videoName)
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        #   비디오 캠 세팅 #############################
        self.initVideoWebcam('권투', widgets.vid_label, widgets.webcam_label)
        #   비디오 캠 리로딩 #############################
        # self.relodingVideoCam('권투', widgets.sign_video, widgets.webcam)
        #   비디오 캠 시작 ################################
        #self.startVideo()
        #   비디오 캠 정지 ################################
        # self.stopVideo()



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
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if not btnName == "btn_learn":
            self.stopVideo()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "pushButton":
            widgets.stackedWidget.setCurrentWidget(widgets.choose_course)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_learn":
            widgets.stackedWidget.setCurrentWidget(widgets.wordList)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_quiz":
            widgets.stackedWidget.setCurrentWidget(widgets.quiz) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_wordList":
            widgets.stackedWidget.setCurrentWidget(widgets.learn)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            # self.startVideo()
            print("Save BTN clicked!")

        # if btnName == "btn_dictionary":
        #     widgets.stackedWidget.setCurrentWidget(widgets.choose_course)  # SET PAGE
        #     UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
        #     btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
        #     # self.startVideo()
        #     print("Save BTN clicked!")

        if btnName == "hobby_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.learning_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            self.startVideo()

        if btnName == "character_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.learning_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            self.startVideo()

        if btnName == "family_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.learning_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            self.startVideo()

        if btnName == "age_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.learning_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            self.startVideo()

        if btnName == "language_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.learning_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            self.startVideo()

        if btnName == "birth_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.learning_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            self.startVideo()

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

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
    sys.exit(app.exec())
