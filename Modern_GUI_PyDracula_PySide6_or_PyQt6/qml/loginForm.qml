import QtQuick 6
import QtQuick.Window 2.15
import QtQuick.Controls 6
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window
    width: 400
    height: 580
    visible: true
    title: qsTr("Login Page")

    // SET FLAGS
    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowTitleHint

    // SET MATERIAL STYLE
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    // CREATE TOP BAR
    Rectangle{

        id: topBar
        height: 40
        color: Material.color(Material.Red)
        anchors{
            left: parent.left
            right: parent.right

            top: parent.top
            margins: 10
        }
        Behavior on opacity {
            SequentialAnimation {
                PropertyAnimation {
                    target: topBar
                    property: "opacity"
                    to: 1
                    duration: 500 // 페이드 인 애니메이션 지속 시간 (밀리초)
                }
                PauseAnimation {
                    duration: 2000 // 페이드 인 후 일정 시간 동안 대기 (밀리초)
                }
                PropertyAnimation {
                    target: topBar
                    property: "opacity"
                    to: 0
                    duration: 500 // 페이드 아웃 애니메이션 지속 시간 (밀리초)
                }
            }
        }

        Component.onCompleted: {
            // 초기에 페이드 아웃 상태로 설정
            opacity = 0
        }
        radius: 10
        opacity: 0
        Text{
            id: topBarText
            text: qsTr("Invalid username or password")
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            color: "#ffffff"
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 13

        }

    }
    // IMAGE IMPORT
    Image{
        id: image
        width: 250
        height: 200
        source: "../images/ESL_logo.png"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: topBar.bottom
        anchors.topMargin: 40
    }

    // TEXT FIELD USERNAME
    TextField{
        id: usernameField
        width: 300
        text: qsTr("")
        selectByMouse: true
        placeholderText: qsTr("Your email")
        verticalAlignment: Text.AlignVCenter
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: image.bottom
        anchors.topMargin: 60
    }

    // TEXT FIELD USERNAME
    TextField{
        id: passwordField
        width: 300
        text: qsTr("")
        selectByMouse: true
        placeholderText: qsTr("Your password")
        verticalAlignment: Text.AlignVCenter
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: usernameField.bottom
        anchors.topMargin: 10
        echoMode: TextInput.Password
    }

    // TEXT SIGNUP
    Text{
        id: signupText
        text: qsTr("회원가입")
        anchors.top: buttonLogin.bottom
        anchors.left: parent.left
        anchors.leftMargin: 50
        anchors.topMargin: 10
        color: "#A5A5A5"
        font.pointSize: 13
        MouseArea{
            hoverEnabled: true
            anchors.fill: signupText
            onClicked: {
                var component = Qt.createComponent("signupForm.qml")
                var win = component.createObject()
                window.visible = false
                win.show()
            }
            onEntered: {
                // 호버영역에 진입
                signupText.color = "#ffffff";
            }

            onExited: {
                // 호버영역 이탈
                signupText.color = "#A5A5A5";
            }
        }
        // 언더바 세팅
//       Rectangle {
//            width: parent.width
//            height: 1
//            color: Material.Pink
//            anchors.bottom: parent.bottom
//        }
    }

    //Text search password/email
    Text{
        id: searchInfo
        text: qsTr("이메일/비밀번호 찾기")
        anchors.top: buttonLogin.bottom
        anchors.right: parent.right
        anchors.rightMargin: 50
        anchors.topMargin: 10
        color: "#A5A5A5"
        font.pointSize: 13
        MouseArea{
            anchors.fill: searchInfo
            hoverEnabled: true
            onClicked: {
                var component = Qt.createComponent("searchInfo.qml")
                var win = component.createObject()
                win.show()
                window.visible = false
            }
            onEntered: {
                // 호버에 진입
                searchInfo.color = "#ffffff";
            }

            onExited: {
                // 호버에 이탈
                searchInfo.color = "#A5A5A5";
            }
        // 언더바 세팅
//       Rectangle {
//            width: parent.width
//            height: 1
//            color: Material.Pink
//            anchors.bottom: parent.bottom
//        }
        }
    }

    // BUTTON LOGIN
    Button{
        id: buttonLogin
        width: 300
        height : 52
        text: qsTr("Login")
        highlighted: true

//        Material.background: "#44D134"
        Material.background: Material.Blue
        anchors.top: passwordField.bottom

        anchors.topMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked: {
            loginBackend.checkLogin(usernameField.text, passwordField.text);
            topBar.opacity = 1;
        }
    }

    Connections {
        target: loginBackend

        // CUSTOM PROPERTIES
        property string username: ""
        property string password: ""
        function onSignalUser(myUser){ username = myUser }
        function onSignalPass(myPass){ password = myPass }

        // FUNTION OPEN NEW WINDOW (APP WINDOW)
        function onSignalLogin(loginStr) {
            if(loginStr == "True"){
                var component = Qt.createComponent("app.qml")
                var win = component.createObject()
                win.textUsername = username
                win.textPassword = password
                win.show()
                visible = false
            }else if (loginStr == "empty_EditText"){
                topBarText.text = qsTr("Empty email or password")
                print("?2")

                // CHANGE USER COLOR
//                    usernameField.Material.background = Material.Pink
//                    usernameField.Material.accent = Material.Pink
                usernameField.Material.underlineColor = Material.Pink
//                    passwordField.Material.accent = Material.Pink
//                    passwordField.Material.background = Material.Pink
                usernameField.Material.underlineColor = Material.Pink
            }else{
                topBarText.text = qsTr("Invalid User")
            }
        }
    }
}
