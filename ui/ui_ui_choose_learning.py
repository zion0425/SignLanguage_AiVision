# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_choose_learninggNWAky.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1103, 904)
        mainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 1101, 101))
        self.frame.setStyleSheet(u"border-bottom: 2px solid #000000;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.logo_btn = QPushButton(self.frame)
        self.logo_btn.setObjectName(u"logo_btn")
        self.logo_btn.setGeometry(QRect(6, 1, 151, 91))
        self.logo_btn.setStyleSheet(u"background-image: url(:/icon/ESL_logo_small2.png);")
        self.logo_btn.setFlat(True)
        self.user_icon = QPushButton(self.frame)
        self.user_icon.setObjectName(u"user_icon")
        self.user_icon.setGeometry(QRect(879, 44, 51, 51))
        self.user_icon.setStyleSheet(u"background-image:url(:/icon/user3.png);\n"
"border-bottom: none;\n"
"")
        self.user_icon.setFlat(True)
        self.user_info_txt = QPushButton(self.frame)
        self.user_info_txt.setObjectName(u"user_info_txt")
        self.user_info_txt.setGeometry(QRect(927, 50, 161, 41))
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(26)
        self.user_info_txt.setFont(font)
        self.user_info_txt.setStyleSheet(u"border-bottom: none;")
        self.user_info_txt.setFlat(True)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setGeometry(QRect(0, 111, 251, 781))
        self.left_menu.setStyleSheet(u"border-right: 2px solid #000000;\n"
"")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout = QVBoxLayout()
        self.left_menu_layout.setSpacing(30)
        self.left_menu_layout.setObjectName(u"left_menu_layout")
        self.learn_sign_lang = QPushButton(self.left_menu)
        self.learn_sign_lang.setObjectName(u"learn_sign_lang")
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\uace0\ub515")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.learn_sign_lang.setFont(font1)

        self.left_menu_layout.addWidget(self.learn_sign_lang)

        self.word_book = QPushButton(self.left_menu)
        self.word_book.setObjectName(u"word_book")
        self.word_book.setFont(font1)

        self.left_menu_layout.addWidget(self.word_book)

        self.dict_btn = QPushButton(self.left_menu)
        self.dict_btn.setObjectName(u"dict_btn")
        self.dict_btn.setFont(font1)

        self.left_menu_layout.addWidget(self.dict_btn)


        self.verticalLayout_2.addLayout(self.left_menu_layout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(259, 119, 841, 761))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 839, 759))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(820, 40))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 80))
        self.label_2.setMaximumSize(QSize(16777215, 80))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hobby = QPushButton(self.scrollAreaWidgetContents)
        self.hobby.setObjectName(u"hobby")
        self.hobby.setMinimumSize(QSize(221, 244))
        self.hobby.setMaximumSize(QSize(221, 244))

        self.horizontalLayout_2.addWidget(self.hobby)

        self.character = QPushButton(self.scrollAreaWidgetContents)
        self.character.setObjectName(u"character")
        self.character.setMinimumSize(QSize(221, 244))
        self.character.setMaximumSize(QSize(221, 244))

        self.horizontalLayout_2.addWidget(self.character)

        self.family = QPushButton(self.scrollAreaWidgetContents)
        self.family.setObjectName(u"family")
        self.family.setMinimumSize(QSize(221, 244))
        self.family.setMaximumSize(QSize(221, 244))

        self.horizontalLayout_2.addWidget(self.family)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.born = QPushButton(self.scrollAreaWidgetContents)
        self.born.setObjectName(u"born")
        self.born.setMinimumSize(QSize(221, 244))
        self.born.setMaximumSize(QSize(221, 244))

        self.horizontalLayout.addWidget(self.born)

        self.age = QPushButton(self.scrollAreaWidgetContents)
        self.age.setObjectName(u"age")
        self.age.setMinimumSize(QSize(221, 244))
        self.age.setMaximumSize(QSize(221, 244))

        self.horizontalLayout.addWidget(self.age)

        self.language = QPushButton(self.scrollAreaWidgetContents)
        self.language.setObjectName(u"language")
        self.language.setMinimumSize(QSize(221, 244))
        self.language.setMaximumSize(QSize(221, 244))

        self.horizontalLayout.addWidget(self.language)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Window", None))
        self.logo_btn.setText("")
        self.user_icon.setText("")
        self.user_info_txt.setText(QCoreApplication.translate("mainWindow", u"\ud68c\uc6d0 \ub2d8", None))
        self.learn_sign_lang.setText(QCoreApplication.translate("mainWindow", u"\uc218\uc5b4 \ud559\uc2b5", None))
        self.word_book.setText(QCoreApplication.translate("mainWindow", u"\ub2e8\uc5b4\uc7a5", None))
        self.dict_btn.setText(QCoreApplication.translate("mainWindow", u"\uc0ac\uc804", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\ud559\uc2b5\uacfc\uc815", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\ud559\uc2b5\uc790\uac00 \uc218\uc5b4\uc758 \uae30\ucd08 \uac1c\ub150\uacfc \uc6d0\ub9ac\ub97c \uc774\ud574\ud558\ub294\ub370 \uc911\uc810\uc744 \ub461\ub2c8\ub2e4. \n"
"\ucde8\ubbf8, \uc131\uaca9, \uac00\uc871\uad00\uacc4, \uce28\uc0dd, \ub098\uc774\ub300, \uc5b8\uc5b4\uc640 \uad00\ub828\ub41c \ub2e8\uc5b4\ub4e4\uc744 \ud559\uc2b5\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4.", None))
        self.hobby.setText("")
        self.character.setText("")
        self.family.setText("")
        self.born.setText("")
        self.age.setText("")
        self.language.setText("")
    # retranslateUi

