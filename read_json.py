import json
import re
import shutil

# 파일명이 1501~3000으로 넘버링 되어있어 반복문에서 사용할 리스트
target1 = list(range(1501,3001))

# 수어동작별 morpheme데이터를 json에서 읽기 위한 경로
str1 = '/Users/sunukkim/Downloads/sign-language-video/1.Training/morpheme/07/NIA_SL_WORD'
str2 = '_REAL07_F_morpheme.json'

# 수어의 모든 동작 1500개 단어 저장 파일경로
# out_f = open('/Users/sunukkim/PycharmProjects/sign_language_AIVision/sign_words.txt', 'w')

# 선정한 30개 동작을 txt로 저장
selected_sign_lang = open('/Users/sunukkim/PycharmProjects/sign_language_AIVision/selected_sign_lang.txt', 'w')

# 선정한 30개 단어 list
sign_list = ['이십', '이십일', '이십이', '이십삼', '이십사', '이십오', '이십육', '이십칠', '이십팔', '이십구'
             , '권투', '낚시', '마라톤', '노래', '수영', '테니스', '야구',
             '조용하다', '똑똑하다', '귀엽다', '솔직하다', '수다스럽다',
             '친모', '친부', '여동생', '누나', '오빠', '할머니', '할아버지', '형']

# 비디오가 저장되어있는 경로
src1 = '/Users/sunukkim/Downloads/sign-language-video/1.Training/07/NIA_SL_WORD'
src2 = '_REAL07_F.mp4'

# 선정한 수어동작 30개를 저장할 경로
dst = '/Users/sunukkim/PycharmProjects/sign_language_AIVision/sign_lang_video/'

# 1501~3000까지 반복
for num in target1:

    # 4자리 숫자로 format 지정 ex) 4 -> 0004
    target = format(num, '04')
    #print(target)

    # json파일 읽는 코드
    with open(str1 + target + str2) as f:
        json_data = json.load(f)
        #print(json.dumps(json_data, ensure_ascii=False))
        file_name = json_data["metaData"]["name"]
        sign_name = json_data["data"][0]["attributes"][0]["name"]

        # 모든 수어 동작을 sign_words에 저장
        # out_f.write("%s\n"%sign_name)

        # file_name과 sign_name을 확인
        #print(file_name)
        print(sign_name)

        # 비디오 데이터가 위치한 경로
        src = src1 + target + src2

        # dst에 저장된 경로에 수어동작 비디오 복사 format: (수어동작명).mp4
        for sign in sign_list:
            if sign == sign_name:
                shutil.copyfile(src, dst + sign_name + '.mp4')

                # 선택된 수어 동작들 txt파일에 작성
                selected_sign_lang.write('%s\n'%sign_name)