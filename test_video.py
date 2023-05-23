import time
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
from PyQt5.uic import loadUi
from tensorflow.keras.models import load_model
import mediapipe as mp
from PIL import ImageFont, ImageDraw, Image


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture('videos/권투.mp4')
        # cap = cv2.VideoCapture(0)

        # 영상의 FPS 정보 가져오기
        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = int(1000 / fps)  # 재생 주기(ms)

        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
            else:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 영상이 끝나면 다시 처음으로 돌아감

            # 재생 주기만큼 대기
            cv2.waitKey(delay)

        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

actions = ['일본어', '솔직하다', '오빠', '할아버지', '어른', '물놀이', '고리타분', '마라톤', '테니스', '영어', '조용하다', '수영', '특기', '형', '낚시', '똑똑하다', '수다스럽다', '노인', '청소년', '할머니', '청년', '계획적', '귀엽다', '야구', '친부', '독특', '친모', '긍정적', '누나', '한국인', '엉뚱', '없다', '권투', '여동생', '노래', '한국어']

seq_length = 30
model = load_model('models/fourth_model.h5')
# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

#한글 폰트 경로 지정
fontpath = "/usr/local/share/fonts/NanumFont/NanumGothicBold.ttf"
# fontpath = "AppleGothic.ttf"
font = ImageFont.truetype(fontpath,40, encoding='unic')

class WebCamThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def put_korean_text(self, image, text, position):
        font_size = 50
        font = ImageFont.truetype(fontpath, font_size, encoding='unic')
        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)
        draw.text(position, text, font=font, fill=(255, 255, 255))
        image = np.array(img_pil)
        return image

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        # cap = cv2.VideoCapture('videos/권투.mp4')
        cap = cv2.VideoCapture(0)

        # 영상의 FPS 정보 가져오기
        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = int(1000 / fps)  # 재생 주기(ms)

        seq = []
        action_seq = []
        action_start_time = None

        while self._run_flag:
            ret, img = cap.read()
            if ret:
                img = img.copy()

                img = cv2.flip(img, 1)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                result = hands.process(img)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                if result.multi_hand_landmarks is not None:
                    for res in result.multi_hand_landmarks:
                        joint = np.zeros((21, 4))
                        for j, lm in enumerate(res.landmark):
                            joint[j] = [lm.x, lm.y, lm.z, lm.visibility]

                        # Compute angles between joints
                        v1 = joint[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19],
                             :3]  # Parent joint
                        v2 = joint[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                             :3]  # Child joint
                        v = v2 - v1  # [20, 3]
                        # Normalize v
                        v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                        # Get angle using arcos of dot product
                        angle = np.arccos(np.einsum('nt,nt->n',
                                                    v[[0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18], :],
                                                    v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19],
                                                    :]))  # [15,]

                        angle = np.degrees(angle)  # Convert radian to degree

                        d = np.concatenate([joint.flatten(), angle])

                        seq.append(d)

                        mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

                        if len(seq) < seq_length:
                            continue

                        input_data = np.expand_dims(np.array(seq[-seq_length:], dtype=np.float32), axis=0)

                        y_pred = model.predict(input_data).squeeze()

                        i_pred = int(np.argmax(y_pred))
                        conf = y_pred[i_pred]

                        if conf < 0.9:
                            continue

                        action = actions[i_pred]
                        action_seq.append(action)

                        if len(action_seq) < 3:
                            action_start_time = None
                            continue

                        this_action = '?'
                        if action_seq[-1] == action_seq[-2] == action_seq[-3]:
                            if action_start_time is None:
                                action_start_time = time.time()
                            elif time.time() - action_start_time >= 3:
                                this_action = action
                                print(this_action)
                                action_start_time = None

                        # Put Korean text
                        position = (int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20))

                        img = self.put_korean_text(img, this_action.upper(), position)

                # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                self.change_pixmap_signal.emit(img)
            else:
                print("cannot read frame.")
                break
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi('ui/prac_sign.ui', self)  # UI 파일의 경로로 변경해야 합니다.

        self.icon_btn.setStyleSheet('border-image: url(ui/img/ESL_logo_small2.png);')
        self.user_icon_btn.setStyleSheet('border-image: url(ui/img/user3.png);')

        self.setWindowTitle("권투 학습하기")

        # create the label that holds the image
        self.sign_video = self.findChild(QLabel, 'sign_video')

        # webcam을 보여줄 label
        self.webcam = self.findChild(QLabel, 'webcam')

        # create the video capture thread
        self.vid_thread = VideoThread()
        # connect its signal to the update_image slot
        self.vid_thread.change_pixmap_signal.connect(self.update_vid_image)
        # start the thread
        self.vid_thread.start()

        self.webcam_thread = WebCamThread()
        self.webcam_thread.change_pixmap_signal.connect(self.update_webcam_image)
        self.webcam_thread.start()

    def closeEvent(self, event):
        self.vid_thread.stop()
        self.webcam_thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_vid_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.sign_video.setPixmap(qt_img)

    @pyqtSlot(np.ndarray)
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
        p = convert_to_Qt_format.scaled(self.sign_video.width(), self.sign_video.height(), Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())