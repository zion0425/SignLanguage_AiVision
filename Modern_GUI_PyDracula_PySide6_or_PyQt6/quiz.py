import os
import random

import cv2
import numpy as np
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QStringListModel, Slot, QSortFilterProxyModel, QTimer
from PySide6.QtGui import QPixmap


class Quiz():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    prefix = '/videos/'
    suffix = '.mp4'
    isRun = False
    currentLearnAction = ''

    def __init__(self, widgets):
        self.widgets = widgets
        self.text = self.widgets.label_about_game.text()
        self.current_text_index = 0
        self.interval = 100 # 글자 간의 표시되는 간격을 조절하기 위한 시간 간격 (밀리초 단위)

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
