import json

target1 = list(range(1501,3001))

str1 = '/Users/sunukkim/Downloads/sign-language-video/1.Training/morpheme/07/NIA_SL_WORD'
str2 = '_REAL07_F_morpheme.json'
out_f = open('/Users/sunukkim/PycharmProjects/gesture-recognition/sign_words.txt', 'w')

for num in target1:
    target = format(num, '04')
    #print(target)

    with open(str1 + target + str2) as f:
        json_data = json.load(f)
        #print(json.dumps(json_data, ensure_ascii=False))
        #file_name = json_data["metaData"]["name"]
        sign_name = json_data["data"][0]["attributes"][0]["name"]
        out_f.write("%s\n"%sign_name)
        #print(file_name)
        print(sign_name)

"""
1. 자라다(1542) - 2. 키우다(1507) - 3. 노부모(2125) - 4. 여동생(1518) - 5. 누나(1516)
6. 상처(1519)- 7. 그립ㄹ(1506) - 8. 관계(1584) - 9. 이별 - 10. 아픔
11. 회복 - 12. 울음 - 13. 위로 - 14. 성장 - 15. 자신감
16. 믿음 - 17. 도전 - 18. 꿈 - 19. 열정 - 20. 목표
21. 성취 - 22. 지지 - 23. 도움 - 24. 용기 - 25. 희생
26. 가치 - 27. 자기계발 - 28. 인생 - 29. 경험 - 30. 노력
"""

'''
while target1 < 1001:
    target = format(target1, '04')
    #print(target)
    target1 += 1

    with open(str1 + target + str2) as f:
        json_data = json.load(f)
    #print(json.dumps(json_data, ensure_ascii=False))
    file_name = json_data["metaData"]["name"]
    sign_name = json_data["data"][0]["attributes"][0]
    print(file_name)
    print(sign_name)
'''