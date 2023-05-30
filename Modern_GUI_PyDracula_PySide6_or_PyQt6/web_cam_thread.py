import numpy as np
from tensorflow.keras.models import load_model
import mediapipe as mp
from PIL import ImageFont, ImageDraw, Image
from PySide6.QtCore import Signal, Slot, Qt, QThread, QFile
import cv2
import time
import os


#2차원 배열로 key : vdiName , value : vdiUrl
actions = ['일본어', '솔직하다', '오빠', '할아버지', '어른', '물놀이', '고리타분', '마라톤', '테니스', '영어', '조용하다', '수영', '특기', '형', '낚시', '똑똑하다', '수다스럽다', '노인', '청소년', '할머니', '청년', '계획적', '귀엽다', '야구', '친부', '독특', '친모', '긍정적', '누나', '한국인', '엉뚱', '없다', '권투', '여동생', '노래', '한국어']

seq_length = 30

current_dir = os.path.abspath(os.path.dirname(__file__))

model = load_model(current_dir+"/../models/fourth_model.h5")
# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

#한글 폰트 경로 지정
fontpath = "/Library/Fonts/NanumGothic.ttf"
# fontpath = "AppleGothic.ttf"
font = ImageFont.truetype(fontpath,40, encoding='unic')

class WebCamThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)

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
        cap = cv2.VideoCapture(0)

        # # 영상의 FPS 정보 가져오기
        # fps = cap.get(cv2.CAP_PROP_FPS)
        # delay = int(1000 / fps)  # 재생 주기(ms)

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