# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesBXOuBa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setLayoutDirection(Qt.LeftToRight)
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_2 = QVBoxLayout(self.page_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.page_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 830, 570))
        self.scrollAreaWidgetContents.setStyleSheet(u"background: transparent;")
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.page_4_title = QLabel(self.scrollAreaWidgetContents)
        self.page_4_title.setObjectName(u"page_4_title")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        self.page_4_title.setFont(font1)
        self.page_4_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.page_4_title)

        self.page_4_descript = QLabel(self.scrollAreaWidgetContents)
        self.page_4_descript.setObjectName(u"page_4_descript")
        self.page_4_descript.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.page_4_descript)

        self.p_4_row_1 = QVBoxLayout()
        self.p_4_row_1.setObjectName(u"p_4_row_1")

        self.verticalLayout_4.addLayout(self.p_4_row_1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_5 = QVBoxLayout(self.page_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.page_5_layout = QVBoxLayout()
        self.page_5_layout.setSpacing(0)
        self.page_5_layout.setObjectName(u"page_5_layout")
        self.video_label = QLabel(self.page_5)
        self.video_label.setObjectName(u"video_label")

        self.page_5_layout.addWidget(self.video_label)

        self.about_video = QLabel(self.page_5)
        self.about_video.setObjectName(u"about_video")
        self.about_video.setMaximumSize(QSize(16777215, 40))

        self.page_5_layout.addWidget(self.about_video)

        self.webcam_label = QLabel(self.page_5)
        self.webcam_label.setObjectName(u"webcam_label")

        self.page_5_layout.addWidget(self.webcam_label)

        self.sign_recognition = QLabel(self.page_5)
        self.sign_recognition.setObjectName(u"sign_recognition")
        self.sign_recognition.setMaximumSize(QSize(16777215, 40))

        self.page_5_layout.addWidget(self.sign_recognition)


        self.verticalLayout_5.addLayout(self.page_5_layout)

        self.pages.addWidget(self.page_5)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PyOneDark GUI", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
        self.page_4_title.setText(QCoreApplication.translate("MainPages", u"\ud559\uc2b5\uacfc\uc815", None))
        self.page_4_descript.setText(QCoreApplication.translate("MainPages", u"\uc544\ub798\uc5d0 \uc81c\uacf5\ub418\ub294 \uc218\uc5b4 \ud559\uc2b5 \uacfc\uc815\uc744 \ud1b5\ud574 \uc6d0\ud558\ub294 \uc218\uc5b4 \uc8fc\uc81c\ub97c \uc120\ud0dd\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \uac01 \ud559\uc2b5 \uacfc\uc815\uc740 \ucde8\ubbf8, \uc131\uaca9, \uac00\uc871\uad00\uacc4, \ucd9c\uc0dd, \ub098\uc774\ub300, \uc5b8\uc5b4 \uc785\ub2c8\ub2e4.", None))
        self.video_label.setText("")
        self.about_video.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.webcam_label.setText("")
        self.sign_recognition.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
    # retranslateUi

