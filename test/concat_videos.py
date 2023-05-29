from moviepy.editor import VideoFileClip, concatenate_videoclips

# 선정한 30개 단어 list
sign_list = ['이십', '이십일', '이십이', '이십삼', '이십사', '이십오', '이십육', '이십칠', '이십팔', '이십구'
             , '권투', '낚시', '마라톤', '노래', '수영', '테니스', '야구',
             '조용하다', '똑똑하다', '귀엽다', '솔직하다', '수다스럽다',
             '친모', '친부', '여동생', '누나', '오빠', '할머니', '할아버지', '형']
vid_angle_scr = ['D','F','L','R','U']

path = "/Users/sunukkim/PycharmProjects/sign_language_AIVision/sign_lang_video/"
# 이어붙일 비디오 파일의 경로를 리스트로 저장합니다.
video_files = []

for sign in sign_list:
    for angle in vid_angle_scr:
        str = path + sign + '_' + angle + '.mp4'
        video_files.append(str)
    print(video_files)

    clips = [VideoFileClip(file) for file in video_files]

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("/Users/sunukkim/PycharmProjects/sign_language_AIVision/mixed_videos/" + sign + "_concat.mp4")
    video_files = []
    # print(sign)



# # 비디오 파일들을 VideoFileClip 객체로 변환합니다.
# clips = [VideoFileClip(file) for file in video_files]
#
# # 비디오 파일들을 이어붙입니다.
# final_clip = concatenate_videoclips(clips)
#
# # 결과를 저장합니다.
# final_clip.write_videofile("result.mp4")
