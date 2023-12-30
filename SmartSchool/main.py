import sys
import json
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi

# Utility functions
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
class AdminApp(QMainWindow):
    def __init__(self):
        super(AdminApp, self).__init__()
        loadUi("admin.ui", self)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.menu11.triggered.connect(self.add_teacher_tab)
        self.menu12.triggered.connect(self.edit_teacher_tab)
        self.menu71.triggered.connect(self.close)             #logout from admin menu

        self.b5.clicked.connect(self.handle_teacher_registration)

    def add_teacher_tab(self):
        self.tabWidget.setCurrentIndex(1)
        self.fill_teacherID()

    def fill_teacherID(self):
        try:
            with open("users.json", "r") as userFile:
                data = json.load(userFile)
                teacherID = 0
                for item in data:
                    if item.get('type') == 'teacher':
                        teacherID += 1
                self.tb11.setText(str(teacherID+1))
        except FileNotFoundError:
            print("File not found: users.json")
            return []
        except Exception as e:
            print(f"Error loading users.json: {e}")
            return []

    def handle_teacher_registration(self):
        # Attempt to register the first teacher
        self.register_teacher()

    def ask_to_register_another(self):
        reply = QMessageBox.question(self, 'Register Another Teacher',
                                     'Do you want to register another teacher?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.add_teacher_tab()  # Prepare the form for a new entry
        else:
            self.close()  # Close the AdminApp window

    def register_teacher(self):
        if self.save_teacher_details():
            self.clear_form_fields()
            self.ask_to_register_another()

    def save_teacher_details(self):
        # Extracting field values
        teacherId = self.tb11.text()
        email = self.tb12.text()
        password = self.tb17.text()
        name = self.tb13.text()
        surname = self.tb14.text()
        gender = self.cb11.currentText()
        date_of_birth = self.tb15.text()
        phone = self.tb16.text()

        # Validations
        if not is_valid_email(email) or not is_valid_password(password) or not is_valid_phone(phone):
            return False

        users = load_users()
        if any(user['email'] == email for user in users):
            QMessageBox.warning(self, "Registration form", "User Already Exists!!")
            return False
        else:
            users.append({
                'teacherId': teacherId,
                'email': email,
                'password': password,
                'name': name,
                'surname': surname,
                'gender': gender,
                'date_of_birth': date_of_birth,
                'phone': phone,
                'type': 'teacher'
            })
            save_users(users)
            QMessageBox.information(self, "Registration form", "New Teacher Registered Successfully, HE/SHE CAN NOW LOGIN!!")
            return True


    def save_teacher_details(self):
        teacherId = self.tb11.text()
        email = self.tb12.text()
        password = self.tb17.text()
        name = self.tb13.text()
        surname = self.tb14.text()
        gender = self.cb11.currentText()
        date_of_birth = self.tb15.text()
        phone = self.tb16.text()

        if not is_valid_email(email) or not is_valid_password(password) or not is_valid_phone(phone):
            QMessageBox.warning(self, "Registration Error", "Invalid input format")
            return False

        users = load_users()
        if any(user['email'] == email for user in users):
            QMessageBox.warning(self, "Registration form", "User Already Exists!!")
            return False
        else:
            users.append({
                'teacherId': teacherId,
                'email': email,
                'password': password,
                'name': name,
                'surname': surname,
                'gender': gender,
                'date_of_birth': date_of_birth,
                'phone': phone,
                'type': 'teacher'
            })
            save_users(users)
            QMessageBox.information(self, "Registration form", "New Teacher Registered Successfully, HE/SHE CAN NOW LOGIN!!")
            self.clear_form_fields()
            return True

    def clear_form_fields(self):
        self.tb11.clear()
        self.tb12.clear()
        self.tb17.clear()
        self.tb13.clear()
        self.tb14.clear()
        self.cb11.setCurrentIndex(0)
        self.tb15.clear()
        self.tb16.clear()

    def edit_teacher_tab(self):
        self.tabWidget.setCurrentIndex(2)

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
                self.admin_app = AdminApp()
                self.admin_app.show()
            else:
                QMessageBox.information(self, "Login Output", "Login Successful")
        else:
            QMessageBox.warning(self, "Login Output", "Invalid email or password")

    def show_reg(self):
        global widget
        widget.setCurrentIndex(1)

class RegApp(QDialog):
    def __init__(self):
        super(RegApp, self).__init__()
        loadUi("register_form.ui", self)
        self.b3.clicked.connect(self.reg)
        self.b4.clicked.connect(self.show_login)

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
                'type': 'student'
            })
            save_users(users)
            QMessageBox.information(self, "Registration form", "User Registered Successfully, YOU CAN NOW LOGIN!!")
            self.tb3.clear()
            self.tb4.clear()
            self.tb5.clear()
            self.tb6.clear()
            self.tb7.clear()

    def show_login(self):
        global widget
        widget.setCurrentIndex(0)

# Main Application Setup
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login_form = LoginApp()
    registration_form = RegApp()
    widget.addWidget(login_form)
    widget.addWidget(registration_form)
    widget.setFixedWidth(400)
    widget.setFixedHeight(500)
    widget.show()
    sys.exit(app.exec_())
