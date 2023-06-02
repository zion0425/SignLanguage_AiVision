import os

import cv2
import numpy as np
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QStringListModel, Slot, QSortFilterProxyModel
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QAbstractItemView, QVBoxLayout

from Modern_GUI_PyDracula_PySide6_or_PyQt6.video_thread import VideoThread


class Dictionary():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    prefix = '/videos/'
    suffix = '.mp4'
    isRun = False
    def __init__(self, widgets):
        self.widgets = widgets
        model = QStringListModel()
        actions = ['일본어', '솔직하다', '오빠', '할아버지', '어른', '물놀이', '고리타분', '마라톤', '테니스', '영어', '조용하다', '수영', '특기', '형', '낚시',
                   '똑똑하다', '수다스럽다', '노인', '청소년', '할머니', '청년', '계획적', '귀엽다', '야구', '친부', '독특', '친모', '긍정적', '누나', '한국인',
                   '엉뚱', '없다', '권투', '여동생', '노래', '한국어']
        model.setStringList(actions)
        # 소스 모델과 필터 모델 설정
        self.source_model = model
        self.filter_model = QSortFilterProxyModel()
        self.filter_model.setSourceModel(self.source_model)

        # 리스트 뷰와 검색 필드 설정
        self.widgets.sign_word_list.setModel(self.filter_model)
        self.widgets.sign_word_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.search_field = self.widgets.search_sign
        self.search_field.textChanged.connect(self.filter_items)
        # 리스트 뷰에서 항목 클릭 시 동작
        self.widgets.sign_word_list.clicked.connect(self.handle_item_clicked)
        # 검색 버튼 클릭 시 검색 수행
        self.widgets.btn_search_sign.clicked.connect(self.handle_search_button)

    def handle_item_clicked(self, index):
        clicked_item = index.data()
        print("클릭된 항목:", clicked_item)
        self.widgets.sign_word_info.setText('해당 수어는 "' + clicked_item + '" 입니다.')
        self.videoName = self.current_dir + self.prefix + clicked_item + self.suffix
        if self.isRun:
            self.vid_thread.stop()
        self.initVideo(self.videoName, self.widgets.label_3)
        self.startVideo()
    def reloadingVdi(self, vName):
        self.videoName = self.current_dir + self.prefix + vName + self.suffix
        self.initVideo(self.videoName, self.widgets.sign_word_info)
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

