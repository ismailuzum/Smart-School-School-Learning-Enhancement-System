import sys
import json
import re
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QComboBox, QPushButton, QDialog, QApplication, QMessageBox, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.uic import loadUi

#############################################################################################################

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

###############################################################################################################

def load_lessons():
        try:
            with open('lessons.json', 'r') as lessons_file:
                return json.load(lessons_file)
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error loading lessons.json: {e}")
            return []
        
def save_lessons(lessons):
        try:
            with open('lessons.json', 'w') as lessons_file:
                json.dump(lessons,lessons_file, indent=4)
        except Exception as e:
            print(f"Error saving to lessons.json: {e}")

###############################################################################################################

def load_attendance():
        try:
            with open('attendance.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Error loading attendance.json: {e}")
            return {}

def save_attendance(attendance_data):
        try:
            with open('attendance.json', 'w') as file:
                json.dump(attendance_data, file, indent=4)
        except Exception as e:
            print(f"Error saving to attendance.json: {e}")

###############################################################################################################

def load_meetings():
        try:
            with open('meetings.json', 'r') as meetings_file:
                return json.load(meetings_file)
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error loading meetings.json: {e}")
            return []
        
def save_meetings(meetings):
        try:
            with open('meetings.json', 'w') as meetings_file:
                json.dump(meetings, meetings_file, indent=4)
        except Exception as e:
            print(f"Error saving to meetings.json: {e}")

##############################################################################################################

def load_meeting_attendance():
        try:
            with open('meeting_attendance.json', 'r') as meeting_attendance_file:
                return json.load(meeting_attendance_file)
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Error loading meeting_attendance.json: {e}")
            return {}

def save_meeting_attendance(meeting_attendance_data):
        try:
            with open('meeting_attendance.json', 'w') as meeting_attendance_file:
                json.dump(meeting_attendance_data, meeting_attendance_file, indent=4)
        except Exception as e:
            print(f"Error saving to meeting_attendance.json: {e}")

###############################################################################################################
def load_announcements():
    try:
        with open('announcements.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_announcements(announcements):
    with open('announcements.json', 'w') as file:
        json.dump(announcements, file, indent=4)
###############################################################################################################
def load_todolist():
    try:
        with open('todolist.json', 'r') as todolist_file:
            return json.load(todolist_file)
    except FileNotFoundError:
        return []

def save_todolist(todolists):
    with open('todolist.json', 'w') as todolist_file:
        json.dump(todolists, todolist_file, indent=4)
###############################################################################################################

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}[\]:;<>,.?/~\\-]).{8,}$"
    return re.match(pattern, password)

def is_valid_phone(phone):
    return re.match(r"^\+\d{1,3}\d{9}$", phone)

def is_admin(user):
    return user.get('type') == 'admin'

def is_student(user):
    return user.get('type') == 'student'

def is_teacher(user):
    return user.get('type') == 'teacher'

#############################################################################################################

# Application Classes
class AdminApp(QMainWindow):
    def __init__(self):
        super(AdminApp, self).__init__()
        loadUi("admin.ui", self)
        self.model = QStandardItemModel()
        self.email = email
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.menu11.triggered.connect(self.add_teacher_tab)
        self.menu12.triggered.connect(self.edit_teacher_tab)
        self.menu71.triggered.connect(self.close)  # Logout from admin menu
        self.b5.clicked.connect(self.handle_teacher_registration)
        self.cb21.currentIndexChanged.connect(self.on_teacher_selected)

        self.menu61_a.triggered.connect(self.add_message_tab)
        self.messages = dict()
        self.getMessages()
        self.load_users()
        self.sendButton1.clicked.connect(self.send_message)
        #self.comboBox_a.currentIndexChanged.connect(self.messageSelected)
        self.listView_4_a.clicked.connect(self.read_message)


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
        if self.save_teacher_details():
            self.clear_form_fields()
            self.ask_to_register_another()

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

    def ask_to_register_another(self):
        reply = QMessageBox.question(self, 'Register Another Teacher',
                                     'Do you want to register another teacher?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.add_teacher_tab()
        else:
            self.close()

    def edit_teacher_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.load_teachers_into_combobox()
        self.b6.clicked.connect(self.update_teacher_details)  # b6 is your Save button
        self.b7.clicked.connect(self.delete_teacher)  # b7 is your Delete button

    def load_teachers_into_combobox(self):
        self.cb21.clear()  # Clear existing items, replace cb21 with your actual QComboBox name
        users = load_users()  # Load users from file
        teachers = [user for user in users if user.get('type') == 'teacher']
        for teacher in teachers:
            self.cb21.addItem(teacher['email'], teacher)  # Adding teacher ID and associate the full teacher data

    def on_teacher_selected(self, index):
        if index == -1:  # No selection or the combo box is being cleared
            return

        teacher_data = self.cb21.itemData(index)
        if teacher_data:
            self.tb21.setText(teacher_data['teacherId'])
            self.tb22.setText(teacher_data['email'])
            self.tb23.setText(teacher_data['name'])
            self.tb24.setText(teacher_data['surname'])
            self.cb22.setCurrentText(teacher_data['gender'])
            self.tb25.setText(teacher_data['date_of_birth'])
            self.tb26.setText(teacher_data['phone'])

    def update_teacher_details(self):
        teacherId = self.tb21.text()
        email = self.tb22.text()
        name = self.tb23.text()
        surname = self.tb24.text()
        gender = self.cb22.currentText()
        date_of_birth = self.tb25.text()
        phone = self.tb26.text()
        password = self.tb27.text()

        users = load_users()
        for i, user in enumerate(users):
            if user.get('type') == 'teacher' and user['email'] == email:
                users[i].update({
                    'teacherId': teacherId,
                    'email': email,
                    'name': name,
                    'surname': surname,
                    'gender': gender,
                    'date_of_birth': date_of_birth,
                    'phone': phone,
                    'password': password
                })
                break
        save_users(users)
        QMessageBox.information(self, "Update Success", "Teacher details updated successfully.")
        self.load_teachers_into_combobox()  # Refresh the teacher list

    def delete_teacher(self):
        teacher_id_to_delete = self.cb21.currentText()
        users = load_users()
        users = [user for user in users if not (user.get('type') == 'teacher' and user['email'] == teacher_id_to_delete)]
        save_users(users)
        QMessageBox.information(self, "Deletion Success", "Teacher details deleted successfully.")
        self.load_teachers_into_combobox()  # Refresh the teacher list
###############################################################################################################
    def add_message_tab(self):
        self.tabWidget.setCurrentIndex(3)
    
    def getMessages(self):
            try:
                with open('messages.json', "r") as messageFile:
                    data = json.load(messageFile)
                    self.messages = data
                
            except (json.JSONDecodeError, FileNotFoundError):
                pass
    def load_users(self):
        self.model2 = QStandardItemModel()
        self.listView_4_a.setModel(self.model2)
        try:
            with open('users.json', 'r') as file:
                users = json.load(file)
                for user in users:
                    if user["email"] != self.email:
                        item = QStandardItem(user['email'])
                        self.model2.appendRow(item)
                        #self.comboBox_a.addItem(user['email'])
                        for key in self.messages.keys():
                            if user['email'] in key:
                                if self.email in key:
                                    if self.messages[key]["unread-messages"] == True:
                                        item.setBackground(QColor('green'))
                                        pass
                                        #change background
        except FileNotFoundError:
            print("users.json dosyası bulunamadı.")
        except json.JSONDecodeError:
            print("users.json dosyası doğru biçimde değil.")


    def send_message(self):
        selected_email = ""
        selected_indexes = self.listView_4_a.selectedIndexes()
        for index in selected_indexes:
            item = self.model2.itemFromIndex(index)
            selected_email = item.text()
        sender = self.email
        message_text = self.LineEdit_3_a.text()


        message_id1 = sender+selected_email
        message_id2 = selected_email+sender

        msg_list = []
    
        if message_id1 in self.messages:
            msg_list = self.messages[message_id1]["messages"]
            saved_message = f"{sender}: {message_text}"
            msg_list.append(saved_message)
            self.message_display = msg_list
            self.messages[message_id1] = {
                "unread-messages": True,
                "messages":msg_list
                }
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)

        elif message_id2 in self.messages:
            msg_list = self.messages[message_id2]["messages"]
            saved_message = f"{sender}: {message_text}"
            msg_list.append(saved_message)
            self.messages[message_id2] = {
                "unread-messages": True,
                "messages":msg_list
                }
            self.message_display = msg_list
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)
        else:
            saved_message = f"{sender}: {message_text}"
            self.messages[message_id1] = {
                "unread-messages": True,
                "messages": [saved_message]
            }
            self.message_display = self.messages[message_id1]
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)
        # self.messageSelected()
        # self.read_message()
                
        self.model = QStandardItemModel()
        self.list_view_3_a.setModel(self.model)
        for message in msg_list:
            item = QStandardItem(message)  
            self.model.appendRow(item)

        self.list_view_3_a.setModel(self.model)




        if message_text and selected_email:
            # self.message_display.append(f"Sen: {message_text}")  # Gönderilen mesajı ekrana ekler
            # self.message_display.append(f"Gönderilen: {selected_email}")  # Gönderilen e-postayı ekrana ekler
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Mesaj Gönderildi!")
            msg_box.setText(f"Mesajınız '{message_text}' adresine gönderildi: {selected_email}")
            msg_box.exec()
    
    def messageSelected(self):
        self.model = QStandardItemModel()
        self.list_view_3_a.setModel(self.model)
        #message_receiver = self.comboBox_a.currentText()
        message_receiver =""
        
        id1 = self.email + message_receiver
        id2 = message_receiver + self.email
        
        msg_list = []
        
        if id1 in self.messages:
            msg_list = self.messages[id1]
    
        elif id2 in self.messages:
            msg_list = self.messages[id2]
        
        for message in msg_list:
            item = QStandardItem(message)  
            self.model.appendRow(item)
        self.list_view_3_a.setModel(self.model) 

    def read_message(self):
        self.model = QStandardItemModel()
        self.list_view_3_a.setModel(self.model)

        selected_indexes = self.listView_4_a.selectedIndexes()
        message_receiver = ""
        for index in selected_indexes:
            item = self.model2.itemFromIndex(index)
            item.setBackground(QColor("white"))
        for key in self.messages.keys():
                if self.email and item.text() in key:
                    self.messages[key]["unread-messages"] = False
                    message_receiver = item.text()

        
        # message_receiver = self.comboBox_3.currentText()
        
        id1 = self.email + message_receiver
        id2 = message_receiver + self.email
        
        msg_list = []
        
        if id1 in self.messages:
            msg_list = self.messages[id1]["messages"]
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)
                    
        elif id2 in self.messages:
            msg_list = self.messages[id2]["messages"]
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)


        for message in msg_list:
            item = QStandardItem(message)  
            self.model.appendRow(item)

        self.list_view_3_a.setModel(self.model)
 
#############################################################################################################

## Part 1: Initialization and UI Setup ##

class TeacherApp(QMainWindow):
    def __init__(self, email):
        super(TeacherApp, self).__init__()
        loadUi("teacher.ui", self)
        self.email = email
        self.initializeUI()
        
        self.messages = dict()
        self.getMessages()
        self.load_users()

        self.listView_t.clicked.connect(self.read_message)
        self.model = QStandardItemModel()
        
        

        
        load_todolist()
        load_announcements()

    def initializeUI(self):
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.setupMenuActions()
        self.setupButtonActions()
        self.setupComboBoxActions()

    def setupMenuActions(self):
        self.menu11_t.triggered.connect(self.showEditProfileTab)
        self.menu21_t.triggered.connect(self.showCourseScheduleTab)
        self.menu31_t.triggered.connect(self.showMeetingScheduleTab)
        self.menu22_t.triggered.connect(self.showLessonAttendanceTab)
        self.menu32_t_2.triggered.connect(self.showMeetingAttendanceTab)
        self.menu71_t.triggered.connect(self.close)  # Logout from teacher menu
        self.announcementMenu.triggered.connect(self.add_announce_tab)
        self.menu41_t.triggered.connect(self.add_todolist_tab)
        self.menu51_t.triggered.connect(self.add_message_tab)
    def setupButtonActions(self):
        self.b6.clicked.connect(self.updateTeacherDetails)  
        self.b6_t.clicked.connect(self.saveCourseSchedule)
        self.b6_t_2.clicked.connect(self.saveMeetingSchedule)
        self.b7_t_3.clicked.connect(self.clearCourseScheduleForm)  
        self.b7_t_4.clicked.connect(self.clearMeetingScheduleForm)  
        self.b6_4_att.clicked.connect(self.saveLessonAttendanceDetails)
        self.b6_4_att_2.clicked.connect(self.saveMeetingAttendanceDetails)
        self.addButton.clicked.connect(self.add_announcement)
        self.editButton.clicked.connect(self.edit_announcement)
        self.deleteButton.clicked.connect(self.delete_announcement)
        self.add_button.clicked.connect(self.add_checkbox)
        self.remove_button.clicked.connect(self.remove_checkbox)
        self.sendButton3_t.clicked.connect(self.send_message)
    def setupComboBoxActions(self):
        self.cb22_t_49.currentIndexChanged.connect(self.studentSelectedForLesson)
        self.cb22_t_49.currentIndexChanged.connect(lambda: self.loadLessonAttendanceData(self.cb22_t_49.itemData(self.cb22_t_49.currentIndex()).get('email')))
        self.cb22_t_76.currentIndexChanged.connect(self.studentSelectedForMeeting)
        self.cb22_t_76.currentIndexChanged.connect(lambda: self.loadMeetingAttendanceData(self.cb22_t_76.itemData(self.cb22_t_76.currentIndex()).get('email')))
        #self.comboBox_t.currentIndexChanged.connect(self.messageSelected)
        #self.comboBox.currentIndexChanged.connect(self.itemSelected)
        self.comboBox.currentIndexChanged.connect(self.view_announcements)
 #############################################################################################################
 ## Part 2: Tab Display Methods ##
 
    def showEditProfileTab(self):
        self.tabWidget.setCurrentIndex(1)
        self.loadTeacherDetails()

    def showCourseScheduleTab(self):
        self.tabWidget.setCurrentIndex(2)
        self.loadCurrentCourseSchedule()

    def showMeetingScheduleTab(self):
        self.tabWidget.setCurrentIndex(4)
        self.loadCurrentMeetingSchedule()

    def showLessonAttendanceTab(self):
        self.tabWidget.setCurrentIndex(3)
        self.loadStudentListForLesson()
        self.loadCurrentCourseSchedule()
    
    def add_message_tab(self):
        self.tabWidget.setCurrentIndex(8)

    def showMeetingAttendanceTab(self):
        print("Opening Meeting Attendance Tab")
        try:
            self.tabWidget.setCurrentIndex(5)
            self.loadStudentListForMeeting()
            self.loadCurrentMeetingSchedule()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
            print(f"Error: {e}")
        
