from PySide6.QtCore import Signal, Slot, Qt, QThread
import cv2
import numpy as np

class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)

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