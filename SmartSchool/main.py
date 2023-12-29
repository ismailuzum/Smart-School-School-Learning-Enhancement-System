import sys
import json
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi

# Utility Functions
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading users.json: {e}")
        return []

def save_users(users):
    try:
        with open('users.json', 'w') as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        print(f"Error saving to users.json: {e}")

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}[\]:;<>,.?/~\\-]).{8,}$"
    return re.match(pattern, password)

def is_valid_phone(phone):
    return re.match(r"^\+\d{1,3}\d{9}$", phone)

def is_admin(user):
    return user.get('type') == 'admin'

# Application Classes
class LoginApp(QDialog):
    def __init__(self):
        super(LoginApp, self).__init__()
        loadUi("login_form.ui", self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(self.show_reg)

    def login(self):
        email = self.tb1.text()
        password = self.tb2.text()

        users = load_users()
        user = next((user for user in users if user['email'] == email and user['password'] == password), None)

        if user:
            if is_admin(user):
                QMessageBox.information(self, "Login Output", "Admin Login Successful")
                # Here, add admin interface
            else:
                QMessageBox.information(self, "Login Output", "Login Successful")
        else:
            QMessageBox.warning(self, "Login Output", "Invalid email or password")

    def show_reg(self):
        widget.setCurrentIndex(1)

class RegApp(QDialog):
    def __init__(self):
        super(RegApp, self).__init__()
        loadUi("register_form.ui", self)
        self.b3.clicked.connect(self.reg)
        self.b3.clicked.connect(self.show_login)

    def reg(self):
        email = self.tb3.text()
        password = self.tb4.text()
        name = self.tb5.text()
        surname = self.tb6.text()
        phone = self.tb7.text()

        if not is_valid_email(email) or not is_valid_password(password) or not is_valid_phone(phone):
            QMessageBox.warning(self, "Registration Error", "Invalid input format")
            return

        users = load_users()
        if any(user['email'] == email for user in users):
            QMessageBox.warning(self, "Registration form", "User Already Exists!!")
        else:
            users.append({
                'email': email, 
                'password': password, 
                'name': name, 
                'surname': surname, 
                'phone': phone, 
                'type': 'student'  # Default type is 'student'
            })
            save_users(users)
            QMessageBox.information(self, "Registration form", "User Registered Successfully, YOU CAN NOW LOGIN!!")
            self.tb3.clear()
            self.tb4.clear()
            self.tb5.clear()
            self.tb6.clear()
            self.tb7.clear()

    def show_login(self):
        widget.setCurrentIndex(0)

# Main Application Setup
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login_form = LoginApp()
    registration_form = RegApp()
    widget.addWidget(login_form)
    widget.addWidget(registration_form)
    widget.setCurrentIndex(0)
    widget.setFixedWidth(400)
    widget.setFixedHeight(500)
    widget.show()

    sys.exit(app.exec_())
