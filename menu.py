import sys

from PyQt5.QtWidgets import *
import json
import register
import main

app = QApplication([])
main_win = QWidget()
app.setApplicationName("Login")

main_Vline = QVBoxLayout()
btn_line = QHBoxLayout()


loginText = QLabel("Login:")
passwordText = QLabel("Password:")
loginEdit = QLineEdit()
passwordEdit = QLineEdit()
loginBtn = QPushButton("Login")
signBtn = QPushButton("Sign Up")
cancelBtn = QPushButton("Cancel")

main_Vline.addWidget(loginText)
main_Vline.addWidget(loginEdit)

main_Vline.addWidget(passwordText)
main_Vline.addWidget(passwordEdit)

btn_line.addWidget(loginBtn)
btn_line.addWidget(signBtn)
btn_line.addWidget(cancelBtn)






def ClickReg ():
    register.RegisterWindow()

def CloseApp():
    app.exit()



def loginGame():
    with open("data.json" ,'r' , encoding='utf8') as file:
        jsonD = json.load(file) 
    login = loginEdit.text()
    password = passwordEdit.text()

    if login in jsonD:
        if password == jsonD[login]['password']:
            main.game()
    else:
        print("No")
        sys.exit()

signBtn.clicked.connect(ClickReg)
cancelBtn.clicked.connect(CloseApp)
loginBtn.clicked.connect(loginGame)
main_Vline.addLayout(btn_line)
main_win.setLayout(main_Vline)

main_win.show()
app.exec_()