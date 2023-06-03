import userManagement as um
def login(userId, userPassword):
    # 사용자 이름과 비밀번호를 가져와서 검증
    # USER 여부 -> uid 사용
    try:
        # firebase 로그인 로직
        um.auth.sign_in_with_email_and_password(userId, userPassword)
        #token
        # u_token = p_auth.create_custom_token(auth.get_user_by_email(username).uid)
        # p_auth.refresh(u_token)
        # print(firebase.auth().current_user)
        print("성공 ")
        return True
    except Exception as e:
        print("실패 시 에러 " + str(e))
        return False


# 로그인 여부 확인 , 토큰 체크 및 갱신
def isLogin():
    try :
        if (um.auth.current_user != None) :
            return True
        else :
            return False
    except Exception as e:
        return False

