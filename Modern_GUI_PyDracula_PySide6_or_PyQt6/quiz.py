import os
import random

import cv2
import numpy as np
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QStringListModel, Slot, QSortFilterProxyModel, QTimer
from PySide6.QtGui import QPixmap

from Modern_GUI_PyDracula_PySide6_or_PyQt6.quiz_cam_thread import QuizThread
from Modern_GUI_PyDracula_PySide6_or_PyQt6.video_thread import VideoThread

class Quiz():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    prefix = '/videos/'
    suffix = '.mp4'
    isRun = False
    currentLearnAction = ''
    randomActions = {}
    def __init__(self, widgets):
        self.widgets = widgets
        self.actions = {
            'hobby': ['물놀이', '수영', '마라톤', '낚시', '야구', '권투', '없다'],
            # 'hobby': ['없다'],
            # 'character': ['계획적', '똑똑하다', '귀엽다', '고리타분', '수다스럽다', '긍정적', '독특', '조용하다', '솔직하다', '엉뚱'],
            'character': ['계획적', '똑똑하다',  '고리타분', '수다스럽다', '긍정적', '독특', '조용하다', '솔직하다'],
            'family': ['친모', '친부', '여동생','오빠', '누나', '형'],
        }

        # Register(Connect) btnEvent
        self.widgets.btn_show_hint.clicked.connect(self.hintBtnClickEvent)
        self.widgets.btn_refresh.clicked.connect(self.refreshBtnClickEvent)

        self.sign_video = widgets.hint_video
        self.webcam = widgets.quiz_webcam

        self.setVideo()

        # 객체 생성시 랜덤 액션, 현재 학습 정보 세팅
        self.setRandomAction()
        self.setCurrentAction('hobby')
        self.setCam()

        self.text = self.widgets.label_about_game.text()
        self.current_text_index = 0
        self.interval = 100  # 글자 간의 표시되는 간격을 조절하기 위한 시간 간격 (밀리초 단위)

    def startQuiz(self):
        self.quiz_thread.start()
        self.quiz_thread.category = 'hobby'
        self.quiz_thread.setActionNames(self.randomActions)
        self.quiz_thread.setStrs()
        self.reloadText()

    def reloadText(self):
        self.widgets.inrouduce_phrase.setText("내 취미는 "
                                              "<span style='color:red; text-decoration: underline;'>(" +
                                              self.randomActions['hobby'] + ")</span> 이며,"
                                                                            " 성격은 <span style='color:red; text-decoration: underline;'>(" +
                                              self.randomActions['character'] + ")</span>."
                                                                                " 가족은 <span style='color:red; text-decoration: underline;'>(" +
                                              self.randomActions['family'] + ")</span>(이/가) 있습니다.")
        self.widgets.inrouduce_phrase.setOpenExternalLinks(True)

    def exitQuiz(self):
        self.isRun = False
        self.vid_thread.stop()
        self.quiz_thread.stop()

    # 현재 학습 정보(비디오 이름) 저장
    def setCurrentAction(self, learnActionCategory):
        self.currentLearnAction = self.randomActions[learnActionCategory]

    # 랜덤 액션 세팅
    def setRandomAction(self):
        self.randomActions['hobby'] = str(random.choice(self.actions['hobby']))
        self.randomActions['character'] = str(random.choice(self.actions['character']))
        self.randomActions['family'] = str(random.choice(self.actions['family']))
    def hintBtnClickEvent(self):
        if self.isRun == True:
            self.stopVideo()
            self.sign_video.setVisible(False)
        else:
            self.showVideo()
            self.sign_video.setVisible(True)

    def refreshBtnClickEvent(self):
        self.setRandomAction()
        self.setCurrentAction('hobby')
        self.quiz_thread.category = 'hobby'
        self.quiz_thread.setActionNames(self.randomActions)
        self.quiz_thread.currentVdiName= self.randomActions['hobby']
        self.reloadText()
        self.showVideo()

    def nextStep(self):
        if self.quiz_thread.category == 'hobby':
            self.setCurrentAction('character')
            self.quiz_thread.category = 'character'
            # self.quiz_thread.setActionNames(self.randomActions)
            self.showVideo()
        elif self.quiz_thread.category == 'character':
            self.setCurrentAction('family')
            self.quiz_thread.category = 'family'
            # self.quiz_thread.setActionNames(self.randomActions)
            self.showVideo()
        else:
            self.exitQuiz()

    def setCam(self):
        self.quiz_thread = QuizThread(self.widgets, self.nextStep)
        self.quiz_thread.setCurrentVdiName(self.currentLearnAction)
        self.quiz_thread.change_pixmap_signal.connect(self.update_webcam_image)
        self.webcam.setScaledContents(True)

    def showVideo(self):
        self.setVideo()
        self.startVideo()

    def setVideo(self):
        if self.isRun == True:
            self.stopVideo()
        self.video_path = self.current_dir + self.prefix + self.currentLearnAction + self.suffix
        self.vid_thread = VideoThread()
        self.vid_thread.setVideoPath(self.video_path)
        self.vid_thread.change_pixmap_signal.connect(self.update_vid_image)
        self.sign_video.setScaledContents(True)

    def stopVideo(self):
        self.isRun = False
        self.sign_video.setVisible(False)
        self.vid_thread.stop()

    def startVideo(self):
        self.isRun = True
        self.sign_video.setVisible(True)
        self.vid_thread.start()

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

    def startQuiz(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(self.interval)

    def update_label(self):
        if self.current_text_index < len(self.text):
            self.widgets.label_about_game.setText(self.text[:self.current_text_index + 1])
            self.current_text_index += 1
        else:
            self.current_text_index = 0
            self.timer.stop()
