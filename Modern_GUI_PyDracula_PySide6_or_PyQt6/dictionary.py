import cv2
import numpy as np
from PySide6 import QtGui
from PySide6.QtCore import QStringListModel, Slot, QSortFilterProxyModel
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QAbstractItemView

from Modern_GUI_PyDracula_PySide6_or_PyQt6.video_thread import VideoThread


def dictionary(widgets):
    model = QStringListModel()
    actions = ['일본어', '솔직하다', '오빠', '할아버지', '어른', '물놀이', '고리타분', '마라톤', '테니스', '영어', '조용하다', '수영', '특기', '형', '낚시',
               '똑똑하다', '수다스럽다', '노인', '청소년', '할머니', '청년', '계획적', '귀엽다', '야구', '친부', '독특', '친모', '긍정적', '누나', '한국인',
               '엉뚱', '없다', '권투', '여동생', '노래', '한국어']
    model.setStringList(actions)

    # 소스 모델과 필터 모델 설정
    source_model = model
    filter_model = QSortFilterProxyModel()
    filter_model.setSourceModel(source_model)

    # 리스트 뷰와 검색 필드 설정
    widgets.sign_word_list.setModel(filter_model)
    widgets.sign_word_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
    search_field = widgets.search_sign

    def handle_item_clicked(index):
        clicked_item = index.data()
        print("클릭된 항목:", clicked_item)
        widgets.sign_word_info.setText('해당 수어는 "' + clicked_item + '" 입니다.')
    def filter_items():
        search_text = search_field.text()
        filter_model.setFilterFixedString(search_text)

    def handle_search_button():
        filter_items()

    # 검색 필드의 텍스트 변경 시 필터링 적용
    search_field.textChanged.connect(filter_items)
    # 리스트 뷰에서 항목 클릭 시 동작
    widgets.sign_word_list.clicked.connect(handle_item_clicked)
    # 검색 버튼 클릭 시 검색 수행
    widgets.btn_search_sign.clicked.connect(handle_search_button)