#############################################################################################################
## Part 3: Teacher Details Methods ##

    def loadTeacherDetails(self):
        users = load_users()
        for user in users:
            if user.get('type') == 'teacher' and user['email'] == self.email:
                # Load the teacher's details into the form
                self.tb21.setText(user.get('teacherId', ''))  
                self.tb22.setText(user.get('email', ''))  
                self.tb23.setText(user.get('name', ''))  
                self.tb24.setText(user.get('surname', ''))  
                self.cb11_tch.setCurrentText(user.get('gender', ''))  
                self.tb25.setText(user.get('date_of_birth', ''))  
                self.tb26.setText(user.get('phone', ''))  
                self.tb27.setText(user.get('password', ''))  
                break

    def updateTeacherDetails(self):
        teacher_id = self.tb21.text()
        email = self.tb22.text()
        name = self.tb23.text()
        surname = self.tb24.text()
        gender = self.cb11_tch.currentText()
        date_of_birth = self.tb25.text()
        phone = self.tb26.text()
        password = self.tb27.text()

        if not is_valid_email(email) or not is_valid_password(password) or not is_valid_phone(phone):
            QMessageBox.warning(self, "Update Error", "Invalid input format")
            return

        users = load_users()
        for i, user in enumerate(users):
            if user.get('type') == 'teacher' and user['email'] == self.email:
                users[i].update({
                    'teacherId': teacher_id,
                    'email': email,
                    'name': name,
                    'surname': surname,
                    'gender': gender,
                    'date_of_birth': date_of_birth,
                    'phone': phone,
                    'password': password
                })
                break
        save_users(users)
        QMessageBox.information(self, "Update Success", "Your teacher details updated successfully.")
