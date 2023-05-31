from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QAbstractItemView


def dictionary(widgets):
    model = QStringListModel()
    actions = ['일본어', '솔직하다', '오빠', '할아버지', '어른', '물놀이', '고리타분', '마라톤', '테니스', '영어', '조용하다', '수영', '특기', '형', '낚시',
               '똑똑하다', '수다스럽다', '노인', '청소년', '할머니', '청년', '계획적', '귀엽다', '야구', '친부', '독특', '친모', '긍정적', '누나', '한국인',
               '엉뚱', '없다', '권투', '여동생', '노래', '한국어']
    model.setStringList(actions)
    widgets.sign_word_list.setModel(model)
    widgets.sign_word_list.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def handle_item_clicked(index):
        clicked_item = index.data()
        print("클릭된 항목:", clicked_item)
        widgets.sign_word_info.setText('해당 수어는 "' + clicked_item + '" 입니다.')

    widgets.sign_word_list.clicked.connect(handle_item_clicked)
