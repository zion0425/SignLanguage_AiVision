import cv2
import mediapipe as mp
import numpy as np
import time, os
from pathlib import Path

actions = []

video_file_path = '/Users/sunukkim/PycharmProjects/sign_language_AIVision/videos'
for file in Path(video_file_path).iterdir():
    print(file.stem)
    actions.append(file.stem)

seq_length = 30
secs_for_action = 30

# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

created_time = int(time.time())
os.makedirs('dataset', exist_ok=True)

for action in actions:
    data = []
    full_seq_data = []

    # Get video files
    video_files = [f for f in os.listdir('videos') if f.endswith('.mp4') and f.startswith(action)]
    for video_file in video_files:
        cap = cv2.VideoCapture(os.path.join('videos', video_file))

        while cap.isOpened():
            ret, img = cap.read()

            if not ret:
                break

            #img = cv2.flip(img, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = hands.process(img)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            if result.multi_hand_landmarks is not None:
                for res in result.multi_hand_landmarks:
                    joint = np.zeros((21, 4))
                    for j, lm in enumerate(res.landmark):
                        joint[j] = [lm.x, lm.y, lm.z, lm.visibility]

                    # Compute angles between joints
                    v1 = joint[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19], :3]  # Parent joint
                    v2 = joint[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                         :3]  # Child joint
                    v = v2 - v1  # [20, 3]
                    # Normalize v
                    v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                    # Get angle using arcos of dot product
                    angle = np.arccos(np.einsum('nt,nt->n',
                                                v[[0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18], :],
                                                v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19], :]))  # [15,]

                    angle = np.degrees(angle)  # Convert radian to degree

                    angle_label = np.array([angle], dtype=np.float32)
                    angle_label = np.append(angle_label, actions.index(action))

                    d = np.concatenate([joint.flatten(), angle_label])

                    data.append(d)

                    mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('img', img)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()

    data = np.array(data)
    print(action, data.shape)
    np.save(os.path.join('dataset', f'raw_{action}_{created_time}'), data)

    # Create sequence data
    full_seq_data = []
    for seq in range(len(data) - seq_length):
        full_seq_data.append(data[seq:seq + seq_length])

    full_seq_data = np.array(full_seq_data)
    print(action, full_seq_data.shape)
    np.save(os.path.join('dataset', f'seq_{action}_{created_time}'), full_seq_data)



