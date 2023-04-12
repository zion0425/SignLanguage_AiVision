import cv2

# 7초 동안 재생될 영상 파일 경로
video_file_path = "./sign_language_video/NIA_SL_WORD0004_SYN01_D.mp4"

# 비디오 파일 열기
video = cv2.VideoCapture(video_file_path)

# 비디오 프레임 수 가져오기
fps = int(video.get(cv2.CAP_PROP_FPS))

# 비디오 크기 가져오기
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 출력 비디오 파일 경로
output_file_path = "output3.mp4"

# 비디오 무한반복 옵션 설정
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_video = cv2.VideoWriter(output_file_path, fourcc, fps, (width, height))

# 비디오 30초 반복
for i in range(fps*30):
    ret, frame = video.read()
    if not ret:
        # 비디오 재생이 끝나면 다시 처음부터 재생
        video.release()
        video = cv2.VideoCapture(video_file_path)
        ret, frame = video.read()
    # 출력 비디오에 프레임 쓰기
    output_video.write(frame)


# 비디오 파일 닫기
video.release()
output_video.release()
cv2.destroyAllWindows()
