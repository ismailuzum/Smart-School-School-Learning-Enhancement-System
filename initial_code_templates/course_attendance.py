class Course_Attendance:
    def __init__(self, course_attendance_id, student_id, course_id, course_dates, course_status):
        self.course_attendance_id = course_attendance_id
        self.student_id = student_id
        self.course_id = course_id
        self.course_dates = course_dates
        self.course_status = course_status

    def create_course_Attendance(self, student_id, course_id, course_dates, course_status):
        self.student_id = student_id
        self.course_id = course_id
        self.course_dates = course_dates
        self.course_status = course_status
        print("Course_Attendance record created")

    def update_course_Attendance(self, new_course_dates, new_course_status):
        self.new_course_dates = new_course_dates
        self.new_course_status = new_course_status
        print("Course_Attendance record updated")

    def view_course_Attendance(self):
        print("Course_Attendance:", self.course_dates, self.course_status)
        return self.course_dates, self.course_status