#############################################################################################################
## Part 4: Course Schedule Methods ##

    def loadCurrentCourseSchedule(self):
        lessons = load_lessons()
        if not lessons:
            QMessageBox.information(self, "Load Schedule", "No existing schedule found.")
            return

        current_schedule = lessons[0]

        self.tb21_course.setText(current_schedule.get('date_lesson_1', ''))
        self.cb21_course.setCurrentText(current_schedule.get('time_slot_lesson_1', ''))
        self.tb22_course.setText(current_schedule.get('lesson_subject_lesson_1', ''))
        self.tb23_course.setText(current_schedule.get('date_lesson_2', ''))
        self.cb22_course.setCurrentText(current_schedule.get('time_slot_lesson_2', ''))
        self.tb24_course.setText(current_schedule.get('lesson_subject_lesson_2', ''))
        self.tb25_course.setText(current_schedule.get('date_lesson_3', ''))
        self.cb23_course.setCurrentText(current_schedule.get('time_slot_lesson_3', ''))
        self.tb26_course.setText(current_schedule.get('lesson_subject_lesson_3', ''))
        self.tb27_course.setText(current_schedule.get('date_lesson_4', ''))
        self.cb24_course.setCurrentText(current_schedule.get('time_slot_lesson_4', ''))
        self.tb28_course.setText(current_schedule.get('lesson_subject_lesson_4', ''))
        self.tb29_course.setText(current_schedule.get('date_lesson_5', ''))
        self.cb25_course.setCurrentText(current_schedule.get('time_slot_lesson_5', ''))
        self.tb210_course.setText(current_schedule.get('lesson_subject_lesson_5', ''))
        self.tb211_course.setText(current_schedule.get('date_lesson_6', ''))
        self.cb26_course.setCurrentText(current_schedule.get('time_slot_lesson_6', ''))
        self.tb212_course.setText(current_schedule.get('lesson_subject_lesson_6', ''))
        self.tb213_course.setText(current_schedule.get('date_lesson_7', ''))
        self.cb27_course.setCurrentText(current_schedule.get('time_slot_lesson_7', ''))
        self.tb214_course.setText(current_schedule.get('lesson_subject_lesson_7', ''))
        self.tb215_course.setText(current_schedule.get('date_lesson_8', ''))
        self.cb28_course.setCurrentText(current_schedule.get('time_slot_lesson_8', ''))
        self.tb216_course.setText(current_schedule.get('lesson_subject_lesson_8', ''))
        self.tb217_course.setText(current_schedule.get('date_lesson_9', ''))
        self.cb29_course.setCurrentText(current_schedule.get('time_slot_lesson_9', ''))
        self.tb218_course.setText(current_schedule.get('lesson_subject_lesson_9', ''))
        self.tb219_course.setText(current_schedule.get('date_lesson_10', ''))
        self.cb210_course.setCurrentText(current_schedule.get('time_slot_lesson_10', ''))
        self.tb220_course.setText(current_schedule.get('lesson_subject_lesson_10', ''))
        self.tb221_course.setText(current_schedule.get('date_lesson_11', ''))
        self.cb211_course.setCurrentText(current_schedule.get('time_slot_lesson_11', ''))
        self.tb222_course.setText(current_schedule.get('lesson_subject_lesson_11', ''))
        self.tb223_course.setText(current_schedule.get('date_lesson_12', ''))
        self.cb212_course.setCurrentText(current_schedule.get('time_slot_lesson_12', ''))
        self.tb224_course.setText(current_schedule.get('lesson_subject_lesson_12', ''))
        self.tb225_course.setText(current_schedule.get('date_lesson_13', ''))
        self.cb213_course.setCurrentText(current_schedule.get('time_slot_lesson_13', ''))
        self.tb226_course.setText(current_schedule.get('lesson_subject_lesson_13', ''))
        self.tb227_course.setText(current_schedule.get('date_lesson_14', ''))
        self.cb214_course.setCurrentText(current_schedule.get('time_slot_lesson_14', ''))
        self.tb228_course.setText(current_schedule.get('lesson_subject_lesson_14', ''))
        self.tb229_course.setText(current_schedule.get('date_lesson_15', ''))
        self.cb215_course.setCurrentText(current_schedule.get('time_slot_lesson_15', ''))
        self.tb230_course.setText(current_schedule.get('lesson_subject_lesson_15', ''))    

        
    def saveCourseSchedule(self):
        try:
            new_schedule = {
            'date_lesson_1': self.tb21_course.text(),
            'time_slot_lesson_1': self.cb21_course.currentText(),
            'lesson_subject_lesson_1': self.tb22_course.text(),
            'date_lesson_2': self.tb23_course.text(),
            'time_slot_lesson_2': self.cb22_course.currentText(),
            'lesson_subject_lesson_2': self.tb24_course.text(),
            'date_lesson_3': self.tb25_course.text(),
            'time_slot_lesson_3': self.cb23_course.currentText(),
            'lesson_subject_lesson_3': self.tb26_course.text(),
            'date_lesson_4': self.tb27_course.text(),
            'time_slot_lesson_4': self.cb24_course.currentText(),
            'lesson_subject_lesson_4': self.tb28_course.text(),
            'date_lesson_5': self.tb29_course.text(),
            'time_slot_lesson_5': self.cb25_course.currentText(),
            'lesson_subject_lesson_5': self.tb210_course.text(),
            'date_lesson_6': self.tb211_course.text(),
            'time_slot_lesson_6': self.cb26_course.currentText(),
            'lesson_subject_lesson_6': self.tb212_course.text(),
            'date_lesson_7': self.tb213_course.text(),
            'time_slot_lesson_7': self.cb27_course.currentText(),
            'lesson_subject_lesson_7': self.tb214_course.text(),
            'date_lesson_8': self.tb215_course.text(),
            'time_slot_lesson_8': self.cb28_course.currentText(),
            'lesson_subject_lesson_8': self.tb216_course.text(),
            'date_lesson_9': self.tb217_course.text(),
            'time_slot_lesson_9': self.cb29_course.currentText(),
            'lesson_subject_lesson_9': self.tb218_course.text(),
            'date_lesson_10': self.tb219_course.text(),
            'time_slot_lesson_10': self.cb210_course.currentText(),
            'lesson_subject_lesson_10': self.tb220_course.text(),
            'date_lesson_11': self.tb221_course.text(),
            'time_slot_lesson_11': self.cb211_course.currentText(),
            'lesson_subject_lesson_11': self.tb222_course.text(),
            'date_lesson_12': self.tb223_course.text(),
            'time_slot_lesson_12': self.cb212_course.currentText(),
            'lesson_subject_lesson_12': self.tb224_course.text(),
            'date_lesson_13': self.tb225_course.text(),
            'time_slot_lesson_13': self.cb213_course.currentText(),
            'lesson_subject_lesson_13': self.tb226_course.text(),
            'date_lesson_14': self.tb227_course.text(),
            'time_slot_lesson_14': self.cb214_course.currentText(),
            'lesson_subject_lesson_14': self.tb228_course.text(),
            'date_lesson_15': self.tb229_course.text(),
            'time_slot_lesson_15': self.cb215_course.currentText(),
            'lesson_subject_lesson_15': self.tb230_course.text(),
            }

        # This will overwrite the existing schedule with the new one
            save_lessons([new_schedule])
            QMessageBox.information(self, "Success", "Course schedule saved/updated successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"An error occurred: {e}")

    def clearCourseScheduleForm(self):
        self.tb21_course.clear()
        self.cb21_course.setCurrentIndex(0)
        self.tb22_course.clear()
        self.tb23_course.clear()
        self.cb22_course.setCurrentIndex(0)
        self.tb24_course.clear()
        self.tb25_course.clear()
        self.cb23_course.setCurrentIndex(0)
        self.tb26_course.clear()
        self.tb27_course.clear()
        self.cb24_course.setCurrentIndex(0)
        self.tb28_course.clear()
        self.tb29_course.clear()
        self.cb25_course.setCurrentIndex(0)
        self.tb210_course.clear()
        self.tb211_course.clear()
        self.cb26_course.setCurrentIndex(0)
        self.tb212_course.clear()
        self.tb213_course.clear()
        self.cb27_course.setCurrentIndex(0)
        self.tb214_course.clear()
        self.tb215_course.clear()
        self.cb28_course.setCurrentIndex(0)
        self.tb216_course.clear()
        self.tb217_course.clear()
        self.cb29_course.setCurrentIndex(0)
        self.tb218_course.clear()
        self.tb219_course.clear()
        self.cb210_course.setCurrentIndex(0)
        self.tb220_course.clear()
        self.tb221_course.clear()
        self.cb211_course.setCurrentIndex(0)
        self.tb222_course.clear()
        self.tb223_course.clear()
        self.cb212_course.setCurrentIndex(0)
        self.tb224_course.clear()
        self.tb225_course.clear()
        self.cb213_course.setCurrentIndex(0)
        self.tb226_course.clear()
        self.tb227_course.clear()
        self.cb214_course.setCurrentIndex(0)
        self.tb228_course.clear()
        self.tb229_course.clear()
        self.cb215_course.setCurrentIndex(0)
        self.tb230_course.clear()
        
        empty_schedule = {
            'date_lesson_1' :  '',
            'time_slot_lesson_1' :  '',
            'lesson_subject_lesson_1' :  '',
            'date_lesson_2' :  '',
            'time_slot_lesson_2' :  '',
            'lesson_subject_lesson_2' :  '',
            'date_lesson_3' :  '',
            'time_slot_lesson_3' :  '',
            'lesson_subject_lesson_3' :  '',
            'date_lesson_4' :  '',
            'time_slot_lesson_4' :  '',
            'lesson_subject_lesson_4' :  '',
            'date_lesson_5' :  '',
            'time_slot_lesson_5' :  '',
            'lesson_subject_lesson_5' :  '',
            'date_lesson_6' :  '',
            'time_slot_lesson_6' :  '',
            'lesson_subject_lesson_6' :  '',
            'date_lesson_7' :  '',
            'time_slot_lesson_7' :  '',
            'lesson_subject_lesson_7' :  '',
            'date_lesson_8' :  '',
            'time_slot_lesson_8' :  '',
            'lesson_subject_lesson_8' :  '',
            'date_lesson_9' :  '',
            'time_slot_lesson_9' :  '',
            'lesson_subject_lesson_9' :  '',
            'date_lesson_10' :  '',
            'time_slot_lesson_10' :  '',
            'lesson_subject_lesson_10' :  '',
            'date_lesson_11' :  '',
            'time_slot_lesson_11' :  '',
            'lesson_subject_lesson_11' :  '',
            'date_lesson_12' :  '',
            'time_slot_lesson_12' :  '',
            'lesson_subject_lesson_12' :  '',
            'date_lesson_13' :  '',
            'time_slot_lesson_13' :  '',
            'lesson_subject_lesson_13' :  '',
            'date_lesson_14' :  '',
            'time_slot_lesson_14' :  '',
            'lesson_subject_lesson_14' :  '',
            'date_lesson_15' :  '',
            'time_slot_lesson_15' :  '',
            'lesson_subject_lesson_15' :  '',
            
            }

        # Save the empty/default schedule
        try:
            save_lessons([empty_schedule])
            QMessageBox.information(self, "Success", "Course schedule cleared and updated in file.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while saving: {e}")    
            
 #############################################################################################################
 
 ## Part 5: Meeting Schedule Methods ##
 
    def loadCurrentMeetingSchedule(self):
        meetings = load_meetings()
        if not meetings:
            QMessageBox.information(self, "Load Schedule", "No existing schedule found.")
            return

        current_meeting_schedule = meetings[0]

        self.tb21_course_3.setText(current_meeting_schedule.get('date_meeting_1', ''))
        self.cb21_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_1', ''))
        self.tb22_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_1', ''))
        self.tb23_course_3.setText(current_meeting_schedule.get('date_meeting_2', ''))
        self.cb22_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_2', ''))
        self.tb24_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_2', ''))
        self.tb25_course_3.setText(current_meeting_schedule.get('date_meeting_3', ''))
        self.cb23_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_3', ''))
        self.tb26_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_3', ''))
        self.tb27_course_3.setText(current_meeting_schedule.get('date_meeting_4', ''))
        self.cb24_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_4', ''))
        self.tb28_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_4', ''))
        self.tb29_course_3.setText(current_meeting_schedule.get('date_meeting_5', ''))
        self.cb25_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_5', ''))
        self.tb210_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_5', ''))
        self.tb211_course_3.setText(current_meeting_schedule.get('date_meeting_6', ''))
        self.cb26_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_6', ''))
        self.tb212_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_6', ''))
        self.tb213_course_3.setText(current_meeting_schedule.get('date_meeting_7', ''))
        self.cb27_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_7', ''))
        self.tb214_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_7', ''))
        self.tb215_course_3.setText(current_meeting_schedule.get('date_meeting_8', ''))
        self.cb28_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_8', ''))
        self.tb216_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_8', ''))
        self.tb217_course_3.setText(current_meeting_schedule.get('date_meeting_9', ''))
        self.cb29_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_9', ''))
        self.tb218_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_9', ''))
        self.tb219_course_3.setText(current_meeting_schedule.get('date_meeting_10', ''))
        self.cb210_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_10', ''))
        self.tb220_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_10', ''))
        self.tb221_course_3.setText(current_meeting_schedule.get('date_meeting_11', ''))
        self.cb211_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_11', ''))
        self.tb222_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_11', ''))
        self.tb223_course_3.setText(current_meeting_schedule.get('date_meeting_12', ''))
        self.cb212_course.setCurrentText(current_meeting_schedule.get('time_slot_meeting_12', ''))
        self.tb224_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_12', ''))
        self.tb225_course_3.setText(current_meeting_schedule.get('date_meeting_13', ''))
        self.cb213_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_13', ''))
        self.tb226_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_13', ''))
        self.tb227_course_3.setText(current_meeting_schedule.get('date_meeting_14', ''))
        self.cb214_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_14', ''))
        self.tb228_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_14', ''))
        self.tb229_course_3.setText(current_meeting_schedule.get('date_meeting_15', ''))
        self.cb215_course_3.setCurrentText(current_meeting_schedule.get('time_slot_meeting_15', ''))
        self.tb230_course_3.setText(current_meeting_schedule.get('meeting_subject_meeting_15', ''))    

        
    def saveMeetingSchedule(self):
        try:
            new_meeting_schedule = {
            'date_meeting_1': self.tb21_course_3.text(),
            'time_slot_meeting_1': self.cb21_course_3.currentText(),
            'meeting_subject_meeting_1': self.tb22_course_3.text(),
            'date_meeting_2': self.tb23_course_3.text(),
            'time_slot_meeting_2': self.cb22_course_3.currentText(),
            'meeting_subject_meeting_2': self.tb24_course_3.text(),
            'date_meeting_3': self.tb25_course_3.text(),
            'time_slot_meeting_3': self.cb23_course_3.currentText(),
            'meeting_subject_meeting_3': self.tb26_course_3.text(),
            'date_meeting_4': self.tb27_course_3.text(),
            'time_slot_meeting_4': self.cb24_course_3.currentText(),
            'meeting_subject_meeting_4': self.tb28_course_3.text(),
            'date_meeting_5': self.tb29_course_3.text(),
            'time_slot_meeting_5': self.cb25_course_3.currentText(),
            'meeting_subject_meeting_5': self.tb210_course_3.text(),
            'date_meeting_6': self.tb211_course_3.text(),
            'time_slot_meeting_6': self.cb26_course_3.currentText(),
            'meeting_subject_meeting_6': self.tb212_course_3.text(),
            'date_meeting_7': self.tb213_course_3.text(),
            'time_slot_meeting_7': self.cb27_course_3.currentText(),
            'meeting_subject_meeting_7': self.tb214_course_3.text(),
            'date_meeting_8': self.tb215_course_3.text(),
            'time_slot_meeting_8': self.cb28_course_3.currentText(),
            'meeting_subject_meeting_8': self.tb216_course_3.text(),
            'date_meeting_9': self.tb217_course_3.text(),
            'time_slot_meeting_9': self.cb29_course_3.currentText(),
            'meeting_subject_meeting_9': self.tb218_course_3.text(),
            'date_meeting_10': self.tb219_course_3.text(),
            'time_slot_meeting_10': self.cb210_course_3.currentText(),
            'meeting_subject_meeting_10': self.tb220_course_3.text(),
            'date_meeting_11': self.tb221_course_3.text(),
            'time_slot_meeting_11': self.cb211_course_3.currentText(),
            'meeting_subject_meeting_11': self.tb222_course_3.text(),
            'date_meeting_12': self.tb223_course_3.text(),
            'time_slot_meeting_12': self.cb212_course_3.currentText(),
            'meeting_subject_meeting_12': self.tb224_course_3.text(),
            'date_meeting_13': self.tb225_course_3.text(),
            'time_slot_meeting_13': self.cb213_course_3.currentText(),
            'meeting_subject_meeting_13': self.tb226_course_3.text(),
            'date_meeting_14': self.tb227_course_3.text(),
            'time_slot_meeting_14': self.cb214_course_3.currentText(),
            'meeting_subject_meeting_14': self.tb228_course_3.text(),
            'date_meeting_15': self.tb229_course_3.text(),
            'time_slot_meeting_15': self.cb215_course_3.currentText(),
            'meeting_subject_meeting_15': self.tb230_course_3.text(),
            }

        # This will overwrite the existing schedule with the new one
            save_meetings([new_meeting_schedule])
            QMessageBox.information(self, "Success", "Course schedule saved/updated successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"An error occurred: {e}")

    def clearMeetingScheduleForm(self):
        # Clear the schedule form for all QLineEdit and QComboBox widgets
        self.tb21_course_3.clear()
        self.cb21_course_3.setCurrentIndex(0)
        self.tb22_course_3.clear()
        self.tb23_course_3.clear()
        self.cb22_course_3.setCurrentIndex(0)
        self.tb24_course_3.clear()
        self.tb25_course_3.clear()
        self.cb23_course_3.setCurrentIndex(0)
        self.tb26_course_3.clear()
        self.tb27_course_3.clear()
        self.cb24_course_3.setCurrentIndex(0)
        self.tb28_course_3.clear()
        self.tb29_course_3.clear()
        self.cb25_course_3.setCurrentIndex(0)
        self.tb210_course_3.clear()
        self.tb211_course_3.clear()
        self.cb26_course_3.setCurrentIndex(0)
        self.tb212_course_3.clear()
        self.tb213_course_3.clear()
        self.cb27_course_3.setCurrentIndex(0)
        self.tb214_course_3.clear()
        self.tb215_course_3.clear()
        self.cb28_course_3.setCurrentIndex(0)
        self.tb216_course_3.clear()
        self.tb217_course_3.clear()
        self.cb29_course_3.setCurrentIndex(0)
        self.tb218_course_3.clear()
        self.tb219_course_3.clear()
        self.cb210_course_3.setCurrentIndex(0)
        self.tb220_course_3.clear()
        self.tb221_course_3.clear()
        self.cb211_course_3.setCurrentIndex(0)
        self.tb222_course_3.clear()
        self.tb223_course_3.clear()
        self.cb212_course_3.setCurrentIndex(0)
        self.tb224_course_3.clear()
        self.tb225_course_3.clear()
        self.cb213_course_3.setCurrentIndex(0)
        self.tb226_course_3.clear()
        self.tb227_course_3.clear()
        self.cb214_course_3.setCurrentIndex(0)
        self.tb228_course_3.clear()
        self.tb229_course_3.clear()
        self.cb215_course_3.setCurrentIndex(0)
        self.tb230_course_3.clear()
 
        # Create an empty or default meeting schedule
        empty_meeting_schedule = {
            'date_meeting_1' :  '',
            'time_slot_meeting_1' :  '',
            'meeting_subject_meeting_1' :  '',
            'date_meeting_2' :  '',
            'time_slot_meeting_2' :  '',
            'meeting_subject_meeting_2' :  '',
            'date_meeting_3' :  '',
            'time_slot_meeting_3' :  '',
            'meeting_subject_meeting_3' :  '',
            'date_meeting_4' :  '',
            'time_slot_meeting_4' :  '',
            'meeting_subject_meeting_4' :  '',
            'date_meeting_5' :  '',
            'time_slot_meeting_5' :  '',
            'meeting_subject_meeting_5' :  '',
            'date_meeting_6' :  '',
            'time_slot_meeting_6' :  '',
            'meeting_subject_meeting_6' :  '',
            'date_meeting_7' :  '',
            'time_slot_meeting_7' :  '',
            'meeting_subject_meeting_7' :  '',
            'date_meeting_8' :  '',
            'time_slot_meeting_8' :  '',
            'meeting_subject_meeting_8' :  '',
            'date_meeting_9' :  '',
            'time_slot_meeting_9' :  '',
            'meeting_subject_meeting_9' :  '',
            'date_meeting_10' :  '',
            'time_slot_meeting_10' :  '',
            'meeting_subject_meeting_10' :  '',
            'date_meeting_11' :  '',
            'time_slot_meeting_11' :  '',
            'meeting_subject_meeting_11' :  '',
            'date_meeting_12' :  '',
            'time_slot_meeting_12' :  '',
            'meeting_subject_meeting_12' :  '',
            'date_meeting_13' :  '',
            'time_slot_meeting_13' :  '',
            'meeting_subject_meeting_13' :  '',
            'date_meeting_14' :  '',
            'time_slot_meeting_14' :  '',
            'meeting_subject_meeting_14' :  '',
            'date_meeting_15' :  '',
            'time_slot_meeting_15' :  '',
            'meeting_subject_meeting_15' :  '',

        }

        # Save the empty/default schedule
        try:
            save_meetings([empty_meeting_schedule])
            QMessageBox.information(self, "Success", "Meeting schedule cleared and updated in file.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while saving: {e}")
    
############################################################################################################# 
## Part 6: Lesson Attendance Methods ##

               
    def loadStudentListForLesson(self):
        self.cb22_t_49.clear()
        self.cb22_t_49.addItem("Select a student", None)  # Default item
        users = load_users()
        for user in users:
            if is_student(user):
                # Create a dictionary to store as item data
                student_info = {'studentId': user['studentId'], 'email': user['email'],'name': user['name'],'surname': user['surname']}
                # Add the student's name and the dictionary as the item data
                self.cb22_t_49.addItem(f"{user['email']}", student_info)
                
                
    def studentSelectedForLesson(self, index):
        if index == -1:  # No selection or the combo box is being cleared
            return
        
        # Clear attendance data fields here
        self.clearLessonAttendanceData()

        student_data = self.cb22_t_49.itemData(index)

        if student_data:
            
           
            
            student_name = student_name = f"{student_data.get('name', '')} {student_data.get('surname', '')}"
            student_email = student_data.get('email', '')
            self.tb23_3.setText(student_name)  # Assuming tb23_3 is the QLineEdit for student ID
            self.tb24_3.setText(student_email)  # Assuming tb24_3 is the QLineEdit for email
            
            

            # Load attendance data for the selected student
            self.loadLessonAttendanceData(student_email)
            

            
            
        else:
            QMessageBox.warning(self, "Error", "Student data is not in the expected format.")
            
            
    def clearLessonAttendanceData(self):
        # Clearing all the attendance data fields
        self.tb21_course_2.clear()
        self.cb21_course_2.setCurrentIndex(0)
        self.cb22_t_50.setCurrentIndex(0)
        self.tb23_course_2.clear()
        self.cb22_course_2.setCurrentIndex(0)
        self.cb22_t_51.setCurrentIndex(0)
        self.tb25_course_2.clear()
        self.cb23_course_2.setCurrentIndex(0)
        self.cb22_t_52.setCurrentIndex(0)
        self.tb27_course_2.clear()
        self.cb24_course_2.setCurrentIndex(0)
        self.cb22_t_53.setCurrentIndex(0)
        self.tb29_course_2.clear()
        self.cb25_course_2.setCurrentIndex(0)
        self.cb22_t_54.setCurrentIndex(0)
        self.tb211_course_2.clear()
        self.cb26_course_2.setCurrentIndex(0)
        self.cb22_t_55.setCurrentIndex(0)
        self.tb213_course_2.clear()
        self.cb27_course_2.setCurrentIndex(0)
        self.cb22_t_56.setCurrentIndex(0)
        self.tb215_course_2.clear()
        self.cb28_course_2.setCurrentIndex(0)
        self.cb22_t_57.setCurrentIndex(0)
        self.tb217_course_2.clear()
        self.cb29_course_2.setCurrentIndex(0)
        self.cb22_t_58.setCurrentIndex(0)
        self.tb219_course_2.clear()
        self.cb210_course_2.setCurrentIndex(0)
        self.cb22_t_59.setCurrentIndex(0)
        self.tb221_course_2.clear()
        self.cb211_course_2.setCurrentIndex(0)
        self.cb22_t_60.setCurrentIndex(0)
        self.tb223_course_2.clear()
        self.cb212_course_2.setCurrentIndex(0)
        self.cb22_t_61.setCurrentIndex(0)
        self.tb225_course_2.clear()
        self.cb213_course_2.setCurrentIndex(0)
        self.cb22_t_62.setCurrentIndex(0)
        self.tb227_course_2.clear()
        self.cb214_course_2.setCurrentIndex(0)
        self.cb22_t_63.setCurrentIndex(0)
        self.tb229_course_2.clear()
        self.cb215_course_2.setCurrentIndex(0)
        self.cb22_t_64.setCurrentIndex(0)
            

            
    def loadLessonAttendanceData(self, student_email):
        # Load the attendance data for the selected student
        attendance = load_attendance()
        student_attendance = attendance.get(student_email, {})
        
        if not student_attendance:
            self.loadCurrentCourseScheduleIntoAttendance()
            
        else:
            self.tb21_course_2.setText(student_attendance.get('date_lesson_1', ''))
            self.cb21_course_2.setCurrentText(student_attendance.get('time_slot_lesson_1', ''))
            self.cb22_t_50.setCurrentText(student_attendance.get('status_lesson_1', ''))
            self.tb23_course_2.setText(student_attendance.get('date_lesson_2', ''))
            self.cb22_course_2.setCurrentText(student_attendance.get('time_slot_lesson_2', ''))
            self.cb22_t_51.setCurrentText(student_attendance.get('status_lesson_2', ''))
            self.tb25_course_2.setText(student_attendance.get('date_lesson_3', ''))
            self.cb23_course_2.setCurrentText(student_attendance.get('time_slot_lesson_3', ''))
            self.cb22_t_52.setCurrentText(student_attendance.get('status_lesson_3', ''))
            self.tb27_course_2.setText(student_attendance.get('date_lesson_4', ''))
            self.cb24_course_2.setCurrentText(student_attendance.get('time_slot_lesson_4', ''))
            self.cb22_t_53.setCurrentText(student_attendance.get('status_lesson_4', ''))
            self.tb29_course_2.setText(student_attendance.get('date_lesson_5', ''))
            self.cb25_course_2.setCurrentText(student_attendance.get('time_slot_lesson_5', ''))
            self.cb22_t_54.setCurrentText(student_attendance.get('status_lesson_5', ''))
            self.tb211_course_2.setText(student_attendance.get('date_lesson_6', ''))
            self.cb26_course_2.setCurrentText(student_attendance.get('time_slot_lesson_6', ''))
            self.cb22_t_55.setCurrentText(student_attendance.get('status_lesson_6', ''))
            self.tb213_course_2.setText(student_attendance.get('date_lesson_7', ''))
            self.cb27_course_2.setCurrentText(student_attendance.get('time_slot_lesson_7', ''))
            self.cb22_t_56.setCurrentText(student_attendance.get('status_lesson_7', ''))
            self.tb215_course_2.setText(student_attendance.get('date_lesson_8', ''))
            self.cb28_course_2.setCurrentText(student_attendance.get('time_slot_lesson_8', ''))
            self.cb22_t_57.setCurrentText(student_attendance.get('status_lesson_8', ''))
            self.tb217_course_2.setText(student_attendance.get('date_lesson_9', ''))
            self.cb29_course_2.setCurrentText(student_attendance.get('time_slot_lesson_9', ''))
            self.cb22_t_58.setCurrentText(student_attendance.get('status_lesson_9', ''))
            self.tb219_course_2.setText(student_attendance.get('date_lesson_10', ''))
            self.cb210_course_2.setCurrentText(student_attendance.get('time_slot_lesson_10', ''))
            self.cb22_t_59.setCurrentText(student_attendance.get('status_lesson_10', ''))
            self.tb221_course_2.setText(student_attendance.get('date_lesson_11', ''))
            self.cb211_course_2.setCurrentText(student_attendance.get('time_slot_lesson_11', ''))
            self.cb22_t_60.setCurrentText(student_attendance.get('status_lesson_11', ''))
            self.tb223_course_2.setText(student_attendance.get('date_lesson_12', ''))
            self.cb212_course_2.setCurrentText(student_attendance.get('time_slot_lesson_12', ''))
            self.cb22_t_61.setCurrentText(student_attendance.get('status_lesson_12', ''))
            self.tb225_course_2.setText(student_attendance.get('date_lesson_13', ''))
            self.cb213_course_2.setCurrentText(student_attendance.get('time_slot_lesson_13', ''))
            self.cb22_t_62.setCurrentText(student_attendance.get('  status_lesson_13', ''))
            self.tb227_course_2.setText(student_attendance.get('date_lesson_14', ''))
            self.cb214_course_2.setCurrentText(student_attendance.get('time_slot_lesson_14', ''))
            self.cb22_t_63.setCurrentText(student_attendance.get('status_lesson_14', ''))
            self.tb229_course_2.setText(student_attendance.get('date_lesson_15', ''))
            self.cb215_course_2.setCurrentText(student_attendance.get('time_slot_lesson_15', ''))
            self.cb22_t_64.setCurrentText(student_attendance.get('status_lesson_15', ''))

                 
    
    def loadCurrentCourseScheduleIntoAttendance(self):

        lessons = load_lessons()
        if lessons:
           
            current_schedule = lessons[0]

            self.tb21_course_2.setText(current_schedule.get('date_lesson_1', ''))
            self.cb21_course_2.setCurrentText(current_schedule.get('time_slot_lesson_1', ''))
            self.tb23_course_2.setText(current_schedule.get('date_lesson_2', ''))
            self.cb22_course_2.setCurrentText(current_schedule.get('time_slot_lesson_2', ''))
            self.tb25_course_2.setText(current_schedule.get('date_lesson_3', ''))
            self.cb23_course_2.setCurrentText(current_schedule.get('time_slot_lesson_3', ''))
            self.tb27_course_2.setText(current_schedule.get('date_lesson_4', ''))
            self.cb24_course_2.setCurrentText(current_schedule.get('time_slot_lesson_4', ''))
            self.tb29_course_2.setText(current_schedule.get('date_lesson_5', ''))
            self.cb25_course_2.setCurrentText(current_schedule.get('time_slot_lesson_5', ''))
            self.tb211_course_2.setText(current_schedule.get('date_lesson_6', ''))
            self.cb26_course_2.setCurrentText(current_schedule.get('time_slot_lesson_6', ''))
            self.tb213_course_2.setText(current_schedule.get('date_lesson_7', ''))
            self.cb27_course_2.setCurrentText(current_schedule.get('time_slot_lesson_7', ''))
            self.tb215_course_2.setText(current_schedule.get('date_lesson_8', ''))
            self.cb28_course_2.setCurrentText(current_schedule.get('time_slot_lesson_8', ''))
            self.tb217_course_2.setText(current_schedule.get('date_lesson_9', ''))
            self.cb29_course_2.setCurrentText(current_schedule.get('time_slot_lesson_9', ''))
            self.tb219_course_2.setText(current_schedule.get('date_lesson_10', ''))
            self.cb210_course_2.setCurrentText(current_schedule.get('time_slot_lesson_10', ''))
            self.tb221_course_2.setText(current_schedule.get('date_lesson_11', ''))
            self.cb211_course_2.setCurrentText(current_schedule.get('time_slot_lesson_11', ''))
            self.tb223_course_2.setText(current_schedule.get('date_lesson_12', ''))
            self.cb212_course_2.setCurrentText(current_schedule.get('time_slot_lesson_12', ''))
            self.tb225_course_2.setText(current_schedule.get('date_lesson_13', ''))
            self.cb213_course_2.setCurrentText(current_schedule.get('time_slot_lesson_13', ''))
            self.tb227_course_2.setText(current_schedule.get('date_lesson_14', ''))
            self.cb214_course_2.setCurrentText(current_schedule.get('time_slot_lesson_14', ''))
            self.tb229_course_2.setText(current_schedule.get('date_lesson_15', ''))
            self.cb215_course_2.setCurrentText(current_schedule.get('time_slot_lesson_15', ''))
        else:
            QMessageBox.information(self, "Load Schedule", "No existing schedule found.")
            
    
            
    def saveLessonAttendanceDetails(self):
        student_index = self.cb22_t_49.currentIndex()
        student_data = self.cb22_t_49.itemData(student_index)
        if not student_data:
            QMessageBox.warning(self, "Error", "No student selected")
            return

        student_email = student_data.get('email')
        if not student_email:
            QMessageBox.warning(self, "Error", "Invalid student email")
            return

        try:
            new_attendance = {
                'date_lesson_1' : self.tb21_course_2.text(),
                'time_slot_lesson_1' : self.cb21_course_2.currentText(),
                'status_lesson_1' : self.cb22_t_50.currentText(),
                'date_lesson_2' : self.tb23_course_2.text(),
                'time_slot_lesson_2' : self.cb22_course_2.currentText(),
                'status_lesson_2' : self.cb22_t_51.currentText(),
                'date_lesson_3' : self.tb25_course_2.text(),
                'time_slot_lesson_3' : self.cb23_course_2.currentText(),
                'status_lesson_3' : self.cb22_t_52.currentText(),
                'date_lesson_4' : self.tb27_course_2.text(),
                'time_slot_lesson_4' : self.cb24_course_2.currentText(),
                'status_lesson_4' : self.cb22_t_53.currentText(),
                'date_lesson_5' : self.tb29_course_2.text(),
                'time_slot_lesson_5' : self.cb25_course_2.currentText(),
                'status_lesson_5' : self.cb22_t_54.currentText(),
                'date_lesson_6' : self.tb211_course_2.text(),
                'time_slot_lesson_6' : self.cb26_course_2.currentText(),
                'status_lesson_6' : self.cb22_t_55.currentText(),
                'date_lesson_7' : self.tb213_course_2.text(),
                'time_slot_lesson_7' : self.cb27_course_2.currentText(),
                'status_lesson_7' : self.cb22_t_56.currentText(),
                'date_lesson_8' : self.tb215_course_2.text(),
                'time_slot_lesson_8' : self.cb28_course_2.currentText(),
                'status_lesson_8' : self.cb22_t_57.currentText(),
                'date_lesson_9' : self.tb217_course_2.text(),
                'time_slot_lesson_9' : self.cb29_course_2.currentText(),
                'status_lesson_9' : self.cb22_t_58.currentText(),
                'date_lesson_10' : self.tb219_course_2.text(),
                'time_slot_lesson_10' : self.cb210_course_2.currentText(),
                'status_lesson_10' : self.cb22_t_59.currentText(),
                'date_lesson_11' : self.tb221_course_2.text(),
                'time_slot_lesson_11' : self.cb211_course_2.currentText(),
                'status_lesson_11' : self.cb22_t_60.currentText(),
                'date_lesson_12' : self.tb223_course_2.text(),
                'time_slot_lesson_12' : self.cb212_course_2.currentText(),
                'status_lesson_12' : self.cb22_t_61.currentText(),
                'date_lesson_13' : self.tb225_course_2.text(),
                'time_slot_lesson_13' : self.cb213_course_2.currentText(),
                'status_lesson_13' : self.cb22_t_62.currentText(),
                'date_lesson_14' : self.tb227_course_2.text(),
                'time_slot_lesson_14' : self.cb214_course_2.currentText(),
                'status_lesson_14' : self.cb22_t_63.currentText(),
                'date_lesson_15' : self.tb229_course_2.text(),
                'time_slot_lesson_15' : self.cb215_course_2.currentText(),
                'status_lesson_15' : self.cb22_t_64.currentText(),

            }

        
            attendance = load_attendance()
            attendance[student_email] = new_attendance
            
            save_attendance(attendance)
            QMessageBox.information(self, "Success", "Lesson attendance saved/updated successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"An error occurred: {e}")  
        
#############################################################################################################
## Part 7: Meeting Attendance Methods ##

    def loadStudentListForMeeting(self):
        # Load students into the studentComboBox
        self.cb22_t_76.clear()
        self.cb22_t_76.addItem("Select a student", None)  # Default item
        users = load_users()
        for user in users:
            if is_student(user):
                # Create a dictionary to store as item data
                student_info = {'studentId': user['studentId'], 'email': user['email'], 'name': user['name'],'surname': user['surname']}
                # Add the student's name and the dictionary as the item data
                self.cb22_t_76.addItem(f"{user['email']}", student_info)
                
    def studentSelectedForMeeting(self, index):
        if index == -1:  # No selection or the combo box is being cleared
            return

        # Clear attendance data fields here
        self.clearMeetingAttendanceData()
        
        student_data = self.cb22_t_76.itemData(index)
        if student_data:
            student_name = student_name = f"{student_data.get('name', '')} {student_data.get('surname', '')}"
            student_email = student_data.get('email', '')

            self.tb23_4.setText(student_name)  # Assuming tb23_3 is the QLineEdit for student ID
            self.tb24_4.setText(student_email)  # Assuming tb24_3 is the QLineEdit for email
        else:
            QMessageBox.warning(self, "Error", "Student data is not in the expected format.")


    def clearMeetingAttendanceData(self):
        # Clearing all the attendance data fields
        self.tb21_course_4.clear()
        self.cb21_course_4.setCurrentIndex(0)
        self.cb22_t_71.setCurrentIndex(0)
        self.tb23_course_4.clear()
        self.cb22_course_4.setCurrentIndex(0)
        self.cb22_t_67.setCurrentIndex(0)
        self.tb25_course_4.clear()
        self.cb23_course_4.setCurrentIndex(0)
        self.cb22_t_74.setCurrentIndex(0)
        self.tb27_course_4.clear()
        self.cb24_course_4.setCurrentIndex(0)
        self.cb22_t_65.setCurrentIndex(0)
        self.tb29_course_4.clear()
        self.cb25_course_4.setCurrentIndex(0)
        self.cb22_t_73.setCurrentIndex(0)
        self.tb211_course_4.clear()
        self.cb26_course_4.setCurrentIndex(0)
        self.cb22_t_75.setCurrentIndex(0)
        self.tb213_course_4.clear()
        self.cb27_course_4.setCurrentIndex(0)
        self.cb22_t_79.setCurrentIndex(0)
        self.tb215_course_4.clear()
        self.cb28_course_4.setCurrentIndex(0)
        self.cb22_t_80.setCurrentIndex(0)
        self.tb217_course_4.clear()
        self.cb29_course_4.setCurrentIndex(0)
        self.cb22_t_69.setCurrentIndex(0)
        self.tb219_course_4.clear()
        self.cb210_course_4.setCurrentIndex(0)
        self.cb22_t_78.setCurrentIndex(0)
        self.tb221_course_4.clear()
        self.cb211_course_4.setCurrentIndex(0)
        self.cb22_t_66.setCurrentIndex(0)
        self.tb223_course_4.clear()
        self.cb212_course_4.setCurrentIndex(0)
        self.cb22_t_68.setCurrentIndex(0)
        self.tb225_course_4.clear()
        self.cb213_course_4.setCurrentIndex(0)
        self.cb22_t_77.setCurrentIndex(0)
        self.tb227_course_4.clear()
        self.cb214_course_4.setCurrentIndex(0)
        self.cb22_t_70.setCurrentIndex(0)
        self.tb229_course_4.clear()
        self.cb215_course_4.setCurrentIndex(0)
        self.cb22_t_72.setCurrentIndex(0)     

    def loadMeetingAttendanceData(self, student_email):
         # Load the attendance data for the selected student
        meeting_attendance = load_meeting_attendance()
        student_meeting_attendance = meeting_attendance.get(student_email, {})
        
        if not student_meeting_attendance:
            self.loadCurrentMeetingScheduleIntoMeetingAttendance()
            
        else:
            self.tb21_course_4.setText(student_meeting_attendance.get('date_meeting_1', ''))
            self.cb21_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_1', ''))
            self.cb22_t_71.setCurrentText(student_meeting_attendance.get('status_meeting_1', ''))
            self.tb23_course_4.setText(student_meeting_attendance.get('date_meeting_2', ''))
            self.cb22_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_2', ''))
            self.cb22_t_67.setCurrentText(student_meeting_attendance.get('status_meeting_2', ''))
            self.tb25_course_4.setText(student_meeting_attendance.get('date_meeting_3', ''))
            self.cb23_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_3', ''))
            self.cb22_t_74.setCurrentText(student_meeting_attendance.get('status_meeting_3', ''))
            self.tb27_course_4.setText(student_meeting_attendance.get('date_meeting_4', ''))
            self.cb24_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_4', ''))
            self.cb22_t_65.setCurrentText(student_meeting_attendance.get('status_meeting_4', ''))
            self.tb29_course_4.setText(student_meeting_attendance.get('date_meeting_5', ''))
            self.cb25_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_5', ''))
            self.cb22_t_73.setCurrentText(student_meeting_attendance.get('status_meeting_5', ''))
            self.tb211_course_4.setText(student_meeting_attendance.get('date_meeting_6', ''))
            self.cb26_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_6', ''))
            self.cb22_t_75.setCurrentText(student_meeting_attendance.get('status_meeting_6', ''))
            self.tb213_course_4.setText(student_meeting_attendance.get('date_meeting_7', ''))
            self.cb27_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_7', ''))
            self.cb22_t_79.setCurrentText(student_meeting_attendance.get('status_meeting_7', ''))
            self.tb215_course_4.setText(student_meeting_attendance.get('date_meeting_8', ''))
            self.cb28_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_8', ''))
            self.cb22_t_80.setCurrentText(student_meeting_attendance.get('status_meeting_8', ''))
            self.tb217_course_4.setText(student_meeting_attendance.get('date_meeting_9', ''))
            self.cb29_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_9', ''))
            self.cb22_t_69.setCurrentText(student_meeting_attendance.get('status_meeting_9', ''))
            self.tb219_course_4.setText(student_meeting_attendance.get('date_meeting_10', ''))
            self.cb210_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_10', ''))
            self.cb22_t_78.setCurrentText(student_meeting_attendance.get('status_meeting_10', ''))
            self.tb221_course_4.setText(student_meeting_attendance.get('date_meeting_11', ''))
            self.cb211_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_11', ''))
            self.cb22_t_66.setCurrentText(student_meeting_attendance.get('status_meeting_11', ''))
            self.tb223_course_4.setText(student_meeting_attendance.get('date_meeting_12', ''))
            self.cb212_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_12', ''))
            self.cb22_t_68.setCurrentText(student_meeting_attendance.get('status_meeting_12', ''))
            self.tb225_course_4.setText(student_meeting_attendance.get('date_meeting_13', ''))
            self.cb213_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_13', ''))
            self.cb22_t_77.setCurrentText(student_meeting_attendance.get('  status_meeting_13', ''))
            self.tb227_course_4.setText(student_meeting_attendance.get('date_meeting_14', ''))
            self.cb214_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_14', ''))
            self.cb22_t_70.setCurrentText(student_meeting_attendance.get('status_meeting_14', ''))
            self.tb229_course_4.setText(student_meeting_attendance.get('date_meeting_15', ''))
            self.cb215_course_4.setCurrentText(student_meeting_attendance.get('time_slot_meeting_15', ''))
            self.cb22_t_72.setCurrentText(student_meeting_attendance.get('status_meeting_15', ''))

            
            
    def loadCurrentMeetingScheduleIntoMeetingAttendance(self):
        meetings = load_meetings()
        if meetings:
           
            current_meeting_schedule = meetings[0]

            self.tb21_course_4.setText(current_meeting_schedule.get('date_meeting_1', ''))
            self.cb21_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_1', ''))
            self.tb23_course_4.setText(current_meeting_schedule.get('date_meeting_2', ''))
            self.cb22_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_2', ''))
            self.tb25_course_4.setText(current_meeting_schedule.get('date_meeting_3', ''))
            self.cb23_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_3', ''))
            self.tb27_course_4.setText(current_meeting_schedule.get('date_meeting_4', ''))
            self.cb24_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_4', ''))
            self.tb29_course_4.setText(current_meeting_schedule.get('date_meeting_5', ''))
            self.cb25_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_5', ''))
            self.tb211_course_4.setText(current_meeting_schedule.get('date_meeting_6', ''))
            self.cb26_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_6', ''))
            self.tb213_course_4.setText(current_meeting_schedule.get('date_meeting_7', ''))
            self.cb27_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_7', ''))
            self.tb215_course_4.setText(current_meeting_schedule.get('date_meeting_8', ''))
            self.cb28_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_8', ''))
            self.tb217_course_4.setText(current_meeting_schedule.get('date_meeting_9', ''))
            self.cb29_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_9', ''))
            self.tb219_course_4.setText(current_meeting_schedule.get('date_meeting_10', ''))
            self.cb210_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_10', ''))
            self.tb221_course_4.setText(current_meeting_schedule.get('date_meeting_11', ''))
            self.cb211_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_11', ''))
            self.tb223_course_4.setText(current_meeting_schedule.get('date_meeting_12', ''))
            self.cb212_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_12', ''))
            self.tb225_course_4.setText(current_meeting_schedule.get('date_meeting_13', ''))
            self.cb213_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_13', ''))
            self.tb227_course_4.setText(current_meeting_schedule.get('date_meeting_14', ''))
            self.cb214_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_14', ''))
            self.tb229_course_4.setText(current_meeting_schedule.get('date_meeting_15', ''))
            self.cb215_course_4.setCurrentText(current_meeting_schedule.get('time_slot_meeting_15', '')) 
             
        else:
             QMessageBox.information(self, "Load Meeting Schedule", "No meeting schedule found.")
            
              
    def saveMeetingAttendanceDetails(self):
        student_index = self.cb22_t_76.currentIndex()
        student_data = self.cb22_t_76.itemData(student_index)
        if not student_data:
            QMessageBox.warning(self, "Error", "No student selected")
            return

        student_email = student_data.get('email')
        if not student_email:
            QMessageBox.warning(self, "Error", "Invalid student email")
            return

        try:
            new_meeting_attendance = {
                'date_meeting_1' : self.tb21_course_4.text(),
                'time_slot_meeting_1' : self.cb21_course_4.currentText(),
                'status_meeting_1' : self.cb22_t_71.currentText(),
                'date_meeting_2' : self.tb23_course_4.text(),
                'time_slot_meeting_2' : self.cb22_course_4.currentText(),
                'status_meeting_2' : self.cb22_t_67.currentText(),
                'date_meeting_3' : self.tb25_course_4.text(),
                'time_slot_meeting_3' : self.cb23_course_4.currentText(),
                'status_meeting_3' : self.cb22_t_74.currentText(),
                'date_meeting_4' : self.tb27_course_4.text(),
                'time_slot_meeting_4' : self.cb24_course_4.currentText(),
                'status_meeting_4' : self.cb22_t_65.currentText(),
                'date_meeting_5' : self.tb29_course_4.text(),
                'time_slot_meeting_5' : self.cb25_course_4.currentText(),
                'status_meeting_5' : self.cb22_t_73.currentText(),
                'date_meeting_6' : self.tb211_course_4.text(),
                'time_slot_meeting_6' : self.cb26_course_4.currentText(),
                'status_meeting_6' : self.cb22_t_75.currentText(),
                'date_meeting_7' : self.tb213_course_4.text(),
                'time_slot_meeting_7' : self.cb27_course_4.currentText(),
                'status_meeting_7' : self.cb22_t_79.currentText(),
                'date_meeting_8' : self.tb215_course_4.text(),
                'time_slot_meeting_8' : self.cb28_course_4.currentText(),
                'status_meeting_8' : self.cb22_t_80.currentText(),
                'date_meeting_9' : self.tb217_course_4.text(),
                'time_slot_meeting_9' : self.cb29_course_4.currentText(),
                'status_meeting_9' : self.cb22_t_69.currentText(),
                'date_meeting_10' : self.tb219_course_4.text(),
                'time_slot_meeting_10' : self.cb210_course_4.currentText(),
                'status_meeting_10' : self.cb22_t_78.currentText(),
                'date_meeting_11' : self.tb221_course_4.text(),
                'time_slot_meeting_11' : self.cb211_course_4.currentText(),
                'status_meeting_11' : self.cb22_t_66.currentText(),
                'date_meeting_12' : self.tb223_course_4.text(),
                'time_slot_meeting_12' : self.cb212_course_4.currentText(),
                'status_meeting_12' : self.cb22_t_68.currentText(),
                'date_meeting_13' : self.tb225_course_4.text(),
                'time_slot_meeting_13' : self.cb213_course_4.currentText(),
                'status_meeting_13' : self.cb22_t_77.currentText(),
                'date_meeting_14' : self.tb227_course_4.text(),
                'time_slot_meeting_14' : self.cb214_course_4.currentText(),
                'status_meeting_14' : self.cb22_t_70.currentText(),
                'date_meeting_15' : self.tb229_course_4.text(),
                'time_slot_meeting_15' : self.cb215_course_4.currentText(),
                'status_meeting_15' : self.cb22_t_72.currentText(),

            }

        
            meeting_attendance = load_meeting_attendance()
            meeting_attendance[student_email] = new_meeting_attendance
            
            save_meeting_attendance(meeting_attendance)
            QMessageBox.information(self, "Success", "meeting attendance saved/updated successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"An error occurred: {e}")
    ###################################################################################################################################
    ## Part 8: Announcement Methods ##
    def add_announce_tab(self):
        self.tabWidget.setCurrentIndex(6)
        self.load_announcements_from_json()
    def add_announcement(self):
        text = self.textEdit.toPlainText()
        title = self.LineEdit.text()

        # Yeni duyuruyu oluştur
        new_announcement = {"title": title, "text": text}

        # Önceki duyuruları yükle
        saved_announcements = load_announcements()

        # Yeni duyuruyu ekle
        saved_announcements.append(new_announcement)

        # Yeni duyuruyu JSON dosyasına kaydet
        save_announcements(saved_announcements)

        # ComboBox'a ekle
        self.comboBox.addItem(f"{title}: {text}")

        # Temizleme işlemleri
        self.textEdit.clear()
        self.LineEdit.clear()

        QMessageBox.information(self, "Saved", "Announcement saved successfully.")

    
    
    def load_announcements_from_json(self):
        self.comboBox.clear()  # Önceki duyuruları temizle
        announcements = load_announcements()
        for announcement in announcements:
            title = announcement.get('title')
            text = announcement.get('text')
            if title and text:
                self.comboBox.addItem(f"{title}: {text}")
    
        
    def view_announcements(self):
        self.comboBox.clear()  # Önceki duyuruları temizle
        self.load_announcements_from_json(self)  # Mevcut duyuruları yükle    
        
    def delete_announcement(self):
        index = self.comboBox.currentIndex()  # Seçilen öğenin indeksini al
        if index != -1:
            msg = QMessageBox.question(self, 'Delete Item', 'Are you sure you want to delete this announcement?',
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msg == QMessageBox.Yes:
                announcements = load_announcements()  
                announcements.pop(index)  
                save_announcements(announcements)  

            # ComboBox ve TextBrowser'ı temizle
                self.comboBox.removeItem(index)
                self.textBrowser.clear()

                QMessageBox.information(self, "Deleted", "Announcement deleted successfully.")


    def edit_announcement(self):
        index = self.comboBox.currentIndex()  
        if index != -1:
            saved_announcements = load_announcements()  
            msg = QMessageBox.question(self, 'Edit Item', 'Are you sure you want to edit this announcement?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msg == QMessageBox.Yes:
                text = self.textEdit.toPlainText()  
                title = self.LineEdit.text()  
                if text and title:  
                    saved_announcements[index]["text"] = text  
                    saved_announcements[index]["title"] = title  
                    save_announcements(saved_announcements)  
                    self.comboBox.setItemText(index, f"{title}: {text}")  
                    self.textBrowser.clear()  
                    self.textBrowser.append(f"{title}: {text}")  
                    self.textEdit.clear()  
                    self.LineEdit.clear()
                    QMessageBox.information(self, "Edited", "Announcement edited successfully.")

    def itemSelected(self, index):
        text = self.comboBox.currentText()
        self.textBrowser.clear()
        self.textBrowser.append(text)
        title, content = text.split(": ", 1)  # ':' işaretine göre bölüp title ve content'ı ayır
        self.LineEdit.setText(content)

    def view_announcements(self):
        index = self.comboBox.currentIndex()  
        if index != -1:
            saved_announcements = load_announcements()
            text = self.textEdit.toPlainText()  
            title = self.LineEdit.text()
            if text and title:  
                    saved_announcements[index]["text"] = text  
                    saved_announcements[index]["title"] = title  
                    save_announcements(saved_announcements)  
                    self.comboBox.setItemText(index, f"{title}: {text}")  
                    self.textBrowser.clear()  
                    self.textBrowser.append(f"{title}: {text}")  
                    self.textEdit.clear()  
                    self.LineEdit.clear()
                
    
###################################################################################################################################
## Part 9: Message Box Methods ##

    def add_message_tab(self):
        self.tabWidget.setCurrentIndex(8)
    
    def getMessages(self):
            try:
                with open('messages.json', "r") as messageFile:
                    data = json.load(messageFile)
                    self.messages = data
                
            except (json.JSONDecodeError, FileNotFoundError):
                pass
    def load_users(self):
        self.model2 = QStandardItemModel()
        self.listView_t.setModel(self.model2)
        try:
            with open('users.json', 'r') as file:
                users = json.load(file)
                for user in users:
                    if user["email"] != self.email:
                        item = QStandardItem(user['email'])
                        self.model2.appendRow(item)
                        #self.comboBox_t.addItem(user['email'])
                        for key in self.messages.keys():
                            if user['email'] in key:
                                if self.email in key:
                                    if self.messages[key]["unread-messages"] == True:
                                        item.setBackground(QColor('green'))
                                        pass
                                        #change background
        except FileNotFoundError:
            print("users.json dosyası bulunamadı.")
        except json.JSONDecodeError:
            print("users.json dosyası doğru biçimde değil.")


    def send_message(self):
        selected_email = ""
        selected_indexes = self.listView_t.selectedIndexes()
        for index in selected_indexes:
            item = self.model2.itemFromIndex(index)
            selected_email = item.text()
        sender = self.email
        message_text = self.LineEdit_3_t.text()


        message_id1 = sender+selected_email
        message_id2 = selected_email+sender

        msg_list = []
    
        if message_id1 in self.messages:
            msg_list = self.messages[message_id1]["messages"]
            saved_message = f"{sender}: {message_text}"
            msg_list.append(saved_message)
            self.message_display = msg_list
            self.messages[message_id1] = {
                "unread-messages": True,
                "messages":msg_list
                }
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)

        elif message_id2 in self.messages:
            msg_list = self.messages[message_id2]["messages"]
            saved_message = f"{sender}: {message_text}"
            msg_list.append(saved_message)
            self.messages[message_id2] = {
                "unread-messages": True,
                "messages":msg_list
                }
            self.message_display = msg_list
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)
        else:
            saved_message = f"{sender}: {message_text}"
            self.messages[message_id1] = {
                "unread-messages": True,
                "messages": [saved_message]
            }
            self.message_display = self.messages[message_id1]
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)
        # self.messageSelected()
        # self.read_message()

        self.model = QStandardItemModel()
        self.list_view_3_a.setModel(self.model)
        for message in msg_list:
            item = QStandardItem(message)  
            self.model.appendRow(item)

        self.list_view_3_t.setModel(self.model)




        if message_text and selected_email:
            # self.message_display.append(f"Sen: {message_text}")  # Gönderilen mesajı ekrana ekler
            # self.message_display.append(f"Gönderilen: {selected_email}")  # Gönderilen e-postayı ekrana ekler
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Mesaj Gönderildi!")
            msg_box.setText(f"Mesajınız '{message_text}' adresine gönderildi: {selected_email}")
            msg_box.exec()
    
    def messageSelected(self):
        self.model = QStandardItemModel()
        self.list_view_3_t.setModel(self.model)
        #message_receiver = self.comboBox_t.currentText()
        message_receiver=""
        
        id1 = self.email + message_receiver
        id2 = message_receiver + self.email
        
        msg_list = []
        
        if id1 in self.messages:
            msg_list = self.messages[id1]
    
        elif id2 in self.messages:
            msg_list = self.messages[id2]
        
        for message in msg_list:
            item = QStandardItem(message)  
            self.model.appendRow(item)
        self.list_view_3_t.setModel(self.model) 

    def read_message(self):
        self.model = QStandardItemModel()
        self.list_view_3_t.setModel(self.model)

        selected_indexes = self.listView_t.selectedIndexes()
        message_receiver = ""
        for index in selected_indexes:
            item = self.model2.itemFromIndex(index)
            item.setBackground(QColor("white"))
        for key in self.messages.keys():
                if self.email and item.text() in key:
                    self.messages[key]["unread-messages"] = False
                    message_receiver = item.text()

        
        # message_receiver = self.comboBox_3.currentText()
        
        id1 = self.email + message_receiver
        id2 = message_receiver + self.email
        
        msg_list = []
        
        if id1 in self.messages:
            msg_list = self.messages[id1]["messages"]
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)
                    
        elif id2 in self.messages:
            msg_list = self.messages[id2]["messages"]
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)


        for message in msg_list:
            item = QStandardItem(message)  
            self.model.appendRow(item)

        self.list_view_3_t.setModel(self.model)


###################################################################################################################################
## Part 10: To Do List Methods ##
    def add_todolist_tab(self):
        self.tabWidget.setCurrentIndex(7)
        self.view_todolist()
    
    def add_checkbox(self):
        text = self.line_edit.text()
        if text:
            item = QStandardItem(text)
            self.model.appendRow(item)
            self.save_todolist_to_json()

    def remove_checkbox(self):
        indexes = self.list_view.selectedIndexes()
        for index in sorted(indexes, reverse=True):
            self.model.removeRow(index.row())
        self.list_view.setModel(self.model)
        self.save_todolist_to_json()
    
    def load_todolist_from_json(self):
        try:
            with open('todolist.json', 'r') as todolist_file:
                checkbox_dict = json.load(todolist_file)
                for key, value in checkbox_dict.items():
                    item = QStandardItem(value)
                    self.model.appendRow(item)
                    self.list_view.setModel(self.model)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass



    def save_todolist_to_json(self):
        checkbox_dict = {}
        for i in range(self.model.rowCount()):
            checkbox_dict[i + 1] = self.model.item(i).text()
            self.list_view.setModel(self.model)
        with open('todolist.json', 'w') as todolist_file:
            json.dump(checkbox_dict, todolist_file, indent=4)
            
    def view_todolist(self):
        self.model = QStandardItemModel()
        self.list_view.setModel(self.model)
        
        todolist_data = load_todolist()
        for key, value in todolist_data.items():
            item = QStandardItem(f"{key}: {value}")
            self.model.appendRow(item)

###################################################################################################################################
        
class LoginApp(QDialog):
    def __init__(self):
        super(LoginApp, self).__init__()
        loadUi("login_form.ui", self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(self.show_reg)
        self.tb2.returnPressed.connect(self.login)
        
    def login(self):
        email = self.tb1.text()
        password = self.tb2.text()
        users = load_users()
        user = next((user for user in users if user['email'] == email and user['password'] == password), None)
        if user:
            widget.close()
            if is_admin(user):
                self.admin_app = AdminApp()
                self.admin_app.show()
                
            elif is_student(user):
                self.student_app = StudentApp(email)
                self.student_app.show()
                
            elif is_teacher(user):
                self.teacher_app = TeacherApp(email)
                self.teacher_app.show()
        
            else:
                QMessageBox.information(self, "Login Output", "Login Successful")
        else:
            QMessageBox.warning(self, "Login Output", "Invalid email or password")

    def show_reg(self):
        global widget
        widget.setCurrentIndex(1)

#############################################################################################################

class RegApp(QDialog):
    def __init__(self):
        super(RegApp, self).__init__()
        loadUi("register_form.ui", self)
        self.b3.clicked.connect(self.reg)
        self.b4.clicked.connect(self.show_login)
        self.fill_studentId()

    def fill_studentId(self):
        users = load_users()
        studentId = sum(1 for user in users if user.get('type') == 'student') + 1
        self.tb_sId.setText(str(studentId))
    
    def reg(self):
        studentId = self.tb_sId.text()
        email = self.tb3.text()
        password = self.tb4.text()
        name = self.tb5.text()
        surname = self.tb6.text()
        gender = self.cb1_reg.currentText()
        date_of_birth = self.tb7.text()
        phone = self.tb8.text()
        
        if not is_valid_email(email) or not is_valid_password(password) or not is_valid_phone(phone):
            QMessageBox.warning(self, "Registration Error", "Invalid input format")
            return

        users = load_users()
        if any(user['email'] == email for user in users):
            QMessageBox.warning(self, "Registration Error", "User Already Exists!!")
            return
        else:
            users.append({
                'studentId': studentId,
                'email': email,
                'password': password,
                'name': name,
                'surname': surname,
                'gender': gender,
                'date_of_birth': date_of_birth,
                'phone': phone,
                'type': 'student'
            })
            save_users(users)
            QMessageBox.information(self, "Registration Successful", "User Registered Successfully, YOU CAN NOW LOGIN!!")
            self.clear_registration_form()

    def clear_registration_form(self):
        self.tb_sId.clear()
        self.tb3.clear()
        self.tb4.clear()
        self.tb5.clear()
        self.tb6.clear()
        self.cb1_reg.setCurrentIndex(0)
        self.tb7.clear()
        self.tb8.clear()

    def show_login(self):
        global widget
        widget.setCurrentIndex(0)

#############################################################################################################
          
class StudentApp(QMainWindow):
    def __init__(self, email):
        super(StudentApp, self).__init__()
        loadUi("student.ui", self)
        self.email = email
        self.model = QStandardItemModel()
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.menu11.triggered.connect(self.edit_profile_tab)
        self.menu21_2.triggered.connect(self.view_course_schedule)
        self.menu22_2.triggered.connect(self.view_lesson_attendance)
        self.menu31_2.triggered.connect(self.view_meeting_schedule)
        self.menu32.triggered.connect(self.view_meeting_attendance)
        self.announcements_s.triggered.connect(self.view_announcements_tab)
        self.menu51_a.triggered.connect(self.view_todolist_tab)
        self.menu61_2.triggered.connect(self.add_message_tab)
        self.menu71.triggered.connect(self.close)
        # Logout from student menu

        self.b6.clicked.connect(self.update_student_details)  
        
        
        self.messages = dict()
        self.getMessages()
        self.load_users()
        self.sendButton3.clicked.connect(self.send_message)
        # self.comboBox_3.currentIndexChanged.connect(self.messageSelected)
        self.listView_4.clicked.connect(self.read_message)
        
        # Load initial data
        self.load_student_details()
        self.view_course_schedule()
        self.view_lesson_attendance()
        self.view_meeting_schedule()
        self.view_meeting_attendance()
        self.view_meeting_attendance()
        self.view_announcements()
        self.view_todolist()
        self.tabWidget.setCurrentIndex(0)
#################################################################################################################       
    def view_announcements_tab(self):
        self.tabWidget.setCurrentIndex(6)
        load_announcements()
        
    def view_announcements(self):
        self.tabWidget.setCurrentIndex
        self.textBrowser.clear()
        announcements = load_announcements()
        for announcement in announcements:
            title = announcement.get('title')
            text = announcement.get('text')
            if title and text:
                self.textBrowser.append(f"Title: {title}\n{text}\n\n")
#################################################################################################################
    def view_todolist_tab(self):
        self.tabWidget.setCurrentIndex(7)
        load_todolist()
        
    def view_todolist(self):
        self.model = QStandardItemModel()
        self.list_view.setModel(self.model)
        
        todolist_data = load_todolist()
        for key, value in todolist_data.items():
            item = QStandardItem(f"{key}: {value}")
            self.model.appendRow(item)

        

   
 #################################################################################################################       
    def edit_profile_tab(self):
        self.tabWidget.setCurrentIndex(1)
        self.load_student_details()

    def load_student_details(self):
        users = load_users()
        for user in users:
            if user.get('type') == 'student' and user['email'] == self.email:
                # Load the student's details into the form
                self.tb21.setText(user.get('studentId', ''))  
                self.tb22.setText(user.get('email', ''))  
                self.tb23.setText(user.get('name', ''))  
                self.tb24.setText(user.get('surname', ''))  
                self.cb11_st.setCurrentText(user.get('gender', ''))  
                self.tb25.setText(user.get('date_of_birth', ''))  
                self.tb26.setText(user.get('phone', ''))  
                self.tb27.setText(user.get('password', ''))  
                break

    def update_student_details(self):
        student_id = self.tb21.text()
        email = self.tb22.text()
        name = self.tb23.text()
        surname = self.tb24.text()
        gender = self.cb11_st.currentText()
        date_of_birth = self.tb25.text()
        phone = self.tb26.text()
        password = self.tb27.text()

        if not is_valid_email(email) or not is_valid_password(password) or not is_valid_phone(phone):
            QMessageBox.warning(self, "Update Error", "Invalid input format")
            return

        users = load_users()
        for i, user in enumerate(users):
            if user.get('type') == 'student' and user['email'] == self.email:
                users[i].update({
                    'studentId': student_id,
                    'email': email,
                    'name': name,
                    'surname': surname,
                    'gender': gender,
                    'date_of_birth': date_of_birth,
                    'phone': phone,
                    'password': password
                })
                break
        save_users(users)
        QMessageBox.information(self, "Update Success", "Student details updated successfully.")
#############################################################################################################
    def view_course_schedule(self):
            self.tabWidget.setCurrentIndex(2)
            lessons = load_lessons()
            if lessons:
                current_schedule = lessons[0]
                self.tb21_course.setText(current_schedule.get('date_lesson_1', ''))
                self.cb21_course.setCurrentText(current_schedule.get('time_slot_lesson_1', ''))
                self.tb22_course.setText(current_schedule.get('lesson_subject_lesson_1', ''))
                self.tb23_course.setText(current_schedule.get('date_lesson_2', ''))
                self.cb22_course.setCurrentText(current_schedule.get('time_slot_lesson_2', ''))
                self.tb24_course.setText(current_schedule.get('lesson_subject_lesson_2', ''))
                self.tb25_course.setText(current_schedule.get('date_lesson_3', ''))
                self.cb23_course.setCurrentText(current_schedule.get('time_slot_lesson_3', ''))
                self.tb26_course.setText(current_schedule.get('lesson_subject_lesson_3', ''))
                self.tb27_course.setText(current_schedule.get('date_lesson_4', ''))
                self.cb24_course.setCurrentText(current_schedule.get('time_slot_lesson_4', ''))
                self.tb28_course.setText(current_schedule.get('lesson_subject_lesson_4', ''))
                self.tb29_course.setText(current_schedule.get('date_lesson_5', ''))
                self.cb25_course.setCurrentText(current_schedule.get('time_slot_lesson_5', ''))
                self.tb210_course.setText(current_schedule.get('lesson_subject_lesson_5', ''))
                self.tb211_course.setText(current_schedule.get('date_lesson_6', ''))
                self.cb26_course.setCurrentText(current_schedule.get('time_slot_lesson_6', ''))
                self.tb212_course.setText(current_schedule.get('lesson_subject_lesson_6', ''))
                self.tb213_course.setText(current_schedule.get('date_lesson_7', ''))
                self.cb27_course.setCurrentText(current_schedule.get('time_slot_lesson_7', ''))
                self.tb214_course.setText(current_schedule.get('lesson_subject_lesson_7', ''))
                self.tb215_course.setText(current_schedule.get('date_lesson_8', ''))
                self.cb28_course.setCurrentText(current_schedule.get('time_slot_lesson_8', ''))
                self.tb216_course.setText(current_schedule.get('lesson_subject_lesson_8', ''))
                self.tb217_course.setText(current_schedule.get('date_lesson_9', ''))
                self.cb29_course.setCurrentText(current_schedule.get('time_slot_lesson_9', ''))
                self.tb218_course.setText(current_schedule.get('lesson_subject_lesson_9', ''))
                self.tb219_course.setText(current_schedule.get('date_lesson_10', ''))
                self.cb210_course.setCurrentText(current_schedule.get('time_slot_lesson_10', ''))
                self.tb220_course.setText(current_schedule.get('lesson_subject_lesson_10', ''))
                self.tb221_course.setText(current_schedule.get('date_lesson_11', ''))
                self.cb211_course.setCurrentText(current_schedule.get('time_slot_lesson_11', ''))
                self.tb222_course.setText(current_schedule.get('lesson_subject_lesson_11', ''))
                self.tb223_course.setText(current_schedule.get('date_lesson_12', ''))
                self.cb212_course.setCurrentText(current_schedule.get('time_slot_lesson_12', ''))
                self.tb224_course.setText(current_schedule.get('lesson_subject_lesson_12', ''))
                self.tb225_course.setText(current_schedule.get('date_lesson_13', ''))
                self.cb213_course.setCurrentText(current_schedule.get('time_slot_lesson_13', ''))
                self.tb226_course.setText(current_schedule.get('lesson_subject_lesson_13', ''))
                self.tb227_course.setText(current_schedule.get('date_lesson_14', ''))
                self.cb214_course.setCurrentText(current_schedule.get('time_slot_lesson_14', ''))
                self.tb228_course.setText(current_schedule.get('lesson_subject_lesson_14', ''))
                self.tb229_course.setText(current_schedule.get('date_lesson_15', ''))
                self.cb215_course.setCurrentText(current_schedule.get('time_slot_lesson_15', ''))
                self.tb230_course.setText(current_schedule.get('lesson_subject_lesson_15', ''))    

                # Set the UI elements to read-only
                self.tb21_course.setReadOnly(True)
                self.cb21_course.setDisabled(True)
                self.tb22_course.setReadOnly(True)
                self.tb23_course.setReadOnly(True)
                self.cb22_course.setDisabled(True)
                self.tb24_course.setReadOnly(True)
                self.tb25_course.setReadOnly(True)
                self.cb23_course.setDisabled(True)
                self.tb26_course.setReadOnly(True)
                self.tb27_course.setReadOnly(True)
                self.cb24_course.setDisabled(True)
                self.tb28_course.setReadOnly(True)
                self.tb29_course.setReadOnly(True)
                self.cb25_course.setDisabled(True)
                self.tb210_course.setReadOnly(True)
                self.tb211_course.setReadOnly(True)
                self.cb26_course.setDisabled(True)
                self.tb212_course.setReadOnly(True)
                self.tb213_course.setReadOnly(True)
                self.cb27_course.setDisabled(True)
                self.tb214_course.setReadOnly(True)
                self.tb215_course.setReadOnly(True)
                self.cb28_course.setDisabled(True)
                self.tb216_course.setReadOnly(True)
                self.tb217_course.setReadOnly(True)
                self.cb29_course.setDisabled(True)
                self.tb218_course.setReadOnly(True)
                self.tb219_course.setReadOnly(True)
                self.cb210_course.setDisabled(True)
                self.tb220_course.setReadOnly(True)
                self.tb221_course.setReadOnly(True)
                self.cb211_course.setDisabled(True)
                self.tb222_course.setReadOnly(True)
                self.tb223_course.setReadOnly(True)
                self.cb212_course.setDisabled(True)
                self.tb224_course.setReadOnly(True)
                self.tb225_course.setReadOnly(True)
                self.cb213_course.setDisabled(True)
                self.tb226_course.setReadOnly(True)
                self.tb227_course.setReadOnly(True)
                self.cb214_course.setDisabled(True)
                self.tb228_course.setReadOnly(True)
                self.tb229_course.setReadOnly(True)
                self.cb215_course.setDisabled(True)
                self.tb230_course.setReadOnly(True)
    
            else:
                QMessageBox.information(self, "Info", "No course schedule available.")
        
#################################################################################################################   
    def view_lesson_attendance(self):
            self.tabWidget.setCurrentIndex(3)
            attendance = load_attendance()
            student_attendance = attendance.get(self.email, {})  
                
            self.tb21_course_2.setText(student_attendance.get('date_lesson_1', ''))
            self.cb21_course_2.setCurrentText(student_attendance.get('time_slot_lesson_1', ''))
            self.cb22_t_50.setCurrentText(student_attendance.get('status_lesson_1', ''))
            self.tb23_course_2.setText(student_attendance.get('date_lesson_2', ''))
            self.cb22_course_2.setCurrentText(student_attendance.get('time_slot_lesson_2', ''))
            self.cb22_t_51.setCurrentText(student_attendance.get('status_lesson_2', ''))
            self.tb25_course_2.setText(student_attendance.get('date_lesson_3', ''))
            self.cb23_course_2.setCurrentText(student_attendance.get('time_slot_lesson_3', ''))
            self.cb22_t_52.setCurrentText(student_attendance.get('status_lesson_3', ''))
            self.tb27_course_2.setText(student_attendance.get('date_lesson_4', ''))
            self.cb24_course_2.setCurrentText(student_attendance.get('time_slot_lesson_4', ''))
            self.cb22_t_53.setCurrentText(student_attendance.get('status_lesson_4', ''))
            self.tb29_course_2.setText(student_attendance.get('date_lesson_5', ''))
            self.cb25_course_2.setCurrentText(student_attendance.get('time_slot_lesson_5', ''))
            self.cb22_t_54.setCurrentText(student_attendance.get('status_lesson_5', ''))
            self.tb211_course_2.setText(student_attendance.get('date_lesson_6', ''))
            self.cb26_course_2.setCurrentText(student_attendance.get('time_slot_lesson_6', ''))
            self.cb22_t_55.setCurrentText(student_attendance.get('status_lesson_6', ''))
            self.tb213_course_2.setText(student_attendance.get('date_lesson_7', ''))
            self.cb27_course_2.setCurrentText(student_attendance.get('time_slot_lesson_7', ''))
            self.cb22_t_56.setCurrentText(student_attendance.get('status_lesson_7', ''))
            self.tb215_course_2.setText(student_attendance.get('date_lesson_8', ''))
            self.cb28_course_2.setCurrentText(student_attendance.get('time_slot_lesson_8', ''))
            self.cb22_t_57.setCurrentText(student_attendance.get('status_lesson_8', ''))
            self.tb217_course_2.setText(student_attendance.get('date_lesson_9', ''))
            self.cb29_course_2.setCurrentText(student_attendance.get('time_slot_lesson_9', ''))
            self.cb22_t_58.setCurrentText(student_attendance.get('status_lesson_9', ''))
            self.tb219_course_2.setText(student_attendance.get('date_lesson_10', ''))
            self.cb210_course_2.setCurrentText(student_attendance.get('time_slot_lesson_10', ''))
            self.cb22_t_59.setCurrentText(student_attendance.get('status_lesson_10', ''))
            self.tb221_course_2.setText(student_attendance.get('date_lesson_11', ''))
            self.cb211_course_2.setCurrentText(student_attendance.get('time_slot_lesson_11', ''))
            self.cb22_t_60.setCurrentText(student_attendance.get('status_lesson_11', ''))
            self.tb223_course_2.setText(student_attendance.get('date_lesson_12', ''))
            self.cb212_course_2.setCurrentText(student_attendance.get('time_slot_lesson_12', ''))
            self.cb22_t_61.setCurrentText(student_attendance.get('status_lesson_12', ''))
            self.tb225_course_2.setText(student_attendance.get('date_lesson_13', ''))
            self.cb213_course_2.setCurrentText(student_attendance.get('time_slot_lesson_13', ''))
            self.cb22_t_62.setCurrentText(student_attendance.get('  status_lesson_13', ''))
            self.tb227_course_2.setText(student_attendance.get('date_lesson_14', ''))
            self.cb214_course_2.setCurrentText(student_attendance.get('time_slot_lesson_14', ''))
            self.cb22_t_63.setCurrentText(student_attendance.get('status_lesson_14', ''))
            self.tb229_course_2.setText(student_attendance.get('date_lesson_15', ''))
            self.cb215_course_2.setCurrentText(student_attendance.get('time_slot_lesson_15', ''))
            self.cb22_t_64.setCurrentText(student_attendance.get('status_lesson_15', ''))
            
            
            self.tb21_course_2.setReadOnly(True)
            self.cb21_course_2.setDisabled(True)
            self.cb22_t_50.setDisabled(True)
            self.tb23_course_2.setReadOnly(True)
            self.cb22_course_2.setDisabled(True)
            self.cb22_t_51.setDisabled(True)
            self.tb25_course_2.setReadOnly(True)
            self.cb23_course_2.setDisabled(True)
            self.cb22_t_52.setDisabled(True)
            self.tb27_course_2.setReadOnly(True)
            self.cb24_course_2.setDisabled(True)
            self.cb22_t_53.setDisabled(True)
            self.tb29_course_2.setReadOnly(True)
            self.cb25_course_2.setDisabled(True)
            self.cb22_t_54.setDisabled(True)
            self.tb211_course_2.setReadOnly(True)
            self.cb26_course_2.setDisabled(True)
            self.cb22_t_55.setDisabled(True)
            self.tb213_course_2.setReadOnly(True)
            self.cb27_course_2.setDisabled(True)
            self.cb22_t_56.setDisabled(True)
            self.tb215_course_2.setReadOnly(True)
            self.cb28_course_2.setDisabled(True)
            self.cb22_t_57.setDisabled(True)
            self.tb217_course_2.setReadOnly(True)
            self.cb29_course_2.setDisabled(True)
            self.cb22_t_58.setDisabled(True)
            self.tb219_course_2.setReadOnly(True)
            self.cb210_course_2.setDisabled(True)
            self.cb22_t_59.setDisabled(True)
            self.tb221_course_2.setReadOnly(True)
            self.cb211_course_2.setDisabled(True)
            self.cb22_t_60.setDisabled(True)
            self.tb223_course_2.setReadOnly(True)
            self.cb212_course_2.setDisabled(True)
            self.cb22_t_61.setDisabled(True)
            self.tb225_course_2.setReadOnly(True)
            self.cb213_course_2.setDisabled(True)
            self.cb22_t_62.setDisabled(True)
            self.tb227_course_2.setReadOnly(True)
            self.cb214_course_2.setDisabled(True)
            self.cb22_t_63.setDisabled(True)
            self.tb229_course_2.setReadOnly(True)
            self.cb215_course_2.setDisabled(True)
            self.cb22_t_64.setDisabled(True)


            if not student_attendance:
                self.loadCurrentSchedule
                
            
            
        
    def loadCurrentSchedule(self):
            lessons = load_lessons()
            if not lessons:
                QMessageBox.information(self, "Load Schedule", "No existing schedule found.")
                return

            current_schedule = lessons[0]

            self.tb21_course_2.setText(current_schedule.get('date_lesson_1', ''))
            self.cb21_course_2.setCurrentText(current_schedule.get('time_slot_lesson_1', ''))
            self.tb23_course_2.setText(current_schedule.get('date_lesson_2', ''))
            self.cb22_course_2.setCurrentText(current_schedule.get('time_slot_lesson_2', ''))
            self.tb25_course_2.setText(current_schedule.get('date_lesson_3', ''))
            self.cb23_course_2.setCurrentText(current_schedule.get('time_slot_lesson_3', ''))
            self.tb27_course_2.setText(current_schedule.get('date_lesson_4', ''))
            self.cb24_course_2.setCurrentText(current_schedule.get('time_slot_lesson_4', ''))
            self.tb29_course_2.setText(current_schedule.get('date_lesson_5', ''))
            self.cb25_course_2.setCurrentText(current_schedule.get('time_slot_lesson_5', ''))
            self.tb211_course_2.setText(current_schedule.get('date_lesson_6', ''))
            self.cb26_course_2.setCurrentText(current_schedule.get('time_slot_lesson_6', ''))
            self.tb213_course_2.setText(current_schedule.get('date_lesson_7', ''))
            self.cb27_course_2.setCurrentText(current_schedule.get('time_slot_lesson_7', ''))
            self.tb215_course_2.setText(current_schedule.get('date_lesson_8', ''))
            self.cb28_course_2.setCurrentText(current_schedule.get('time_slot_lesson_8', ''))
            self.tb217_course_2.setText(current_schedule.get('date_lesson_9', ''))
            self.cb29_course_2.setCurrentText(current_schedule.get('time_slot_lesson_9', ''))
            self.tb219_course_2.setText(current_schedule.get('date_lesson_10', ''))
            self.cb210_course_2.setCurrentText(current_schedule.get('time_slot_lesson_10', ''))
            self.tb221_course_2.setText(current_schedule.get('date_lesson_11', ''))
            self.cb211_course_2.setCurrentText(current_schedule.get('time_slot_lesson_11', ''))
            self.tb223_course_2.setText(current_schedule.get('date_lesson_12', ''))
            self.cb212_course_2.setCurrentText(current_schedule.get('time_slot_lesson_12', ''))
            self.tb225_course_2.setText(current_schedule.get('date_lesson_13', ''))
            self.cb213_course_2.setCurrentText(current_schedule.get('time_slot_lesson_13', ''))
            self.tb227_course_2.setText(current_schedule.get('date_lesson_14', ''))
            self.cb214_course_2.setCurrentText(current_schedule.get('time_slot_lesson_14', ''))
            self.tb229_course_2.setText(current_schedule.get('date_lesson_15', ''))
            self.cb215_course_2.setCurrentText(current_schedule.get('time_slot_lesson_15', ''))
            
            
            self.tb21_course_2.setReadOnly(True)
            self.cb21_course_2.setDisabled(True)
            self.cb22_t_50.setDisabled(True)
            self.tb23_course_2.setReadOnly(True)
            self.cb22_course_2.setDisabled(True)
            self.cb22_t_51.setDisabled(True)
            self.tb25_course_2.setReadOnly(True)
            self.cb23_course_2.setDisabled(True)
            self.cb22_t_52.setDisabled(True)
            self.tb27_course_2.setReadOnly(True)
            self.cb24_course_2.setDisabled(True)
            self.cb22_t_53.setDisabled(True)
            self.tb29_course_2.setReadOnly(True)
            self.cb25_course_2.setDisabled(True)
            self.cb22_t_54.setDisabled(True)
            self.tb211_course_2.setReadOnly(True)
            self.cb26_course_2.setDisabled(True)
            self.cb22_t_55.setDisabled(True)
            self.tb213_course_2.setReadOnly(True)
            self.cb27_course_2.setDisabled(True)
            self.cb22_t_56.setDisabled(True)
            self.tb215_course_2.setReadOnly(True)
            self.cb28_course_2.setDisabled(True)
            self.cb22_t_57.setDisabled(True)
            self.tb217_course_2.setReadOnly(True)
            self.cb29_course_2.setDisabled(True)
            self.cb22_t_58.setDisabled(True)
            self.tb219_course_2.setReadOnly(True)
            self.cb210_course_2.setDisabled(True)
            self.cb22_t_59.setDisabled(True)
            self.tb221_course_2.setReadOnly(True)
            self.cb211_course_2.setDisabled(True)
            self.cb22_t_60.setDisabled(True)
            self.tb223_course_2.setReadOnly(True)
            self.cb212_course_2.setDisabled(True)
            self.cb22_t_61.setDisabled(True)
            self.tb225_course_2.setReadOnly(True)
            self.cb213_course_2.setDisabled(True)
            self.cb22_t_62.setDisabled(True)
            self.tb227_course_2.setReadOnly(True)
            self.cb214_course_2.setDisabled(True)
            self.cb22_t_63.setDisabled(True)
            self.tb229_course_2.setReadOnly(True)
            self.cb215_course_2.setDisabled(True)
            self.cb22_t_64.setDisabled(True)
 #################################################################################################################

#############################################################################################################
    def view_meeting_schedule(self):
            self.tabWidget.setCurrentIndex(4)
            meetings = load_meetings()
            if meetings:
                current_meeting_schedule = meetings[0]
                self.tb21_course_7.setText(current_meeting_schedule.get('date_meeting_1', ''))
                self.cb21_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_1', ''))
                self.tb22_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_1', ''))
                self.tb23_course_7.setText(current_meeting_schedule.get('date_meeting_2', ''))
                self.cb22_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_2', ''))
                self.tb24_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_2', ''))
                self.tb25_course_7.setText(current_meeting_schedule.get('date_meeting_3', ''))
                self.cb23_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_3', ''))
                self.tb26_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_3', ''))
                self.tb27_course_7.setText(current_meeting_schedule.get('date_meeting_4', ''))
                self.cb24_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_4', ''))
                self.tb28_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_4', ''))
                self.tb29_course_7.setText(current_meeting_schedule.get('date_meeting_5', ''))
                self.cb25_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_5', ''))
                self.tb210_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_5', ''))
                self.tb211_course_7.setText(current_meeting_schedule.get('date_meeting_6', ''))
                self.cb26_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_6', ''))
                self.tb212_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_6', ''))
                self.tb213_course_7.setText(current_meeting_schedule.get('date_meeting_7', ''))
                self.cb27_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_7', ''))
                self.tb214_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_7', ''))
                self.tb215_course_7.setText(current_meeting_schedule.get('date_meeting_8', ''))
                self.cb28_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_8', ''))
                self.tb216_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_8', ''))
                self.tb217_course_7.setText(current_meeting_schedule.get('date_meeting_9', ''))
                self.cb29_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_9', ''))
                self.tb218_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_9', ''))
                self.tb219_course_7.setText(current_meeting_schedule.get('date_meeting_10', ''))
                self.cb210_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_10', ''))
                self.tb220_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_10', ''))
                self.tb221_course_7.setText(current_meeting_schedule.get('date_meeting_11', ''))
                self.cb211_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_11', ''))
                self.tb222_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_11', ''))
                self.tb223_course_7.setText(current_meeting_schedule.get('date_meeting_12', ''))
                self.cb212_course.setCurrentText(current_meeting_schedule.get('time_slot_meeting_12', ''))
                self.tb224_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_12', ''))
                self.tb225_course_7.setText(current_meeting_schedule.get('date_meeting_13', ''))
                self.cb213_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_13', ''))
                self.tb226_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_13', ''))
                self.tb227_course_7.setText(current_meeting_schedule.get('date_meeting_14', ''))
                self.cb214_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_14', ''))
                self.tb228_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_14', ''))
                self.tb229_course_7.setText(current_meeting_schedule.get('date_meeting_15', ''))
                self.cb215_course_7.setCurrentText(current_meeting_schedule.get('time_slot_meeting_15', ''))
                self.tb230_course_4.setText(current_meeting_schedule.get('meeting_subject_meeting_15', ''))    
            

                # Set the UI elements to read-only
                self.tb21_course_7.setReadOnly(True)
                self.cb21_course_7.setDisabled(True)
                self.tb22_course_4.setReadOnly(True)
                self.tb23_course_7.setReadOnly(True)
                self.cb22_course_7.setDisabled(True)
                self.tb24_course_4.setReadOnly(True)
                self.tb25_course_7.setReadOnly(True)
                self.cb23_course_7.setDisabled(True)
                self.tb26_course_4.setReadOnly(True)
                self.tb27_course_7.setReadOnly(True)
                self.cb24_course_7.setDisabled(True)
                self.tb28_course_4.setReadOnly(True)
                self.tb29_course_7.setReadOnly(True)
                self.cb25_course_7.setDisabled(True)
                self.tb210_course_4.setReadOnly(True)
                self.tb211_course_7.setReadOnly(True)
                self.cb26_course_7.setDisabled(True)
                self.tb212_course_4.setReadOnly(True)
                self.tb213_course_7.setReadOnly(True)
                self.cb27_course_7.setDisabled(True)
                self.tb214_course_4.setReadOnly(True)
                self.tb215_course_7.setReadOnly(True)
                self.cb28_course_7.setDisabled(True)
                self.tb216_course_4.setReadOnly(True)
                self.tb217_course_7.setReadOnly(True)
                self.cb29_course_7.setDisabled(True)
                self.tb218_course_4.setReadOnly(True)
                self.tb219_course_7.setReadOnly(True)
                self.cb210_course_7.setDisabled(True)
                self.tb220_course_4.setReadOnly(True)
                self.tb221_course_7.setReadOnly(True)
                self.cb211_course_7.setDisabled(True)
                self.tb222_course_4.setReadOnly(True)
                self.tb223_course_7.setReadOnly(True)
                self.cb212_course_7.setDisabled(True)
                self.tb224_course_4.setReadOnly(True)
                self.tb225_course_7.setReadOnly(True)
                self.cb213_course_7.setDisabled(True)
                self.tb226_course_4.setReadOnly(True)
                self.tb227_course_7.setReadOnly(True)
                self.cb214_course_7.setDisabled(True)
                self.tb228_course_4.setReadOnly(True)
                self.tb229_course_7.setReadOnly(True)
                self.cb215_course_7.setDisabled(True)
                self.tb230_course_4.setReadOnly(True)
    
            else:
                QMessageBox.information(self, "Info", "No meeting schedule available.")
        
#################################################################################################################   
    def view_meeting_attendance(self):
            self.tabWidget.setCurrentIndex(5)
            meeting_attendance = load_meeting_attendance()
            student_meeting_attendance = meeting_attendance.get(self.email, {})  
                
            self.tb21_course_12.setText(student_meeting_attendance.get('date_meeting_1', ''))
            self.cb21_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_1', ''))
            self.cb22_t_140.setCurrentText(student_meeting_attendance.get('status_meeting_1', ''))
            self.tb23_course_12.setText(student_meeting_attendance.get('date_meeting_2', ''))
            self.cb22_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_2', ''))
            self.cb22_t_138.setCurrentText(student_meeting_attendance.get('status_meeting_2', ''))
            self.tb25_course_12.setText(student_meeting_attendance.get('date_meeting_3', ''))
            self.cb23_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_3', ''))
            self.cb22_t_132.setCurrentText(student_meeting_attendance.get('status_meeting_3', ''))
            self.tb27_course_12.setText(student_meeting_attendance.get('date_meeting_4', ''))
            self.cb24_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_4', ''))
            self.cb22_t_136.setCurrentText(student_meeting_attendance.get('status_meeting_4', ''))
            self.tb29_course_12.setText(student_meeting_attendance.get('date_meeting_5', ''))
            self.cb25_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_5', ''))
            self.cb22_t_133.setCurrentText(student_meeting_attendance.get('status_meeting_5', ''))
            self.tb211_course_12.setText(student_meeting_attendance.get('date_meeting_6', ''))
            self.cb26_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_6', ''))
            self.cb22_t_141.setCurrentText(student_meeting_attendance.get('status_meeting_6', ''))
            self.tb213_course_12.setText(student_meeting_attendance.get('date_meeting_7', ''))
            self.cb27_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_7', ''))
            self.cb22_t_139.setCurrentText(student_meeting_attendance.get('status_meeting_7', ''))
            self.tb215_course_12.setText(student_meeting_attendance.get('date_meeting_8', ''))
            self.cb28_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_8', ''))
            self.cb22_t_142.setCurrentText(student_meeting_attendance.get('status_meeting_8', ''))
            self.tb217_course_12.setText(student_meeting_attendance.get('date_meeting_9', ''))
            self.cb29_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_9', ''))
            self.cb22_t_130.setCurrentText(student_meeting_attendance.get('status_meeting_9', ''))
            self.tb219_course_12.setText(student_meeting_attendance.get('date_meeting_10', ''))
            self.cb210_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_10', ''))
            self.cb22_t_135.setCurrentText(student_meeting_attendance.get('status_meeting_10', ''))
            self.tb221_course_12.setText(student_meeting_attendance.get('date_meeting_11', ''))
            self.cb211_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_11', ''))
            self.cb22_t_128.setCurrentText(student_meeting_attendance.get('status_meeting_11', ''))
            self.tb223_course_12.setText(student_meeting_attendance.get('date_meeting_12', ''))
            self.cb212_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_12', ''))
            self.cb22_t_137.setCurrentText(student_meeting_attendance.get('status_meeting_12', ''))
            self.tb225_course_12.setText(student_meeting_attendance.get('date_meeting_13', ''))
            self.cb213_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_13', ''))
            self.cb22_t_131.setCurrentText(student_meeting_attendance.get('  status_meeting_13', ''))
            self.tb227_course_12.setText(student_meeting_attendance.get('date_meeting_14', ''))
            self.cb214_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_14', ''))
            self.cb22_t_129.setCurrentText(student_meeting_attendance.get('status_meeting_14', ''))
            self.tb229_course_12.setText(student_meeting_attendance.get('date_meeting_15', ''))
            self.cb215_course_12.setCurrentText(student_meeting_attendance.get('time_slot_meeting_15', ''))
            self.cb22_t_134.setCurrentText(student_meeting_attendance.get('status_meeting_15', ''))

            
            
            self.tb21_course_12.setReadOnly(True)
            self.cb21_course_12.setDisabled(True)
            self.cb22_t_140.setDisabled(True)
            self.tb23_course_12.setReadOnly(True)
            self.cb22_course_12.setDisabled(True)
            self.cb22_t_138.setDisabled(True)
            self.tb25_course_12.setReadOnly(True)
            self.cb23_course_12.setDisabled(True)
            self.cb22_t_132.setDisabled(True)
            self.tb27_course_12.setReadOnly(True)
            self.cb24_course_12.setDisabled(True)
            self.cb22_t_136.setDisabled(True)
            self.tb29_course_12.setReadOnly(True)
            self.cb25_course_12.setDisabled(True)
            self.cb22_t_133.setDisabled(True)
            self.tb211_course_12.setReadOnly(True)
            self.cb26_course_12.setDisabled(True)
            self.cb22_t_141.setDisabled(True)
            self.tb213_course_12.setReadOnly(True)
            self.cb27_course_12.setDisabled(True)
            self.cb22_t_139.setDisabled(True)
            self.tb215_course_12.setReadOnly(True)
            self.cb28_course_12.setDisabled(True)
            self.cb22_t_142.setDisabled(True)
            self.tb217_course_12.setReadOnly(True)
            self.cb29_course_12.setDisabled(True)
            self.cb22_t_130.setDisabled(True)
            self.tb219_course_12.setReadOnly(True)
            self.cb210_course_12.setDisabled(True)
            self.cb22_t_135.setDisabled(True)
            self.tb221_course_12.setReadOnly(True)
            self.cb211_course_12.setDisabled(True)
            self.cb22_t_128.setDisabled(True)
            self.tb223_course_12.setReadOnly(True)
            self.cb212_course_12.setDisabled(True)
            self.cb22_t_137.setDisabled(True)
            self.tb225_course_12.setReadOnly(True)
            self.cb213_course_12.setDisabled(True)
            self.cb22_t_131.setDisabled(True)
            self.tb227_course_12.setReadOnly(True)
            self.cb214_course_12.setDisabled(True)
            self.cb22_t_129.setDisabled(True)
            self.tb229_course_12.setReadOnly(True)
            self.cb215_course_12.setDisabled(True)
            self.cb22_t_134.setDisabled(True)


            if not student_meeting_attendance:
                self.loadCurrentSchedule
                     
    def loadCurrentSchedule(self):
            lessons = load_lessons()
            if not lessons:
                QMessageBox.information(self, "Load Schedule", "No existing schedule found.")
                return

            current_schedule = lessons[0]

            self.tb21_course_12.setText(current_schedule.get('date_meeting_1', ''))
            self.cb21_course_12.setCurrentText(current_schedule.get('time_slot_meeting_1', ''))
            self.tb23_course_12.setText(current_schedule.get('date_meeting_2', ''))
            self.cb22_course_12.setCurrentText(current_schedule.get('time_slot_meeting_2', ''))
            self.tb25_course_12.setText(current_schedule.get('date_meeting_3', ''))
            self.cb23_course_12.setCurrentText(current_schedule.get('time_slot_meeting_3', ''))
            self.tb27_course_12.setText(current_schedule.get('date_meeting_4', ''))
            self.cb24_course_12.setCurrentText(current_schedule.get('time_slot_meeting_4', ''))
            self.tb29_course_12.setText(current_schedule.get('date_meeting_5', ''))
            self.cb25_course_12.setCurrentText(current_schedule.get('time_slot_meeting_5', ''))
            self.tb211_course_12.setText(current_schedule.get('date_meeting_6', ''))
            self.cb26_course_12.setCurrentText(current_schedule.get('time_slot_meeting_6', ''))
            self.tb213_course_12.setText(current_schedule.get('date_meeting_7', ''))
            self.cb27_course_12.setCurrentText(current_schedule.get('time_slot_meeting_7', ''))
            self.tb215_course_12.setText(current_schedule.get('date_meeting_8', ''))
            self.cb28_course_12.setCurrentText(current_schedule.get('time_slot_meeting_8', ''))
            self.tb217_course_12.setText(current_schedule.get('date_meeting_9', ''))
            self.cb29_course_12.setCurrentText(current_schedule.get('time_slot_meeting_9', ''))
            self.tb219_course_12.setText(current_schedule.get('date_meeting_10', ''))
            self.cb210_course_12.setCurrentText(current_schedule.get('time_slot_meeting_10', ''))
            self.tb221_course_12.setText(current_schedule.get('date_meeting_11', ''))
            self.cb211_course_12.setCurrentText(current_schedule.get('time_slot_meeting_11', ''))
            self.tb223_course_12.setText(current_schedule.get('date_meeting_12', ''))
            self.cb212_course_12.setCurrentText(current_schedule.get('time_slot_meeting_12', ''))
            self.tb225_course_12.setText(current_schedule.get('date_meeting_13', ''))
            self.cb213_course_12.setCurrentText(current_schedule.get('time_slot_meeting_13', ''))
            self.tb227_course_12.setText(current_schedule.get('date_meeting_14', ''))
            self.cb214_course_12.setCurrentText(current_schedule.get('time_slot_meeting_14', ''))
            self.tb229_course_12.setText(current_schedule.get('date_meeting_15', ''))
            self.cb215_course_12.setCurrentText(current_schedule.get('time_slot_meeting_15', ''))
            
            
            self.tb21_course_12.setReadOnly(True)
            self.cb21_course_12.setDisabled(True)
            self.cb22_t_140.setDisabled(True)
            self.tb23_course_12.setReadOnly(True)
            self.cb22_course_12.setDisabled(True)
            self.cb22_t_138.setDisabled(True)
            self.tb25_course_12.setReadOnly(True)
            self.cb23_course_12.setDisabled(True)
            self.cb22_t_132.setDisabled(True)
            self.tb27_course_12.setReadOnly(True)
            self.cb24_course_12.setDisabled(True)
            self.cb22_t_136.setDisabled(True)
            self.tb29_course_12.setReadOnly(True)
            self.cb25_course_12.setDisabled(True)
            self.cb22_t_133.setDisabled(True)
            self.tb211_course_12.setReadOnly(True)
            self.cb26_course_12.setDisabled(True)
            self.cb22_t_141.setDisabled(True)
            self.tb213_course_12.setReadOnly(True)
            self.cb27_course_12.setDisabled(True)
            self.cb22_t_139.setDisabled(True)
            self.tb215_course_12.setReadOnly(True)
            self.cb28_course_12.setDisabled(True)
            self.cb22_t_142.setDisabled(True)
            self.tb217_course_12.setReadOnly(True)
            self.cb29_course_12.setDisabled(True)
            self.cb22_t_130.setDisabled(True)
            self.tb219_course_12.setReadOnly(True)
            self.cb210_course_12.setDisabled(True)
            self.cb22_t_135.setDisabled(True)
            self.tb221_course_12.setReadOnly(True)
            self.cb211_course_12.setDisabled(True)
            self.cb22_t_128.setDisabled(True)
            self.tb223_course_12.setReadOnly(True)
            self.cb212_course_12.setDisabled(True)
            self.cb22_t_137.setDisabled(True)
            self.tb225_course_12.setReadOnly(True)
            self.cb213_course_12.setDisabled(True)
            self.cb22_t_131.setDisabled(True)
            self.tb227_course_12.setReadOnly(True)
            self.cb214_course_12.setDisabled(True)
            self.cb22_t_129.setDisabled(True)
            self.tb229_course_12.setReadOnly(True)
            self.cb215_course_12.setDisabled(True)
            self.cb22_t_134.setDisabled(True)
#################################################################################################################
    def add_message_tab(self):
        self.tabWidget.setCurrentIndex(8)
    
    def getMessages(self):
            try:
                with open('messages.json', "r") as messageFile:
                    data = json.load(messageFile)
                    self.messages = data
                
            except (json.JSONDecodeError, FileNotFoundError):
                pass
    def load_users(self):
        self.model2 = QStandardItemModel()
        self.listView_4.setModel(self.model2)
        try:
            with open('users.json', 'r') as file:
                users = json.load(file)
                for user in users:
                    if user["email"] != self.email:
                        item = QStandardItem(user['email'])
                        self.model2.appendRow(item)
                        #self.comboBox_3.addItem(user['email'])
                        for key in self.messages.keys():
                            if user['email'] in key:
                                if self.email in key:
                                    if self.messages[key]["unread-messages"] == True:
                                        item.setBackground(QColor('green'))
                                        pass
                                    #change background
        except FileNotFoundError:
            print("users.json dosyası bulunamadı.")
        except json.JSONDecodeError:
            print("users.json dosyası doğru biçimde değil.")


    def send_message(self):
        selected_email = ""
        selected_indexes = self.listView_4.selectedIndexes()
        for index in selected_indexes:
            item = self.model2.itemFromIndex(index)
            selected_email = item.text()
        sender = self.email
        message_text = self.LineEdit_3.text()


        message_id1 = sender+selected_email
        message_id2 = selected_email+sender

        msg_list = []

    
        if message_id1 in self.messages:
            msg_list = self.messages[message_id1]["messages"]
            saved_message = f"{sender}: {message_text}"
            msg_list.append(saved_message)
            self.message_display = msg_list
            self.messages[message_id1] = {
                "unread-messages": True,
                "messages":msg_list
                }
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)

        elif message_id2 in self.messages:
            msg_list = self.messages[message_id2]["messages"]
            saved_message = f"{sender}: {message_text}"
            msg_list.append(saved_message)
            self.messages[message_id2] = {
                "unread-messages": True,
                "messages":msg_list
                }
            self.message_display = msg_list
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)
        else:
            saved_message = f"{sender}: {message_text}"
            self.messages[message_id1] = {
                "unread-messages": True,
                "messages": [saved_message]
            }
            self.message_display = self.messages[message_id1]
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)
        # self.messageSelected()
        # self.read_message()
                
        
        self.model = QStandardItemModel()
        self.list_view_3.setModel(self.model)
        for message in msg_list:
            item = QStandardItem(message)  
            self.model.appendRow(item)

        self.list_view_3_a.setModel(self.model)




        if message_text and selected_email:
            # self.message_display.append(f"Sen: {message_text}")  # Gönderilen mesajı ekrana ekler
            # self.message_display.append(f"Gönderilen: {selected_email}")  # Gönderilen e-postayı ekrana ekler
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Mesaj Gönderildi!")
            msg_box.setText(f"Mesajınız '{message_text}' adresine gönderildi: {selected_email}")
            msg_box.exec()
    
    def messageSelected(self):
        self.model = QStandardItemModel()
        self.list_view_3.setModel(self.model)
        #message_receiver = self.comboBox_3.currentText()
        message_receiver =""
        
        id1 = self.email + message_receiver
        id2 = message_receiver + self.email
        
        msg_list = []
        
        if id1 in self.messages:
            msg_list = self.messages[id1]
    
        elif id2 in self.messages:
            msg_list = self.messages[id2]
        
        for message in msg_list:
            item = QStandardItem(message)  
            self.model.appendRow(item)
        self.list_view_3.setModel(self.model) 

    def read_message(self):
        self.model = QStandardItemModel()
        self.list_view_3.setModel(self.model)

        selected_indexes = self.listView_4.selectedIndexes()
        message_receiver = ""
        for index in selected_indexes:
            item = self.model2.itemFromIndex(index)
            item.setBackground(QColor("white"))
        for key in self.messages.keys():
                if self.email and item.text() in key:
                    self.messages[key]["unread-messages"] = False
                    message_receiver = item.text()

        
        # message_receiver = self.comboBox_3.currentText()
        
        id1 = self.email + message_receiver
        id2 = message_receiver + self.email
        
        msg_list = []
        
        if id1 in self.messages:
            msg_list = self.messages[id1]["messages"]
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)
                    
        elif id2 in self.messages:
            msg_list = self.messages[id2]["messages"]
            with open("messages.json", "w") as messageFile:
                json.dump(self.messages, messageFile, indent=2)


        for message in msg_list:
            item = QStandardItem(message)  
            self.model.appendRow(item)

        self.list_view_3.setModel(self.model)



















 #################################################################################################################

        
 #################################################################################################################
# Main Application Setup
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login_form = LoginApp()
    registration_form = RegApp()
    email = "admin@admin.com"
    student_form = StudentApp(email)
    teacher_form = TeacherApp(email)
    

    widget.addWidget(login_form)
    widget.addWidget(registration_form)
    widget.addWidget(student_form)
    widget.addWidget(teacher_form)
    widget.setFixedWidth(400)
    widget.setFixedHeight(650)
    widget.show()
    sys.exit(app.exec_())
    
#############################################################################################################