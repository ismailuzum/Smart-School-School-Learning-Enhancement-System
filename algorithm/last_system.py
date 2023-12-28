import json
import re
from last_user import *

class SchoolManagementSystem():
    def __init__(self):
        self.users = []
        self.admin_num = 0
        self.teacher_num = 0
        self.student_num = 0

    def get_users(self, file_name):
        try:
            with open(file_name, "r") as userFile:
                data = json.load(userFile)
                for user_data in data:
                    if user_data["user_status"] == "student":
                        user = Student(**user_data)
                        self.users.append(user)
                        self.student_num +=1
                    elif user_data["user_status"] == "teacher":
                        user = Teacher(**user_data)
                        self.users.append(user)
                        self.teacher_num +=1
                    elif user_data["user_status"] == "admin":
                        user = Admin(**user_data)
                        self.users.append(user)
                        self.admin_num +=1  
        except (json.JSONDecodeError, FileNotFoundError):
            pass


    def post_users(self, file_name):
        with open(file_name, "w") as userFile:
            data = []
            for user in self.users:
                if user.user_status == "student":
                    new_data = {
                     "first_name": user.first_name,
                     "last_name": user.last_name,
                     "email": user.email,
                     "password": user.password,
                     "user_status": user.user_status,
                     f"{user.user_status}_id": user.student_id
                    }
                    data.append(new_data) 
                elif user.user_status == "teacher":
                    new_data = {
                     "first_name": user.first_name,
                     "last_name": user.last_name,
                     "email": user.email,
                     "password": user.password,
                     "user_status": user.user_status,
                     f"{user.user_status}_id": user.teacher_id
                    }
                    data.append(new_data) 
                if user.user_status == "admin":
                    new_data = {
                     "first_name": user.first_name,
                     "last_name": user.last_name,
                     "email": user.email,
                     "password": user.password,
                     "user_status": user.user_status,
                     f"{user.user_status}_id": user.admin_id
                    }
                    data.append(new_data) 
            json.dump(data, userFile, indent=2)

    def loginRequest(self, email, password):
        for user in self.users:
            if user.email == email:
                if user.password == password:
                    print(f"Welcome {user.first_name} {user.last_name}")
                    return user
                else:
                    print("Wrong Password")
        print("There is no user matched with this email.")
        return None
    
    def registerRequest(self, first_name, last_name, email, password, user_status):
        if user_status == "student":
            new_student = Student(first_name, last_name, email, password, "student", self.student_num+1)
            self.users.append(new_student)
            self.student_num += 1
        elif user_status == "teacher":
            new_teacher = Teacher(first_name, last_name, email, password, "teacher", self.teacher_num+1)
            self.users.append(new_teacher)
            self.teacher_num += 1
        elif user_status == "admin":
            new_admin = Admin(first_name, last_name, email, password, "admin", self.admin_num+1)
            self.users.append(new_admin)
            self.admin_num += 1

    def passwordValidator(self, password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}[\]:;<>,.?/~\\-]).{8,}$"
        if re.match(pattern, password):
            return True
        return False
    
    def emailValidator(self, email):
        pattern = r"^([a-zA-Z0-9_.+-]+)@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$"

        if re.match(pattern, email):
            return True
        return False
    
    def isEmailUnique(self, email):
        for user in self.users:
            if user.email == email:
                    return False
        return True

    
    def editRequest(self, email, user, **kwargs):
        teacher = next((teacher for teacher in self.users if teacher.email == email), None)
        if teacher:
            if isinstance(user, Admin):
                user.editTeacher(teacher, **kwargs)
            else:
                print("There is no permission")
        else:
            print("User not found")

