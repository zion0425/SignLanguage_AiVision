import json

from userManagement import *

if __name__ == '__main__':
    print("Main")

    # # Login Debugging
    # Login.login("123545jkkkk@asdf.com", "asdfasdf")
    #
    # # Signup, insertDB Debugging
    # str = '{"email":"tdr@gmail.com.com", "password":"asdfasdf", "nickname":"kimsion"}'
    # Signup.signup(json.loads(str))
    #
    # # SelectDB Debugging (get nickname) + with login
    # Login.login("123545jkkkk@asdf.com", "asdfasdf")
    # uid = auth.current_user['localId']
    # CRUD.selectJson(uid, "nickname")
    #
    # # Check login + with login
    # Login.login("123545jkkkk@asdf.com", "asdfasdf")
    # print ("로그인 되어 있습니다. " if Login.isLogin() else "로그인 되어 있지 않습니다.")
