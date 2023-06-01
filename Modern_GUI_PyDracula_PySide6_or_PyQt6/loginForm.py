import json
import sys
import os

# IMPORT MODULES
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal
from userManagement import Login, Signup

# Main Window Class
class LoginClass(QObject):
    def __init__(self):
        QObject.__init__(self)

    ## Debuging Static User And Pass
    # staticUser = "wanderson"
    # staticPass = "123456"

    # Signals To Send Data
    signalUser = Signal(str)
    signalPass = Signal(str)
    signalLogin = Signal(str)

    # Function To Check Login
    @Slot(str, str)
    def checkLogin(self, getUser, getPass):
        print(getUser)
        if  (getUser == "" or getPass == "") :
            self.signalLogin.emit("empty_EditText")
            print("empty Form!")
        elif(Login.login(getUser, getPass)) :
            # Send
            self.signalUser.emit("Username: " + getUser)
            self.signalPass.emit("Password: " + getPass)
            self.signalLogin.emit("True")
        else:
            # Send Login Signal
            self.signalLogin.emit("False")
            print("Login error!")

class SignupClass(QObject):
    def __init__(self):
        QObject.__init__(self)

    # Signals To Send Data
    signalUser = Signal(str)
    signalPass = Signal(str)
    signalPassCheck = Signal(str)
    signalNickname = Signal(str)
    signalSignup = Signal(str)

    # Function To Check Signup
    @Slot(str, str, str, str)
    def checkSignup(self, email, getPass, getPassCheck, getNickName):
        print("signup")
        if  (email == "" or getPass == "" or getNickName == "") :
            self.signalSignup.emit("empty_EditText")
            print("Empty Form!")
        elif (getPass != getPassCheck):
            self.signalSignup.emit("password_not_match")
            print("Password Not Match!")
        elif (len(getPass) < 6) :
            self.signalSignup.emit("password_short")
            print("Password Too Short!")
        elif (Signup.isEmail(email) == False) :
            self.signalSignup.emit("email_not_valid")
            print("Email Not Valid!")
        elif (Signup.dupEmail(email)) :
            self.signalSignup.emit("email_dup")
            print("Email Duplication!")
        else:
            str = '{"email":"' + email + '", "password":"' + getPass + '", "nickname":"' + getNickName + '"}'
            print("str ="+str)
            jsonStr = json.loads(str)
            if(Signup.signup(jsonStr)) :
                # Send
                self.signalUser.emit("Email: " + email)
                self.signalPass.emit("Password: " + getPass)
                self.signalNickname.emit("Nickname: " + getNickName)
                self.signalSignup.emit("True")
            else:
                # Send Login Signal
                self.signalSignup.emit("False")
                print("Login error!")



# INSTACE CLASS
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    loginClass = LoginClass()
    signupClass = SignupClass()

    engine.rootContext().setContextProperty("loginBackend", loginClass)
    engine.rootContext().setContextProperty("signupBackend", signupClass)

    # Load QML File
    engine.load("qml/loginForm.qml")
    # Check Exit App
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
