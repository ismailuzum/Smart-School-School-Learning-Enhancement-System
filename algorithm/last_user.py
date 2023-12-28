class User():
    def __init__(self, first_name, last_name, email, password, user_status):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.user_status = user_status

class Student(User):
    def __init__(self, first_name, last_name, email, password, user_status, student_id):
        super().__init__(first_name, last_name, email, password, user_status)
        self.student_id = student_id

class Teacher(User):
    def __init__(self, first_name, last_name, email, password, user_status, teacher_id):
        super().__init__(first_name, last_name, email, password, user_status)
        self.teacher_id = teacher_id

class Admin(User):
    def __init__(self, first_name, last_name, email, password, user_status, admin_id):
        super().__init__(first_name, last_name, email, password, user_status)
        self.admin_id = admin_id

    def editTeacher(self, teacher, **kwargs):
        for key, value in kwargs.items():
                setattr(teacher, key, value)

