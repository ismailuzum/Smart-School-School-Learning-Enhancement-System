from user import User

class Teacher(User):
    def __init__(self, user_id, email, password, role, profile_info, course_schedule, lesson_attendance, mentor_meeting_schedule, mentor_meeting_attendance):
        super().__init__(user_id, email, password, role)
        self.profile_info = profile_info
        self.course_schedule = course_schedule
        self.lesson_attendance = lesson_attendance
        self.mentor_meeting_schedule = mentor_meeting_schedule
        self.mentor_meeting_attendance = mentor_meeting_attendance

    def login(self):
        print("Teacher logged in")

    def logout(self):
        print("Teacher logged out")

    def editProfile(self):
        print("Teacher profile edited")

    def createCourseSchedule(self):
        print("Course schedule created")

    def editCourseSchedule(self):
        print("Course schedule edited")

    def viewCourseSchedule(self):
        return self.course_schedule

    def createLessonAttendance(self):
        print("Lesson attendance created")

    def editLessonAttendance(self):
        print("Lesson attendance edited")

    def viewLessonAttendance(self):
        return self.lesson_attendance

    def createMentorMeetingSchedule(self):
        print("Mentor meeting schedule created")

    def editMentorMeetingSchedule(self):
        print("Mentor meeting schedule edited")

    def viewMentorMeetingSchedule(self):
        return self.mentor_meeting_schedule

    def createMentorMeetingAttendance(self):
        print("Mentor meeting attendance created")

    def editMentorMeetingAttendance(self):
        print("Mentor meeting attendance edited")

    def viewMentorMeetingAttendance(self):
        return self.mentor_meeting_attendance

    def createAnnouncement(self):
        print("Announcement created")

    def viewAnnouncements(self):
        print("Viewing announcements")

    def sendMessage(self, message):
        print("Message sent:", message)

    def createToDoList(self):
        print("To-do list created")

    def editToDoList(self):
        print("To-do list edited")
