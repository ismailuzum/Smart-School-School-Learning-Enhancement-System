from user import User

class Admin(User):
    def login(self):
        print("Admin logged in")

    def logout(self):
        print("Admin logged out")

    def createTeacherAccount(self):
        print("Teacher account created")

    def viewAllUsers(self):
        print("Viewing all users")
