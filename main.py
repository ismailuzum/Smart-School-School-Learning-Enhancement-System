from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import json
import re

class LogSignWindow(QMainWindow):
    def __init__(self):
        super(LogSignWindow, self).__init__()
        loadUi("log-sign.ui", self)
        
        self.sign_result_label.hide()
        self.signup_pushButton.clicked.connect(self.sign_up)
        
    def sign_up(self):
        email = self.sign_email_lineEdit.text()
        password = self.sign_password_lineEdit.text()
        name = self.sign_name_lineEdit.text()
        surname = self.sign_surname_lineEdit.text()
        
        if self.emailValidator(email) and self.passwordValidator(password):
            user_data = {
                "name": name,
                "surname": surname,
                "email": email,
                "password": password
            }

            with open("users.json", "a") as file:
                file.write(json.dumps(user_data) + '\n')

            self.sign_result_label.setText("Sign up successful!")
            self.sign_result_label.show()
        else:
            print("Invalid email or password format")
        
    @staticmethod
    def emailValidator(email):
        try:
            with open("users.json", "r") as userFile:
                existing_data = json.load(userFile)
                for i in existing_data:
                    if i[2] == email:
                        print("There is an account matched with this email")
                        return False
        except (json.JSONDecodeError, FileNotFoundError):
            pass

        pattern = r"^([a-zA-Z0-9_.+-]+)@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$"

        if re.match(pattern, email):
            return True
        else:
            print("Wrong format")
            return False

    @staticmethod
    def passwordValidator(password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}[\]:;<>,.?/~\\-]).{8,}$"
        return re.match(pattern, password)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = LogSignWindow()
    window.show()
    sys.exit(app.exec())
