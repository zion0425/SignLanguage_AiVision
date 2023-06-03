import json

import userManagement as um
from userManagement import CRUD

def signup(jsonUserAccountData):
    # 사용자 이름, 비밀번호, 이메일을 가져와서 검증
    password = jsonUserAccountData['password']
    email = jsonUserAccountData['email']
    print(email)
    nickname = jsonUserAccountData['nickname']

    # 이메일과 비밀번호로 새로운 사용자 등록
    try:
        user = um.auth.create_user_with_email_and_password(email, password)
        str = '{"nickname" : "' + nickname + '"}'
        CRUD.insertJson(user['localId'], json.loads(str))
        print('회원가입 성공')
        # 회원가입 성공 시 수행할 작업을 여기에 작성합니다.
        return True
    except Exception as e :
        print('회원가입 실패 ' + e)
        return False

def isEmail(email):
    if '@' in email :
        return True
    else :
        return False

def dupEmail(email):
    try:
        if um.auth.get_account_info(email) :
            return True
        else :
            return False
    except Exception as e:
        return False