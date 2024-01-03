from user import User

class Student(User):
    def __init__(self, user_id, email, password, role, profile_info, course_schedule, lesson_attendance, mentor_meeting_schedule, mentor_meeting_attendance):
        super().__init__(user_id, email, password, role)
        self.profile_info = profile_info
        self.course_schedule = course_schedule
        self.lesson_attendance = lesson_attendance
        self.mentor_meeting_schedule = mentor_meeting_schedule
        self.mentor_meeting_attendance = mentor_meeting_attendance

    def login(self):
        print("Student logged in")

    def logout(self):
        print("Student logged out")

    def signUp(self):
        print("Student signed up")

    def editProfile(self):
        print("Student profile edited")

    def viewCourseSchedule(self):
        return self.course_schedule

    def viewLessonAttendance(self):
        return self.lesson_attendance

    def viewMentorMeetingSchedule(self):
        return self.mentor_meeting_schedule

    def viewMentorMeetingAttendance(self):
        return self.mentor_meeting_attendance

    def viewAnnouncements(self):
        print("Viewing announcements")

    def sendMessage(self, message):
        print("Message sent:", message)

    def viewToDoList(self):
        print("Viewing to-do list")

    def reactToDoList(self):
        print("Reacted to to-do list")
