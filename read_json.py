import json
import re
import shutil

target1 = list(range(1501,3001))

str1 = '/Users/sunukkim/Downloads/sign-language-video/1.Training/morpheme/07/NIA_SL_WORD'
str2 = '_REAL07_F_morpheme.json'
out_f = open('/Users/sunukkim/PycharmProjects/gesture-recognition/sign_words.txt', 'w')
sign_list = ['이십', '이십일', '이십이', '이십삼', '이십사', '이십오', '이십육', '이십칠', '이십팔', '이십구'
             , '권투', '낚시', '마라톤', '노래', '수영', '테니스', '야구',
             '조용하다', '똑똑하다', '귀엽다', '솔직하다', '수다스럽다',
             '친모', '친부', '여동생', '누나', '오빠', '할머니', '할아버지']

src1 = '/Users/sunukkim/Downloads/sign-language-video/1.Training/07/NIA_SL_WORD'
src2 = '_REAL07_F.mp4'
dst = '/Users/sunukkim/PycharmProjects/sign_language_AIVision/sign_lang_video/'

#res_list = ["이십", "0"]

for num in target1:
    target = format(num, '04')
    #print(target)

    with open(str1 + target + str2) as f:
        json_data = json.load(f)
        #print(json.dumps(json_data, ensure_ascii=False))
        file_name = json_data["metaData"]["name"]
        sign_name = json_data["data"][0]["attributes"][0]["name"]
        out_f.write("%s\n"%sign_name)
        #print(file_name)

        src = src1 + target + src2

        for sign in sign_list:
            if sign == sign_name:
                shutil.copy(src, dst)