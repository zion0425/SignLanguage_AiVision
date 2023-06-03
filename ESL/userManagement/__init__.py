# firebase-admin 코드
#pip install firebase-admin

# import firebase_admin
# from firebase_admin import auth, credentials, db

# Firebase Admin SDK 초기화
# cred = credentials.Certificate("signlan-8f8c5-firebase-adminsdk-jf9io-4936fea47c.json")
# firebase_admin.initialize_app(cred, {
#     "databaseURL": "https://signlan-8f8c5-default-rtdb.firebaseio.com/"}
# )
# As an admin, the app has access to read and write all data, regradless of Security Rules
# ref = db.reference('restricted_access/secret_document')

#pip install pyrebase4
#pip install requests==2.18.4
#pip install requests-toolbelt==0.7.1

# Firebase --> with python 3.7
# pyrebase4
import pyrebase
from userManagement import Login, CRUD, Signup

# Firebase config
firebaseConfig = {
    "apiKey": "AIzaSyDaJsxcrwSU4pxvdy7dazFGhXx3xhu4XqU",
    "authDomain": "signlan-8f8c5.firebaseapp.com",
    "projectId": "signlan-8f8c5",
    "databaseURL": "https://signlan-8f8c5-default-rtdb.firebaseio.com/",
    "storageBucket": "signlan-8f8c5.appspot.com",
    "messagingSenderId": "998817743244",
    "appId": "1:998817743244:web:9f44c8369c324c767b96a9"
};

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
