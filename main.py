from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QWidget 
from PyQt5.uic import loadUi
import json
import re



class LogSignWindow(QMainWindow):
    def __init__(self):
        super(LogSignWindow,self).__init__()
        loadUi("log-sign.ui",self)
        
        
        self.sign_result_label.hide()
        self.signup_pushButton.clicked.connect(self.sign_up)
        
    def sign_up(self):
        email = self.sign_email_lineEdit.text()
        password = self.sign_password_lineEdit.text()
        name = self.sign_name_lineEdit.text()
        surname = self.sign_surname_lineEdit.text()
        
        user_data = {
            "name": name,
            "surname":surname,
            "email": email,
            "password": password
            
        }

        with open("users.json", "a") as file:
            file.write(json.dumps(user_data) + '\n')
        
        self.sign_result_label.setText("Sign up succesfull!")
        self.sign_result_label.show()
    def log_in(self):

        email = self.log_email_lineEdit.text()
        password = self.log_password_lineEdit.text()
        
    def checkCredentials(self, email, password):
        try:
            with open("users.json", "r") as userFile:
                existing_data = json.load(userFile)
                for i in existing_data:
                    if i["email"] == email and i["password"] == password:
                        return True
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window= LogSignWindow()
    window.show()
    sys.exit(app.exec())
