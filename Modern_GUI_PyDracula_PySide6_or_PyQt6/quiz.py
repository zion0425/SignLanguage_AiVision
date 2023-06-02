import os
import random

import cv2
import numpy as np
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QStringListModel, Slot, QSortFilterProxyModel
from PySide6.QtGui import QPixmap


from Modern_GUI_PyDracula_PySide6_or_PyQt6.Quiz_cam_thread import VideoThread

class Quiz():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    prefix = '/videos/'
    suffix = '.mp4'
    isRun = False
    currentLearnAction = ''

    def __init__(self, widgets):
        self.widgets = widgets
        self.actions = {
            'hobby': ['노래', '특기', '물놀이', '테니스', '수영', '마라톤', '낚시', '야구', '권투', '없다'],
            'character': ['계획적', '똑똑하다', '귀엽다', '고리타분', '수다스럽다', '긍정적', '독특', '조용하다', '솔직하다', '엉뚱'],
            'family': ['친모', '친부', '여동생', '할아버지', '오빠', '할머니', '누나', '형'],
        }

        # Register(Connect) btnEvent
        self.widgets.""" hintBtn """.clicked.connect(self.onClickEvent)
        self.widgets.""" setRandomActionBtn """ .clicked.connect(self.onClickEvent())

        self.sign_video = """ video 보여줄 label """
        self.webcam = """ webcam 보여줄 label """

        # 객체 생성시 랜덤 액션, 현재 학습 정보 세팅
        self.setRandomAction()
        self.setCurrentAction('hobby')
        self.initVideo(self.currentLearnAction)

    def startQuiz(self):
        """hintBtn""".setENabled(True)
        self.isRun = False

    def exitQuiz(self):
        self.isRun = False
        self.stopThreads()

    # 현재 학습 정보(비디오 이름) 저장
    def setCurrentAction(self, learnActionCategory):
        self.currentLearnAction = self.randomAction[learnActionCategory]
        if learnActionCategory != 'hobby':
            """ hintBtn """.setEnabled(False)

    # 랜덤 액션 세팅
    def setRandomAction(self):
        self.randomActions['hobby'] = random.randint(0, len(self.actions.get('hobby')) - 1)
        self.randomActions['character'] = random.randint(0, len(self.actions.get('character')) - 1)
        self.randomActions['family'] = random.randint(0, len(self.actions.get('family')) - 1)


    def onClickEvent(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == """'hintBtn'""":
            self.initVideo()
        if btnName == """'setRandomActionBtn'""":
            self.setRandomAction()
            self.reloadingVdi()

    def nextStep(self):
        if self.currentLearnAction == self.randomActions['hobby']:
            self.setCurrentAction('character')
            self.reloadingVdi()
        elif self.currentLearnAction == self.randomActions['character']:
            self.setCurrentAction('family')
            self.reloadingVdi()
        else :
            self.setCurrentAction('hobby')
            self.reloadingVdi()

    def initVideo(self, videoName):
        self.vid_thread = VideoThread()

        self.vid_thread.setVideoPath(videoName)
        self.vid_thread.change_pixmap_signal.connect(self.update_vid_image)

        self.sign_video.setScaledContents(True)

    def reloadingVdi(self):
        self.videoName = self.current_dir + self.prefix + self.currentLearnAction + self.suffix
        self.initVideo(self.videoName)
        self.startVideo()

    def stopVideo(self):
        self.isRun = False
        self.vid_thread.stop()

    def startVideo(self):
        self.isRun = True
        self.vid_thread.start()

    def filter_items(self):
        search_text = self.search_field.text()
        self.filter_model.setFilterFixedString(search_text)

    def handle_search_button(self):
        self.filter_items()

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


    def initVideo(self, videoName, vLable):
        self.sign_video = vLable
        self.vid_thread = VideoThread()

        self.vid_thread.setVideoPath(videoName)
        self.vid_thread.change_pixmap_signal.connect(self.update_vid_image)

        self.sign_video.setScaledContents(True)

