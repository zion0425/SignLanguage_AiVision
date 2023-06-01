import json

import userManagement as um

def insertJson(uid, data):
    try:
        um.db.child(uid).push(data)
        print("성공 ")

    except Exception as e:
        print("실패 시 에러 " + str(e))

def selectJson(uid, data):
    try:
        sel = um.db.child(uid).get().val().values()
        nickname = list(sel)[0][data]
        return nickname
    except Exception as e:
        print("실패 시 에러 " + str(e))

